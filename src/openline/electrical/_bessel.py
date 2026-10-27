r"""The modified Bessel functions :math:`I_0` and :math:`I_1` of complex argument, scaled by
:math:`e^{-\zeta}` so that neither overflows: by their series where the argument is small, and by
their asymptotic expansion where it is large."""

import cmath
import math

__all__ = ["i"]

LARGE = 40.0  # from this |zeta| on, the asymptotic expansion is the more precise: the series loses
PRECISION = 1e-17  # a term of e**-2zeta


def i(order: int, zeta: complex) -> complex:
    r"""The modified Bessel function of order 0 or 1, scaled: :math:`I_\nu(\zeta)\,e^{-\zeta}`."""
    if abs(zeta) >= LARGE:
        return _expansion(order, zeta) / cmath.sqrt(2 * math.pi * zeta)
    return _series(order, zeta) * cmath.exp(-zeta)


def _series(order: int, zeta: complex) -> complex:
    r""":math:`I_\nu(\zeta) = \sum_q \frac{(\zeta/2)^{2q+\nu}}{q!\,(q+\nu)!}`, to the precision of
    its terms."""
    quarter = zeta * zeta / 4
    term = (zeta / 2) ** order
    total, q = term, 0
    while True:
        q += 1
        term *= quarter / (q * (q + order))
        total += term
        if abs(term) <= PRECISION * abs(total):
            return total


def _expansion(order: int, zeta: complex) -> complex:
    r"""The asymptotic series of :math:`I_\nu` at large :math:`\zeta`, summed to its smallest term:
    :math:`1 - \frac{4\nu^2 - 1}{8\zeta} + \frac{(4\nu^2 - 1)(4\nu^2 - 9)}{2!\,(8\zeta)^2} -
    \cdots`."""
    four = 4 * order * order
    term = total = 1 + 0j
    q = 0
    while True:
        q += 1
        following = -term * (four - (2 * q - 1) ** 2) / (8 * q * zeta)
        if abs(following) >= abs(term) or abs(following) <= PRECISION * abs(total):
            return total
        term = following
        total += term
