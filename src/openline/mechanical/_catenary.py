r"""Sag and tension in a level span, accounting for conductor weight, stiffness, and expansion."""

import math
from functools import lru_cache

from ..types.conductors import Conductor
from ..types.lines import Strung
from ..types.units import Force, Length, Temperature, celsius, m, n
from ._properties import stiffness, weight

__all__ = ["sag", "tension"]


def tension(
    conductor: Conductor, *, span: Length, strung: Strung, temperature: Temperature
) -> Force:
    r"""Return horizontal tension :math:`H` at ``temperature`` for a level span :math:`S`.

    With weight per unit length :math:`w` and catenary constant :math:`c = H/w`, the conductor
    has length :math:`L` and mean tension :math:`\bar N`:

    .. math::  L = 2c\sinh\frac{S}{2c}, \qquad
               \bar N = H\,\frac{S + c\sinh(S/c)}{2L}

    Each strand has stiffness :math:`k_s` and expansion coefficient :math:`\alpha_s`
    (``mechanical.stiffness``). Strands carry tension only:

    .. math::  \bar N = \sum_s k_s \max(\varepsilon_s, 0), \qquad
               \varepsilon_s = \frac{L}{L_0\,[1 + \alpha_s(T - T_0)]} - 1

    :math:`L_0` is the unstressed length at stringing temperature :math:`T_0`. Strands have
    equal strain at the supplied stringing condition. If the aluminum goes slack, the core
    carries the load. Creep and permanent set are included in the supplied stringing tension;
    they are not modeled separately."""
    return n(_tension(conductor, span, strung, temperature))


def sag(
    conductor: Conductor,
    *,
    span: Length,
    strung: Strung,
    temperature: Temperature,
    at: float = 0.5,
) -> Length:
    r"""Return the vertical drop below the supports at fraction ``at`` of a level span:

    .. math::  y(u) = c\left[\cosh\frac{S}{2c} - \cosh\frac{(u - \tfrac12)S}{c}\right]

    :math:`u` is ``at`` (default 0.5, midspan), :math:`S` is span length, and :math:`c = H/w`
    uses the horizontal tension from ``tension`` and weight per unit length."""
    c = _tension(conductor, span, strung, temperature) / weight(conductor).si
    offset = (at - 0.5) * span.si
    drop = c * (math.cosh(span.si / (2 * c)) - math.cosh(offset / c))
    return m(drop)


@lru_cache(maxsize=4096)
def _tension(conductor: Conductor, span: Length, strung: Strung, temperature: Temperature) -> float:
    """Solve tension in newtons by bisection with relative tolerance 1e-12."""
    w, s = weight(conductor).si, span.si
    parts = [
        (k.si, strand.material.expansion.si)
        for k, strand in zip(stiffness(conductor), conductor.strands, strict=True)
    ]
    held = strung.tension.si
    stretched = sum(k for k, _ in parts)
    unstressed = _length(held, w, s) / (1 + _mean(held, w, s) / stretched)
    rise = temperature.to(celsius) - strung.temperature.to(celsius)

    def excess(h: float) -> float:
        length = _length(h, w, s)
        pulled = sum(k * max(length / (unstressed * (1 + a * rise)) - 1, 0) for k, a in parts)
        return pulled - _mean(h, w, s)

    low, high = w * s / 50, w * s * 100
    while excess(high) > 0:
        high *= 2
    while (high - low) > 1e-12 * high:
        middle = (low + high) / 2
        low, high = (middle, high) if excess(middle) > 0 else (low, middle)
    return (low + high) / 2


def _length(h: float, w: float, s: float) -> float:
    """The catenary's length, in meters, at a horizontal tension ``h``."""
    c = h / w
    return 2 * c * math.sinh(s / (2 * c))


def _mean(h: float, w: float, s: float) -> float:
    """Return tension averaged over catenary length, in newtons."""
    c = h / w
    return h * (s + c * math.sinh(s / c)) / (2 * _length(h, w, s))
