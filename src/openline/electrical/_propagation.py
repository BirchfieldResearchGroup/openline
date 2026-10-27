"""Numerical propagation kernel, imported only by propagation calculations."""

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm, solve, sqrtm  # type: ignore[import-untyped]
from scipy.optimize import linear_sum_assignment  # type: ignore[import-untyped]

from ..types.lines import Line, Phases
from ..types.parameters import Parameters
from ..types.propagation import Propagation, PropagationMode, PropagationSweep
from ..types.units import (
    Attenuation,
    CharacteristicAdmittance,
    Conductance,
    Duration,
    Frequency,
    Length,
    PhaseConstant,
    PropagationConstant,
    Susceptance,
    Temperature,
    ohm_per_m,
    s_per_m,
)
from . import parameters

type Matrix = NDArray[np.complex128]


def _terminal_blocks(yc: Matrix, h: Matrix) -> tuple[Matrix, Matrix]:
    """Admittance for equal/opposite end voltages: (I +/- H)^-1 (I -/+ H) Yc.

    Terminal passivity requires both Hermitian parts to be positive semidefinite;
    decaying modes alone are insufficient. Currents point into both ends.
    """
    identity = np.eye(len(h))
    return (
        np.linalg.solve(identity + h, identity - h) @ yc,
        np.linalg.solve(identity - h, identity + h) @ yc,
    )


def minimum_delays(sweep: PropagationSweep, *, magnitude_cutoff: float) -> tuple[Duration, ...]:
    """Bode delay extraction: De Tommasi and Gustavsen, IPST 2007, (9)-(13).

    https://www.ipstconf.org/papers/Proc_IPST2007/07IPST025.pdf
    """
    if not 0 < magnitude_cutoff < 1:
        raise ValueError("magnitude_cutoff must be between zero and one")
    if len(sweep) < 3:
        raise ValueError("delay extraction requires at least three frequencies")
    frequencies = np.array([sample.frequency.si for sample in sweep])
    log_frequency = np.log(frequencies)
    # log|H| = -length * alpha, even when exp(-length * alpha) underflows.
    log_magnitude = np.array(
        [
            [-sample.length.si * mode.constant.attenuation.si for mode in sample.modes]
            for sample in sweep
        ]
    )
    delays = []
    for mode, magnitude in enumerate(log_magnitude.T):
        crossings = np.flatnonzero(magnitude <= np.log(magnitude_cutoff))
        index = int(crossings[0]) if crossings.size else len(sweep) - 1
        phase = _minimum_phase(log_frequency, magnitude, index)
        delays.append(
            Duration(
                sweep[index].modes[mode].phase_delay.si + phase / (2 * np.pi * frequencies[index])
            )
        )
    return tuple(delays)


def _minimum_phase(
    log_frequency: NDArray[np.float64], log_magnitude: NDArray[np.float64], index: int
) -> float:
    """Bode integral with the local slope separated from the correction integral.

    The correction is integrated over the supplied band, with no tail extrapolation.
    Its integrand tends to zero at the logarithmic kernel's singularity.
    """
    slope = np.gradient(log_magnitude, log_frequency, edge_order=2)
    distance = np.abs(log_frequency - log_frequency[index])
    kernel = np.zeros_like(distance)
    other = distance > 0
    kernel[other] = -np.log(np.tanh(distance[other] / 2))
    correction = np.trapezoid((slope - slope[index]) * kernel, log_frequency) / np.pi
    return float(np.pi / 2 * slope[index] + correction)


def calculate(
    line: Line, *, temperature: Temperature, frequencies: tuple[Frequency, ...], length: Length
) -> PropagationSweep:
    found: list[Propagation] = []
    previous: Matrix | None = None
    for frequency in frequencies:
        sample, previous = _sample(
            parameters(line, temperature=temperature, frequency=frequency),
            frequency,
            length,
            previous,
        )
        found.append(sample)
    return PropagationSweep(samples=tuple(found))


def _sample(
    parameters: Parameters, frequency: Frequency, length: Length, previous: Matrix | None
) -> tuple[Propagation, Matrix]:
    z = np.asarray(parameters.impedance.to(ohm_per_m), dtype=np.complex128)
    y = np.asarray(parameters.admittance.to(s_per_m), dtype=np.complex128)
    gamma = np.asarray(sqrtm(y @ z), dtype=np.complex128)
    function = np.asarray(expm(-length.si * gamma), dtype=np.complex128)
    yc = np.asarray(solve(gamma, y), dtype=np.complex128)

    values, vectors = np.linalg.eig(gamma)
    if previous is None:
        order = np.lexsort((values.real, values.imag))
    else:
        overlap = np.abs(np.linalg.solve(previous, vectors))
        _, order = linear_sum_assignment(overlap, maximize=True)
    values, vectors = values[order], vectors[:, order]
    modal_yc = (
        values
        * np.sum(np.abs(vectors) ** 2, axis=0)
        / np.sum(vectors.conj() * (z @ vectors), axis=0)
    )

    labels = parameters.impedance.labels
    omega = 2 * np.pi * frequency.si
    modes = tuple(
        PropagationMode(
            constant=PropagationConstant(
                Attenuation(float(value.real)),
                PhaseConstant(float(value.imag)),
            ),
            function=complex(np.exp(-length.si * value)),
            characteristic_admittance=CharacteristicAdmittance(
                Conductance(float(admittance.real)), Susceptance(float(admittance.imag))
            ),
            phase_delay=Duration(float(length.si * value.imag / omega)),
        )
        for value, admittance in zip(values, modal_yc, strict=True)
    )
    return (
        Propagation(
            frequency=frequency,
            length=length,
            function=Phases(
                tuple(tuple(complex(value) for value in row) for row in function),
                labels,
            ),
            characteristic_admittance=Phases(
                tuple(
                    tuple(
                        CharacteristicAdmittance(
                            Conductance(float(value.real)),
                            Susceptance(float(value.imag)),
                        )
                        for value in row
                    )
                    for row in yc
                ),
                labels,
            ),
            modes=modes,
        ),
        vectors,
    )
