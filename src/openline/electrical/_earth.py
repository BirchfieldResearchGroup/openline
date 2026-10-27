r"""Earth-return impedance and potential coefficients for a homogeneous half-space.

Evaluate Carson's full integral in closed form and Wise's potential integral by quadrature.
The quasi-TEM model includes soil conductivity and permittivity. All inputs use SI units.
"""

import cmath
import math
from collections.abc import Callable, Sequence
from decimal import Decimal, getcontext, localcontext
from fractions import Fraction
from functools import cache, lru_cache
from itertools import pairwise
from typing import Self

from ..types.units import EPSILON_0, MU_0
from . import _span

__all__ = ["carson", "earth", "external", "potentials", "wise"]

SMALL = 2.0  # use floating-point series below this |beta|
LARGE = 40.0  # use asymptotic evaluation above this |beta|
DIGITS = 17  # target digits, with extra working precision for cancellation
TOLERANCE = 1e-13  # quadrature tolerance relative to the largest potential integral


def external(near: float, image: float, frequency: float) -> float:
    r"""External reactance in Ω/m for wire separation ``near`` and image distance ``image``:

    .. math::  z = j\frac{\omega\mu_0}{2\pi}\ln\frac{D_{ik}}{d_{ik}}

    For self impedance, use the wire radius and twice its height."""
    return frequency * MU_0 * math.log(image / near)


def earth(
    above: float, apart: float, frequency: float, resistivity: float, permittivity: float
) -> complex:
    r"""Earth-return impedance in Ω/m for height sum ``above`` and separation ``apart``:

    .. math::  z = j\frac{\omega\mu_0}{\pi}\,J_{ik}

    ``resistivity`` is in Ω·m; ``permittivity`` is relative to vacuum. Returns zero at DC."""
    if frequency == 0:
        return 0j
    m, _ = _constants(frequency, resistivity, permittivity)
    return 2j * frequency * MU_0 * carson(above, apart, m)


def potentials(
    pairs: Sequence[tuple[float, float]], frequency: float, resistivity: float, permittivity: float
) -> list[complex]:
    r"""Earth potential corrections in m/F for pairs of (height sum, horizontal separation):

    .. math::  p = \frac{1}{\pi\varepsilon_0}\,W_{ik}

    Returns zero at DC."""
    if frequency == 0:
        return [0j] * len(pairs)
    m, square = _constants(frequency, resistivity, permittivity)
    return [value / (math.pi * EPSILON_0) for value in wise(pairs, m, square)]


@lru_cache(maxsize=65536)
def carson(above: float, apart: float, m: complex) -> complex:
    r"""Carson's full integral for height sum ``above`` and horizontal separation ``apart``.

    Use the closed form in Theodoulidis (2015), equation (3):

    .. math::

        J_{ik} = \int_0^\infty \frac{e^{-(h_i + h_k)\xi}\cos x_{ik}\xi}
                 {\xi + \sqrt{\xi^2 + m^2}}\,d\xi
               = \tfrac12\Bigl[F\bigl(m(h_i + h_k - jx_{ik})\bigr)
                 + F\bigl(m(h_i + h_k + jx_{ik})\bigr)\Bigr]

    with

    .. math::

        F(\beta) = \int_0^\infty e^{-\beta\xi}\left(\sqrt{\xi^2 + 1} - \xi\right) d\xi
                 = \frac{\pi}{2\beta}\left[\mathbf H_1(\beta) - Y_1(\beta)\right]
                   - \frac{1}{\beta^2}

    in the Struve function :math:`\mathbf H_1` and the Bessel function of the second kind
    :math:`Y_1`. Carson's conduction-only model uses :math:`m^2 = j\omega\mu_0/\rho`.
    The numerical evaluation retains the full integral, including analytic continuation
    for arguments in the left half-plane."""
    if apart == 0:
        return _f(m * above)
    return (_f(m * complex(above, -apart)) + _f(m * complex(above, apart))) / 2


def wise(pairs: Sequence[tuple[float, float]], m: complex, square: complex) -> list[complex]:
    r"""Wise's potential integral (1948, equation 8), with ``square`` equal to :math:`n^2`:

    .. math::

        W_{ik} = \int_0^\infty \frac{e^{-(h_i + h_k)\xi}\cos x_{ik}\xi}
                 {n^2\xi + \sqrt{\xi^2 + m^2}}\,d\xi

    Integrate on a logarithmic grid near zero and a linear grid through the exponential
    tail, using adaptive Gauss-Legendre quadrature."""
    if not pairs:
        return []
    lowest = min(above for above, _ in pairs)
    highest = max(above for above, _ in pairs)
    near = min(abs(m / square), abs(m), 1 / highest) * 1e-3
    m2 = m * m

    def term(xi: float) -> list[complex]:
        kernel = 1 / (square * xi + cmath.sqrt(xi * xi + m2))
        return [math.exp(-above * xi) * math.cos(apart * xi) * kernel for above, apart in pairs]

    def logged(t: float) -> list[complex]:
        xi = math.exp(t)
        return [value * xi for value in term(xi)]

    start, end = math.log(near), math.log(1 / lowest)
    steps = math.ceil((end - start) / 3)
    edges = [start + (end - start) * i / steps for i in range(steps + 1)]
    parts: list[tuple[Callable[[float], list[complex]], float, float]] = [(term, 0.0, near)]
    parts += [(logged, a, b) for a, b in pairwise(edges)]
    parts += [(term, (1 + 6 * i) / lowest, (7 + 6 * i) / lowest) for i in range(7)]
    rough = [_span.panel(*part) for part in parts]
    largest = max(abs(sum(column)) for column in zip(*rough, strict=True))
    floor = TOLERANCE * largest / len(parts)
    found = [0j] * len(pairs)
    for part in parts:
        summed = _span.integral(*part, floor=floor)
        found = [f + v for f, v in zip(found, summed, strict=True)]
    return found


def _constants(
    frequency: float, resistivity: float, permittivity: float
) -> tuple[complex, complex]:
    r"""Propagation constant :math:`m` and squared refractive index :math:`n^2`.

    The quasi-TEM model uses the wave velocity in air, soil conductivity :math:`\sigma`,
    and relative permittivity :math:`\varepsilon_r`:

    .. math::

        m^2 = j\omega\mu_0\bigl[\sigma + j\omega\varepsilon_0(\varepsilon_r - 1)\bigr], \qquad
        n^2 = \varepsilon_r - j\frac{\sigma}{\omega\varepsilon_0}"""
    omega = 2 * math.pi * frequency
    conducted = 1 / resistivity + 1j * omega * EPSILON_0 * (permittivity - 1)
    m = cmath.sqrt(1j * omega * MU_0 * conducted)
    square = permittivity - 1j / (resistivity * omega * EPSILON_0)
    return m, square


def _f(beta: complex) -> complex:
    r"""Evaluate F with series or asymptotics to floating-point precision.

    Extra decimal precision prevents cancellation in the intermediate range. In the left
    half-plane, retain the Hankel term required by analytic continuation (DLMF 10.11.6):

    .. math::

        F(\beta) = -F(-\beta) - 2/\beta^2
                   + j\pi H_1^{(2)}(-\beta)/\beta, \qquad \mathrm{Im}\,\beta \geq 0.
    """
    if beta.real < 0 and beta.imag < 0:
        return _f(beta.conjugate()).conjugate()
    size = abs(beta)
    if size >= LARGE:
        expanded = _expansion(beta)
        if beta.real < 0:
            expanded += 1j * math.pi / beta * _hankel2(-beta)
        return expanded
    if size < SMALL:
        euler = complex(float(_euler(DIGITS + 3)))
        return _series(beta, cmath.log(beta / 2), euler, 10.0**-DIGITS)
    digits = DIGITS + 3 + math.ceil(size / math.log(10))
    with localcontext() as context:
        context.prec = digits
        z = _Exact(Decimal(beta.real), Decimal(beta.imag))
        value = _series(z, _log(z / 2), _Exact(_euler(digits), Decimal(0)), 10.0**-digits)
        return complex(float(value.re), float(value.im))


def _series[N: (complex, "_Exact")](beta: N, log_half: N, gamma: N, precision: float) -> N:
    r"""F by the power series of :math:`\mathbf H_1` and :math:`Y_1` (A&S 12.1.3 and 9.1.11),
    the :math:`2/\pi\beta` of :math:`Y_1` cancelling the :math:`1/\beta^2`:

    .. math::

        F(\beta) = \frac{1}{2\beta}\left[\sum_q \frac{2(-1)^q\beta^{2q+2}}{(2q+1)!!\,(2q+3)!!}
            + \sum_q (\mathcal H_q + \mathcal H_{q+1})\,b_q
            - 2\left(\ln\frac{\beta}{2} + \gamma\right)\sum_q b_q\right]

    with :math:`b_q = (-1)^q(\beta/2)^{2q+1}/q!\,(q+1)!`, :math:`\mathcal H_q` the harmonic
    numbers and :math:`\gamma` Euler's constant."""
    half = beta / 2
    square = half * half
    term = half
    struve = beta * beta * 2 / 3
    bessel, neumann, total = term, term, struve
    harmonic, k = Fraction(1), 0
    peak = max(abs(term), abs(struve))
    while True:
        term = -term * square / ((k + 1) * (k + 2))
        struve = -struve * square * 4 / ((2 * k + 3) * (2 * k + 5))
        weight = 2 * harmonic + Fraction(1, k + 2)
        harmonic += Fraction(1, k + 2)
        k += 1
        bessel, neumann, total = bessel + term, neumann + term * weight, total + struve
        peak = max(peak, abs(term), abs(struve))
        if max(abs(term) * float(weight), abs(struve)) <= precision * peak:
            return (total + neumann - bessel * (log_half + gamma) * 2) / (beta * 2)


def _expansion(beta: complex) -> complex:
    r"""F at large :math:`\beta`, by the asymptotic expansion of :math:`\mathbf H_1 - Y_1`
    (A&S 12.1.31), summed to its smallest term:

    .. math::

        \mathbf H_1(\beta) - Y_1(\beta) \sim \frac{1}{\pi}\sum_q b_q, \qquad b_0 = 2, \quad
        b_{q+1} = b_q\,\frac{1 - 4q^2}{\beta^2}"""
    term = total = 2 + 0j
    k = 0
    while True:
        following = term * (1 - 4 * k * k) / (beta * beta)
        if abs(following) >= abs(term) or abs(following) <= 1e-17 * abs(total):
            return total / (2 * beta) - 1 / (beta * beta)
        term = following
        total += term
        k += 1


def _hankel2(z: complex) -> complex:
    r"""Evaluate :math:`H_1^{(2)}(z)` for |z| >= 40 in the fourth quadrant (DLMF 10.17.6)."""
    term = total = 1 + 0j
    k = 0
    while True:
        k += 1
        following = term * (4 - (2 * k - 1) ** 2) / (8j * k * z)
        if abs(following) >= abs(term) or abs(following) <= 1e-17 * abs(total):
            # Keep the fixed phase separate to avoid losing it when |Re z| is large.
            phase = cmath.exp(-1j * z) * cmath.exp(3j * math.pi / 4)
            return cmath.sqrt(2 / (math.pi * z)) * phase * total
        term = following
        total += term


class _Exact:
    """A complex number of decimal parts, in the precision of the context it is made in."""

    __slots__ = ("im", "re")

    def __init__(self, re: Decimal, im: Decimal) -> None:
        self.re, self.im = re, im

    def __add__(self, other: Self) -> Self:
        return type(self)(self.re + other.re, self.im + other.im)

    def __sub__(self, other: Self) -> Self:
        return type(self)(self.re - other.re, self.im - other.im)

    def __neg__(self) -> Self:
        return type(self)(-self.re, -self.im)

    def __mul__(self, other: "Self | int | Fraction") -> Self:
        if isinstance(other, _Exact):
            re = self.re * other.re - self.im * other.im
            return type(self)(re, self.re * other.im + self.im * other.re)
        scale = Decimal(other.numerator) / Decimal(other.denominator)
        return type(self)(self.re * scale, self.im * scale)

    def __truediv__(self, other: "Self | int") -> Self:
        if isinstance(other, _Exact):
            size = other.re * other.re + other.im * other.im
            re = (self.re * other.re + self.im * other.im) / size
            return type(self)(re, (self.im * other.re - self.re * other.im) / size)
        return type(self)(self.re / other, self.im / other)

    def __abs__(self) -> float:
        return math.hypot(float(self.re), float(self.im))


def _log(z: _Exact) -> _Exact:
    """The principal logarithm, in the context's precision."""
    size = (z.re * z.re + z.im * z.im).ln() / 2
    if z.re > 0:
        return _Exact(size, _atan(z.im / z.re))
    turn = _pi() if z.im >= 0 else -_pi()
    if z.re < 0:
        return _Exact(size, _atan(z.im / z.re) + turn)
    return _Exact(size, turn / 2)


def _atan(x: Decimal) -> Decimal:
    r"""The arctangent, in the context's precision: halved by
    :math:`\arctan v = 2\arctan\frac{v}{1 + \sqrt{1 + v^2}}` until small, then by its series."""
    halvings = 0
    while abs(x) > Decimal("0.1"):
        x = x / (1 + (1 + x * x).sqrt())
        halvings += 1
    total, power, square, k = x, x, x * x, 0
    while True:
        k += 1
        power = -power * square
        step = power / (2 * k + 1)
        if abs(step) <= abs(total).scaleb(-getcontext().prec):
            return total * (1 << halvings)
        total += step


def _pi() -> Decimal:
    """Pi, in the context's precision."""
    return _pi_to(getcontext().prec)


@cache
def _pi_to(digits: int) -> Decimal:
    """Pi to ``digits``: four times the arctangent of one."""
    with localcontext() as context:
        context.prec = digits
        return 4 * _atan(Decimal(1))


@cache
def _euler(digits: int) -> Decimal:
    r"""Euler's constant :math:`\gamma` to ``digits``, by Brent and McMillan's algorithm B1:
    with :math:`U_0 = -\ln N`, :math:`V_0 = 1`,

    .. math::

        V_q = V_{q-1}\frac{N^2}{q^2}, \qquad U_q = \frac{1}{q}\left(\frac{U_{q-1}N^2}{q}
        + V_q\right), \qquad \gamma = \frac{\sum U_q}{\sum V_q} + O(e^{-4N})"""
    with localcontext() as context:
        context.prec = digits + 10
        size = math.ceil((digits + 10) * math.log(10) / 4) + 1
        square = Decimal(size * size)
        u: Decimal = -Decimal(size).ln()
        v = Decimal(1)
        us, vs, q = u, v, 0
        while True:
            q += 1
            v = v * square / (q * q)
            u = (u * square / q + v) / q
            us, vs = us + u, vs + v
            if q > size and v < vs.scaleb(-(digits + 10)):
                return us / vs
