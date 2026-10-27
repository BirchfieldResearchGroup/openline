r"""Adaptive Gauss-Legendre integration and symmetric span averages."""

import math
from collections.abc import Callable
from functools import cache

__all__ = ["integral", "legendre", "mean", "panel"]

ORDER = 16  # Gauss-Legendre points to a panel
TOLERANCE = 1e-13  # of a panel's largest value, by which its two estimates agree


def mean(term: Callable[[float], list[complex]]) -> list[complex]:
    r"""The mean of each of ``term``'s values along a level span, a fraction :math:`u` of its
    length from one end: as its wires hang symmetrically about the middle, twice the integral
    over the first half,

    .. math::  \bar f = \int_0^1 f(u)\,du = 2\int_0^{1/2} f(u)\,du"""
    return [2 * value for value in integral(term, 0.0, 0.5)]


def integral(
    term: Callable[[float], list[complex]], a: float, b: float, floor: float = 0.0
) -> list[complex]:
    """Integrate each component of ``term`` from ``a`` to ``b``.

    Subdivide panels until estimates agree within the relative tolerance or absolute ``floor``."""
    return _refined(term, a, b, panel(term, a, b), floor)


def _refined(
    term: Callable[[float], list[complex]], a: float, b: float, whole: list[complex], floor: float
) -> list[complex]:
    middle = (a + b) / 2
    left, right = panel(term, a, middle), panel(term, middle, b)
    halves = [x + y for x, y in zip(left, right, strict=True)]
    error = max((abs(h - w) for h, w in zip(halves, whole, strict=True)), default=0.0)
    largest = max((abs(h) for h in halves), default=0.0)
    if error <= max(TOLERANCE * largest, floor) or b - a < 1e-12:
        return halves
    first = _refined(term, a, middle, left, floor)
    second = _refined(term, middle, b, right, floor)
    return [x + y for x, y in zip(first, second, strict=True)]


@cache
def legendre(n: int) -> tuple[tuple[float, float], ...]:
    """Find Gauss-Legendre nodes and weights on [-1, 1] using Newton iteration."""
    found = []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p, before = 1.0, 0.0
            for k in range(1, n + 1):
                p, before = ((2 * k - 1) * x * p - (k - 1) * before) / k, p
            slope = n * (x * p - before) / (x * x - 1)
            step = p / slope
            x -= step
            if abs(step) <= 1e-15:
                break
        found.append((x, 2 / ((1 - x * x) * slope * slope)))
    return tuple(found)


def panel(term: Callable[[float], list[complex]], a: float, b: float) -> list[complex]:
    """Integrate each component of ``term`` over one panel using ``ORDER`` quadrature points."""
    half, middle = (b - a) / 2, (a + b) / 2
    found: list[complex] = []
    for x, w in legendre(ORDER):
        values = term(middle + half * x)
        if not found:
            found = [0j] * len(values)
        found = [f + half * w * v for f, v in zip(found, values, strict=True)]
    return found
