"""openline.electrical's propagation and openline.types.propagation: a line's current waves over a
length, by its coupled phase matrices, against lines of known modes; the modes tracked across a
sweep of frequencies, and their delays found by Bode's minimum phase; and a pulse carried along a
lossless line."""

import cmath
from typing import Any

import numpy as np
import pytest
from numpy.typing import NDArray
from scipy.linalg import expm  # type: ignore[import-untyped]

from openline import (
    Bundle,
    Circuit,
    Earth,
    Line,
    Shield,
    Strung,
    conductors,
    electrical,
    structures,
)
from openline import units as u
from openline.electrical import _propagation
from openline.types.lines import Phases
from openline.types.parameters import Parameters
from openline.types.propagation import Propagation, PropagationSweep

type Matrix = NDArray[np.complex128]

LENGTH, FREQUENCY = u.km(37), u.hz(1000)


def parameters(z: Matrix, y: Matrix) -> Parameters:
    """``z`` and ``y`` as a line's impedance and admittance, its circuits named 1, 2 ..."""
    labels = tuple(f"{i // 3 + 1}.{'ABC'[i % 3]}" for i in range(len(z)))
    return Parameters(
        impedance=Phases(
            tuple(
                tuple(
                    u.Impedance(u.ResistancePerLength(v.real), u.ReactancePerLength(v.imag))
                    for v in row
                )
                for row in z
            ),
            labels,
        ),
        admittance=Phases(
            tuple(
                tuple(
                    u.Admittance(u.ConductancePerLength(v.real), u.SusceptancePerLength(v.imag))
                    for v in row
                )
                for row in y
            ),
            labels,
        ),
    )


def line() -> Line:
    """Drake on RUS's TH-230 H-frame: a line the sweeps below give their own matrices."""
    frame = structures.frame.TH_230
    return Line(
        structure=frame,
        height=u.m(22),
        span=u.m(300),
        circuits=(
            Circuit.uniform(
                conductors.astm.b232.DRAKE,
                at=dict(zip("ABC", frame.phases, strict=True)),
                strung=Strung(u.kn(28), u.celsius(15)),
                insulator_drop=u.m(2.5),
            ),
        ),
        shields=(),
        earth=Earth(u.ohm_m(100), 10),
    )


class Known:
    """A line of ``size`` known modes: Z = T diag(z) Tᵀ and Y = T⁻ᵀ diag(y) T⁻¹, so that each
    mode propagates by sqrt(z y)."""

    def __init__(self, size: int) -> None:
        self.transform = np.eye(size) + 0.1 * np.tril(np.ones((size, size)), -1)
        self.inverse = np.linalg.solve(self.transform, np.eye(size))
        self.z = np.arange(1, size + 1) * (1e-4 + 2e-3j)
        self.y = np.arange(1, size + 1) * (1e-9 + 3e-7j)
        self.roots = np.array([cmath.sqrt(a * b) for a, b in zip(self.z, self.y, strict=True)])
        self.parameters = parameters(
            np.asarray(self.transform @ np.diag(self.z) @ self.transform.T, dtype=np.complex128),
            np.asarray(self.inverse.T @ np.diag(self.y) @ self.inverse, dtype=np.complex128),
        )
        self.sample, self.vectors = _propagation._sample(self.parameters, FREQUENCY, LENGTH, None)


SIZES = [1, 3, 6]


@pytest.mark.parametrize("size", SIZES)
def test_the_function_carries_each_known_mode_by_its_own_decay(size: int) -> None:
    known = Known(size)
    decay = np.diag(np.exp(-LENGTH.si * known.roots))
    expected = known.inverse.T @ decay @ known.transform.T
    np.testing.assert_allclose(known.sample.function.rows, expected, rtol=1e-11, atol=1e-13)


@pytest.mark.parametrize("size", SIZES)
def test_the_characteristic_admittance_is_the_known_modes(size: int) -> None:
    known = Known(size)
    expected = known.inverse.T @ np.diag(known.roots / known.z) @ known.inverse
    found = known.sample.characteristic_admittance.to(u.siemens)
    np.testing.assert_allclose(found, expected, rtol=1e-11, atol=1e-13)


@pytest.mark.parametrize("size", SIZES)
def test_each_mode_propagates_by_its_known_constant(size: int) -> None:
    known = Known(size)
    found = [mode.constant.to(u.per_m) for mode in known.sample.modes]
    np.testing.assert_allclose(found, known.roots, rtol=1e-11)


@pytest.mark.parametrize("size", SIZES)
def test_each_mode_is_delayed_by_its_phase_constant(size: int) -> None:  # length β / ω
    known = Known(size)
    found = [mode.phase_delay.si for mode in known.sample.modes]
    expected = LENGTH.si * known.roots.imag / (2 * np.pi * FREQUENCY.si)
    np.testing.assert_allclose(found, expected)


def test_a_propagation_names_its_rows_as_its_line_s_phases() -> None:
    known = Known(6)
    assert known.sample.function.labels == known.parameters.impedance.labels


def mixed() -> tuple[Parameters, Propagation, Matrix]:
    """Two modes mixed by a complex transform, its sample and its current modes."""
    transform = np.array([[1, 0.2 + 0.1j], [0.1 - 0.1j, 1]])
    inverse = np.linalg.solve(transform, np.eye(2))
    z = transform @ np.diag([1e-4 + 2e-3j, 2e-4 + 3e-3j]) @ transform.T
    y = inverse.T @ np.diag([1e-9 + 3e-7j, 2e-9 + 4e-7j]) @ inverse
    given = parameters(z, y)
    sample, currents = _propagation._sample(given, u.hz(1000), u.km(10), None)
    return given, sample, currents


def test_each_mode_s_admittance_carries_its_own_power() -> None:
    given, sample, currents = mixed()
    z = np.asarray(given.impedance.to(u.ohm_per_m))
    y = np.asarray(given.admittance.to(u.s_per_m))
    yc = np.asarray(sample.characteristic_admittance.to(u.siemens))
    modal = np.array([mode.characteristic_admittance.to(u.siemens) for mode in sample.modes])
    gamma = np.array([mode.constant.to(u.per_m) for mode in sample.modes])
    voltages = np.linalg.solve(yc, currents) * modal
    np.testing.assert_allclose(np.diag(currents.conj().T @ voltages), np.ones(2), atol=1e-13)
    np.testing.assert_allclose(
        np.linalg.solve(voltages, z @ currents), np.diag(gamma / modal), atol=1e-13
    )
    np.testing.assert_allclose(
        np.linalg.solve(currents, y @ voltages), np.diag(gamma * modal), atol=1e-13
    )


def test_a_mode_s_admittance_is_not_its_eigenvector_s_scale(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    given, sample, _ = mixed()
    eig = np.linalg.eig

    def rescaled(matrix: Matrix) -> tuple[Matrix, Matrix]:
        values, vectors = eig(matrix)
        return values, vectors * np.array([2j, -3 + 4j])

    monkeypatch.setattr(np.linalg, "eig", rescaled)
    scaled, _ = _propagation._sample(given, u.hz(1000), u.km(10), None)
    np.testing.assert_allclose(
        [mode.characteristic_admittance.to(u.siemens) for mode in scaled.modes],
        [mode.characteristic_admittance.to(u.siemens) for mode in sample.modes],
        rtol=1e-13,
    )


def test_exactly_repeated_modes_leave_the_phase_matrices_defined() -> None:
    roots = np.array([1e-5 + 2e-3j, 1e-5 + 2e-3j, 2e-5 + 3e-3j])
    matrix = np.diag(roots)
    sample, basis = _propagation._sample(parameters(matrix, matrix), u.hz(10), u.km(2), None)
    repeated, _ = _propagation._sample(parameters(matrix, matrix), u.hz(20), u.km(2), basis)
    np.testing.assert_allclose(repeated.function.rows, np.diag(np.exp(-2000 * roots)))
    np.testing.assert_allclose(
        repeated.characteristic_admittance.to(u.siemens), np.eye(3), atol=1e-13
    )
    assert [mode.constant for mode in repeated.modes] == [mode.constant for mode in sample.modes]


TRANSFORM = np.array([[1.0, 0.2, 0.1], [0.1, 1.0, 0.3], [0.2, 0.1, 1.0]])
CROSSING = np.array([[1, 2, 3], [2, 2 + 1e-8, 3], [2.1, 1.9, 3]]) * 1e-3  # β by sample, mode


def crossing(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Give the line, at 1, 2 and 3 Hz, matrices whose modes' phase constants cross, in place of
    its own; the frequencies they are asked for at, in order."""
    inverse = np.linalg.solve(TRANSFORM, np.eye(3))
    asked: list[float] = []

    def given(_: Line, *, temperature: u.Temperature, frequency: u.Frequency) -> Parameters:
        asked.append(frequency.si)
        roots = 1e-5 + 1j * CROSSING[int(frequency.si) - 1]
        return parameters(
            np.asarray(TRANSFORM @ np.diag(roots) @ TRANSFORM.T, dtype=np.complex128),
            np.asarray(inverse.T @ np.diag(roots) @ inverse, dtype=np.complex128),
        )

    monkeypatch.setattr(_propagation, "parameters", given)
    return asked


def swept() -> PropagationSweep:
    """The line's sweep of 1, 2 and 3 Hz over 10 km."""
    return electrical.propagation_sweep(
        line(), temperature=u.celsius(50), frequencies=map(u.hz, (1, 2, 3)), length=u.km(10)
    )


def test_a_sweep_tracks_modes_whose_phase_constants_cross(monkeypatch: pytest.MonkeyPatch) -> None:
    crossing(monkeypatch)
    phases = [[mode.constant.phase.si for mode in sample.modes] for sample in swept()]
    np.testing.assert_allclose(phases, CROSSING, rtol=1e-10)


def test_a_sweep_reads_as_its_samples(monkeypatch: pytest.MonkeyPatch) -> None:
    crossing(monkeypatch)
    sweep = swept()
    assert (tuple(sweep), sweep[1:], len(sweep)) == (sweep.samples, sweep.samples[1:], 3)


def test_one_frequency_s_propagation_is_a_sweep_s_sample(monkeypatch: pytest.MonkeyPatch) -> None:
    crossing(monkeypatch)
    alone = electrical.propagation(
        line(), temperature=u.celsius(50), frequency=u.hz(1), length=u.km(10)
    )
    assert alone == swept()[0]


def bundled() -> Line:
    """Four Dipper subconductors per phase, with two Turkey shields, on a 765 kV tower."""
    tower = structures.tower.TYPICAL_765KV_TANGENT_TOWER
    return Line(
        structure=tower,
        height=u.m(35),
        span=u.m(450),
        circuits=(
            Circuit.uniform(
                Bundle(conductor=conductors.astm.b232.DIPPER, count=4, spacing=u.m(0.457)),
                at=dict(zip("ABC", tower.phases, strict=True)),
                strung=Strung(u.kn(40), u.celsius(15)),
            ),
        ),
        shields=Shield.each(
            conductors.astm.b232.TURKEY,
            at=tower.shields,
            strung=Strung(u.kn(8), u.celsius(15)),
        ),
        earth=Earth(u.ohm_m(100), 10),
    )


def terminal_blocks(sample: Propagation) -> tuple[Matrix, Matrix]:
    """The sample's equal- and opposite-voltage terminal admittances, in siemens."""
    return _propagation._terminal_blocks(
        np.asarray(sample.characteristic_admittance.to(u.siemens)),
        np.asarray(sample.function.rows),
    )


def passivity_margin(sample: Propagation) -> float:
    """Smallest Hermitian eigenvalue of the complete terminal admittance, in siemens."""
    return min(
        float(np.linalg.eigvalsh((block + block.conj().T) / 2)[0])
        for block in terminal_blocks(sample)
    )


@pytest.mark.parametrize("size", SIZES)
def test_the_terminal_blocks_match_the_telegrapher_equations(size: int) -> None:
    known = Known(size)
    z = np.asarray(known.parameters.impedance.to(u.ohm_per_m))
    y = np.asarray(known.parameters.admittance.to(u.s_per_m))
    zero = np.zeros_like(z)
    transfer = expm(-LENGTH.si * np.block([[zero, z], [y, zero]]))
    a, b = transfer[:size, :size], transfer[:size, size:]
    c, d = transfer[size:, :size], transfer[size:, size:]
    near, far = np.linalg.solve(b, -a), np.linalg.solve(b, np.eye(size))
    terminal = np.block([[near, far], [-c - d @ near, -d @ far]])
    same, opposite = terminal_blocks(known.sample)
    transform = np.block([[np.eye(size), np.eye(size)], [np.eye(size), -np.eye(size)]])
    expected = transform @ np.block([[same, zero], [zero, opposite]]) @ transform / 2
    np.testing.assert_allclose(terminal, expected, rtol=1e-10, atol=1e-12)


def test_decaying_modes_do_not_guarantee_positive_terminal_power() -> None:
    # An intentionally active shunt: forward waves decay, but equal end voltages supply power.
    z, y = np.array([[1 + 10j]]), np.array([[-0.01 + 1j]])
    length = u.m(0.01)
    sample, _ = _propagation._sample(parameters(z, y), FREQUENCY, length, None)
    assert abs(sample.modes[0].function) < 1
    assert passivity_margin(sample) < 0

    same, _ = terminal_blocks(sample)
    initial = np.array([1, same[0, 0]])
    generator = np.block([[np.zeros_like(z), z], [y, np.zeros_like(y)]])
    nodes, weights = np.polynomial.legendre.leggauss(8)
    loss = 0.0
    for node, weight in zip(nodes, weights, strict=True):
        voltage, current = expm(-(node + 1) * length.si / 2 * generator) @ initial
        loss += weight * (abs(current) ** 2 * z[0, 0].real + abs(voltage) ** 2 * y[0, 0].real)
    # Peak phasors: one half of the integrated series and shunt losses equals both ports' power.
    assert loss * length.si / 4 == pytest.approx(same[0, 0].real, rel=1e-11)


@pytest.mark.parametrize("frequency", [10**7.5, 1e8])
def test_a_300_km_bundled_line_is_passive_at_high_frequency(frequency: float) -> None:
    # Separate span averages made this line's ground mode grow above 30.7 MHz.
    sample = electrical.propagation(
        bundled(), temperature=u.celsius(50), frequency=u.hz(frequency), length=u.km(300)
    )
    for mode in sample.modes:
        gamma = mode.constant.to(u.per_m)
        assert gamma.real > 0
        assert gamma.imag > 0

    assert passivity_margin(sample) > 0


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="The quasi-TEM earth model has negative shunt loss near 28.5 MHz.",
)
@pytest.mark.parametrize("length", [10, 50])
def test_a_short_bundled_line_is_passive_at_high_frequency(length: float) -> None:
    sample = electrical.propagation(
        bundled(), temperature=u.celsius(50), frequency=u.hz(28.5e6), length=u.m(length)
    )
    assert passivity_margin(sample) >= 0


def test_a_sweep_s_delays_take_no_more_line_parameters(monkeypatch: pytest.MonkeyPatch) -> None:
    asked = crossing(monkeypatch)
    delays = swept().minimum_delays()
    assert asked == [1, 2, 3]
    expected = 10e3 * CROSSING[-1] / (2 * np.pi * 3)  # flat magnitudes: the last sample's
    np.testing.assert_allclose([delay.si for delay in delays], expected)


def test_no_length_carries_a_wave_unchanged(monkeypatch: pytest.MonkeyPatch) -> None:
    crossing(monkeypatch)
    zero = electrical.propagation(
        line(), temperature=u.celsius(50), frequency=u.hz(1), length=u.m(0)
    )
    np.testing.assert_allclose(zero.function.rows, np.eye(3), atol=1e-15)
    assert [(mode.function, mode.phase_delay.si) for mode in zero.modes] == [(1, 0)] * 3


@pytest.mark.parametrize("irregular", [False, True], ids=["even", "uneven"])
@pytest.mark.parametrize("weights", [(1, 1, 1), (1, -2, 1)], ids=["poles", "poles and zero"])
def test_bode_s_phase_is_a_known_minimum_phase_response_s(
    irregular: bool, weights: tuple[int, ...]
) -> None:
    x = np.linspace(-6, 12, 1441)
    if irregular:
        x += 0.002 * np.sin(np.arange(len(x)))
    frequencies = 10**x
    poles = np.array([100, 1700, 40000])
    exponent = (np.log1p(1j * frequencies[:, None] / poles) * weights).sum(axis=1)
    for frequency in (17, 630, 7200, 150000):
        index = int(np.argmin(abs(frequencies - frequency)))
        phase = _propagation._minimum_phase(np.log(frequencies), -exponent.real, index)
        assert phase == pytest.approx(-exponent[index].imag, rel=6e-4)


def test_a_cutoff_delay_recovers_known_delays_without_unwrapping() -> None:
    frequencies = np.geomspace(1e-3, 1e10, 781)
    expected = np.array([80e-6, 340e-6, 1000e-6])
    samples, previous = [], None
    for frequency in frequencies:
        s = 2j * np.pi * frequency
        # two delayed low-pass responses, and a pure delay whose H underflows
        roots = expected * s + np.array(
            [3 * np.log1p(s / (2 * np.pi * 1700)), 2 * np.log1p(s / (2 * np.pi * 4000)), 1000]
        )
        sample, previous = _propagation._sample(
            parameters(np.diag(roots), np.diag(roots)), u.hz(float(frequency)), u.m(1), previous
        )
        samples.append(sample)
    sweep = PropagationSweep(samples=tuple(samples))
    assert all(sample.modes[2].function == 0 for sample in sweep)
    for cutoff in (1e-3, 1e-5):  # the highest frequency's phase turns millions of times a step
        delays = sweep.minimum_delays(magnitude_cutoff=cutoff)
        np.testing.assert_allclose([d.si for d in delays], expected, rtol=2e-5, atol=1e-10)


def lossless() -> tuple[Matrix, Matrix, NDArray[np.floating[Any]]]:
    """A band-limited pulse's current along a 20 km lossless line of 1 µH/m and 25 pF/m, 200 Mm/s:
    its spectrum after the line, the voltage's at its start, and the pulse, by 25 µs steps."""
    count, step = 256, 25e-6
    time = np.arange(count) * step
    offset = (time - 8e-4) / 1e-4
    pulse = offset * np.exp(-(offset**2) / 2)
    pulse /= np.max(np.abs(pulse))
    source = np.fft.rfft(pulse)
    source[[0, -1]] = 0
    pulse = np.fft.irfft(source, n=count)
    current, voltage = (np.zeros(len(source), dtype=np.complex128) for _ in range(2))
    for index, frequency in enumerate(np.fft.rfftfreq(count, step)[1:], start=1):
        omega = 2 * np.pi * frequency
        z, y = np.array([[1j * omega * 1e-6]]), np.array([[1j * omega * 25e-12]])
        sample, _ = _propagation._sample(parameters(z, y), u.hz(float(frequency)), u.km(20), None)
        current[index] = source[index] * sample.function[0][0]
        voltage[index] = source[index] / sample.characteristic_admittance[0][0].to(u.siemens)
    return current, voltage, pulse


def test_a_pulse_arrives_unchanged_after_the_lossless_line_s_delay() -> None:  # 100 µs
    current, _, pulse = lossless()
    np.testing.assert_allclose(np.fft.irfft(current, n=len(pulse)), np.roll(pulse, 4), atol=1e-13)


def test_a_lossless_line_s_voltage_is_its_characteristic_impedance_s_times_its_current() -> None:
    _, voltage, pulse = lossless()  # sqrt(L / C): 200 Ω
    np.testing.assert_allclose(np.fft.irfft(voltage, n=len(pulse)), 200 * pulse, atol=1e-11)


@pytest.mark.parametrize(
    "frequencies", [(), (0,), (-1,), (float("nan"),), (float("inf"),), (2, 1), (1, 1)]
)
def test_a_sweep_takes_positive_increasing_frequencies(frequencies: tuple[float, ...]) -> None:
    with pytest.raises(ValueError, match="frequenc"):
        electrical.propagation_sweep(
            line(), temperature=u.celsius(50), frequencies=map(u.hz, frequencies), length=u.km(10)
        )


@pytest.mark.parametrize("length", [-1.0, float("inf"), float("nan")])
def test_a_propagation_s_length_is_finite_and_not_negative(length: float) -> None:
    with pytest.raises(ValueError, match="length"):
        electrical.propagation(
            line(), temperature=u.celsius(50), frequency=u.hz(60), length=u.m(length)
        )


@pytest.mark.parametrize("cutoff", [0, 1, 2])
def test_a_delay_s_magnitude_cutoff_is_between_zero_and_one(
    monkeypatch: pytest.MonkeyPatch, cutoff: float
) -> None:
    crossing(monkeypatch)
    with pytest.raises(ValueError, match="between zero and one"):
        swept().minimum_delays(magnitude_cutoff=cutoff)


def test_delays_take_three_frequencies_or_more() -> None:
    known = Known(3)
    with pytest.raises(ValueError, match="three frequencies"):
        PropagationSweep(samples=(known.sample, known.sample)).minimum_delays()
