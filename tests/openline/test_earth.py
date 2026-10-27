"""openline.electrical's earth return: Carson's integral in closed form against high-precision
values and against its definition by quadrature, and its low-frequency series; Wise's integral
against its definition and his own example; and no return at DC. How the return enters a line's
impedance and admittance is test_electrical's."""

import cmath
import math
from itertools import pairwise

import pytest

from openline.electrical import _earth, _span, series, shunt
from openline.types.environment import Earth
from openline.types.lines import Placed
from openline.types.structures.geometry import Point
from openline.types.units import hz, m, mm, ohm_m

# mpmath at 80 decimal digits: pi*(struveh(1,b)-bessely(1,b))/(2*b) - 1/b**2, by each method's
# boundary; the large left-half-plane ones once stalled in the decimal power series.
F = [
    (1.999j, 0.1801902366110163 - 0.38329223258907824j),
    (2j, 0.18006705909173878 - 0.3831777525972876j),
    (2.001j, 0.179943996319722 - 0.38306332746208843j),
    (39.999j, 0.000625031251171914 - 0.024984969262185856j),
    (40j, 0.000625 - 0.02498434542220594j),
    (40.001j, 0.0006249687511718359 - 0.024983721613358278j),
    (-40 + 1j, -0.025320004119939635 - 0.004288944708581758j),
    (-800 + 1j, -0.0012386603871145522 - 4.022321511201747e-05j),
    (-10000 + 10j, -0.00010001000210565212 - 1.0007207757689057e-07j),
]
# An independent 80-digit evaluation of Theodoulidis (2015), equation (3), divided by 2.
MUTUAL = [
    (5.0, 2000.0, 0.0001 + 0.4j, 3.973270190670824e-07 - 8.941997028918078e-06j),
    (30.0, 80.0, 0.3 + 0.3j, 0.006862415018802516 - 0.007409663767733495j),
    (5.0, 1000.0, 0.00001 + 0.8j, -1.2389072127840065e-06 - 7.200800516281906e-06j),
]
WIRES = (Placed(mm(14), Point(m(0), m(0), m(20))), Placed(mm(14), Point(m(8), m(0), m(20))))


def defined(above: float, apart: float, m: complex, square: complex = 1) -> complex:
    """Wise's integral as it is defined, by quadrature, in t = above * lambda; at n^2 = 1,
    Carson's."""
    p = m * above
    q = apart / above

    def term(t: float) -> list[complex]:
        return [math.exp(-t) * math.cos(q * t) / (square * t + cmath.sqrt(t * t + p * p))]

    edges = [0.0, min(abs(p / square), abs(p), 1.0) / 64]
    while edges[-1] < 1:
        edges.append(min(2 * edges[-1], 1.0))
    while edges[-1] < 45:
        edges.append(min(edges[-1] + 1, 45.0))
    edges = sorted({*edges, min(abs(p), 45.0)})  # where a low-loss earth's root nears the axis
    return sum((_span.integral(term, a, b)[0] for a, b in pairwise(edges)), 0j)


@pytest.mark.parametrize(("beta", "expected"), F)
def test_carson_s_function_meets_high_precision_values(beta: complex, expected: complex) -> None:
    found = _earth._f(beta)
    assert (found.real, found.imag) == pytest.approx(
        (expected.real, expected.imag), rel=2e-13, abs=0
    )


@pytest.mark.parametrize("beta", [beta for beta, _ in F])
def test_carson_s_function_of_a_conjugate_is_its_conjugate(beta: complex) -> None:
    assert _earth._f(beta.conjugate()) == pytest.approx(
        _earth._f(beta).conjugate(), rel=2e-13, abs=0
    )


@pytest.mark.parametrize(("above", "apart", "m", "expected"), MUTUAL)
def test_carson_s_integral_over_a_low_loss_earth_meets_high_precision_values(
    above: float, apart: float, m: complex, expected: complex
) -> None:
    found = _earth.carson(above, apart, m)
    assert (found.real, found.imag) == pytest.approx(
        (expected.real, expected.imag), rel=2e-12, abs=0
    )


@pytest.mark.parametrize(("above", "apart", "m"), [row[:3] for row in MUTUAL])
def test_carson_s_integral_is_alike_either_side(above: float, apart: float, m: complex) -> None:
    assert _earth.carson(above, -apart, m) == _earth.carson(above, apart, m)


@pytest.mark.parametrize("frequency", [1.0, 60.0, 1e3, 1e5, 1e7])
@pytest.mark.parametrize("resistivity", [1.0, 100.0, 10000.0])
@pytest.mark.parametrize("permittivity", [1.0, 15.0])
def test_carson_in_closed_form_is_its_integral(
    frequency: float, resistivity: float, permittivity: float
) -> None:  # small, intermediate and large |beta|
    m, _ = _earth._constants(frequency, resistivity, permittivity)
    pairs = [(above, apart) for above in (5.0, 30.0, 120.0) for apart in (0.0, 10.0, 80.0)]
    closed = [_earth.carson(above, apart, m) for above, apart in pairs]
    exact = [defined(above, apart, m) for above, apart in pairs]
    assert closed == pytest.approx(exact, rel=1e-12, abs=0)


def test_carson_at_low_frequency_is_its_series() -> None:  # Carson: P = pi/8 - p/(3 sqrt 2) ...
    above = 50.0
    p = above * math.sqrt(2 * math.pi * 0.001 * 4e-7 * math.pi / 100)
    m, _ = _earth._constants(0.001, 100.0, 1.0)
    assert -_earth.carson(above, 0.0, m).imag == pytest.approx(
        math.pi / 8 - p / (3 * math.sqrt(2)), abs=1e-6
    )


@pytest.mark.parametrize("frequency", [60.0, 1e4, 1e6, 1e7])
@pytest.mark.parametrize("resistivity", [10.0, 1000.0])
@pytest.mark.parametrize("permittivity", [1.0, 15.0])
def test_wise_is_its_integral(frequency: float, resistivity: float, permittivity: float) -> None:
    m, square = _earth._constants(frequency, resistivity, permittivity)
    pairs = [(above, apart) for above in (10.0, 40.0, 120.0) for apart in (0.0, 10.0, 60.0)]
    exact = [defined(above, apart, m, square) for above, apart in pairs]
    largest = max(map(abs, exact))
    found = _earth.wise(pairs, m, square)
    assert (
        max(abs(ours - given) for ours, given in zip(found, exact, strict=True)) <= 1e-12 * largest
    )


def test_wise_is_wise_s_example() -> None:  # 1948, p. 365: by his approximation (10), to 2%
    m, square = _earth._constants(2e6, 100.0, 15.0)  # sigma 1e-13 emu, epsilon 15, 2 MHz
    (integral,) = _earth.wise([(0.06, 0.0)], m, square)  # a wire 3 cm up, with itself
    assert (4 * integral.real, 4 * integral.imag) == pytest.approx((0.152, 0.319), rel=0.02)


def test_the_earth_returns_no_current_at_dc() -> None:
    earth = series.earth(*WIRES, frequency=hz(0), earth=Earth(ohm_m(100), 15))
    assert (earth.resistance.si, earth.reactance.si) == (0, 0)


def test_the_earth_holds_no_charge_at_dc() -> None:
    earth = shunt.earth(*WIRES, frequency=hz(0), earth=Earth(ohm_m(100), 15))
    assert (earth.real.si, earth.imaginary.si) == (0, 0)
