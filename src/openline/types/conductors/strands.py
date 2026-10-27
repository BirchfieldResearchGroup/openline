"""Wire groups and their arrangement in central wires, rings, bands, and helices."""

import math
from abc import ABC
from collections.abc import Sequence
from enum import Enum, auto
from itertools import pairwise

from .. import Missing, Record
from ..materials import Material, Metal
from ..units import Area, Length, m, m2

__all__ = [
    "Band",
    "Center",
    "Hand",
    "Helical",
    "HelicalBand",
    "Helix",
    "LayRatio",
    "Layer",
    "Ring",
    "Round",
    "Strand",
    "Trapezoidal",
    "layout",
]


class Strand[M: Material](Record, ABC, kw_only=False):
    """A group of identical wires, given in order: ``Round(SteelGA2, 7, inch(0.136))``. It
    prints as ``7 round wires of 3.454 mm, SteelGA2``."""

    material: type[M]
    """What the wires are made of."""
    count: int
    """Number of wires."""
    diameter: Length
    """Wire diameter."""

    @property
    def area(self) -> Area:
        """The wires' cross-section together."""
        return m2(self.count * math.pi / 4 * self.diameter.si**2)

    def __str__(self) -> str:
        shape = type(self).__name__.lower()
        return f"{self.count} {shape} wires of {self.diameter}, {self.material}"


class Round[M: Material](Strand[M]):
    """Round wires."""


class Trapezoidal[M: Material](Strand[M]):
    """Trapezoidal wires; ``diameter`` is that of a round wire of equal area, their equivalent
    diameter (IEC 62219, 3.5)."""

    layers: int | None = None
    """How many layers they make about what lies within, not counting a central wire (IEC 62219,
    table 2, note b): 2; none where no document at hand gives it."""
    outside_diameter: Length | None = None
    """The diameter across their outermost layer, as their standard's tables print it (ASTM B778,
    tables 1 and 2); none where no document at hand gives it."""


class Hand(Enum):
    """Helix handedness along the conductor axis."""

    RIGHT = auto()
    """Right-hand: as the middle stroke of a Z."""
    LEFT = auto()
    """Left-hand: as the middle stroke of an S."""

    @property
    def opposite(self) -> "Hand":
        """The other hand, the next ring in's."""
        return Hand.LEFT if self is Hand.RIGHT else Hand.RIGHT


class LayRatio(Record, kw_only=False):
    """Permitted lay length divided by layer outside diameter.

    For ASTM B232's outer layer in 26/7 construction: ``LayRatio(10, 13)``; for ASTM B231's
    class AA layers: ``LayRatio(10, 16, 13.5)``."""

    least: float
    """The shortest lay, over the ring's outside diameter."""
    most: float
    """The longest lay, over the ring's outside diameter."""
    preferred: float | None = None
    """The lay its standard prefers, over the ring's outside diameter; none where it prefers
    none."""

    def __str__(self) -> str:
        """``10 to 16, 13.5 preferred``."""
        given = f"{self.least:g} to {self.most:g}"
        return given if self.preferred is None else f"{given}, {self.preferred:g} preferred"


class Layer[W: Strand[Metal]](Record, ABC):
    """Wires laid together about a conductor's axis, each of a strand, in order around it."""

    wires: tuple[W, ...]
    """Each wire's strand, in order around the layer."""

    @property
    def outer_radius(self) -> Length:
        """The radius its wires lie within."""
        raise NotImplementedError


class Center(Layer[Strand[Metal]]):
    """The straight wire on the axis: a round one, or the round wire trapezoidal ones lie about
    (ASTM B778, note 1)."""

    @property
    def outer_radius(self) -> Length:
        return self.wires[0].diameter / 2


class Ring(Layer[Round[Metal]]):
    """Round wires about the axis, their centers on a circle."""

    radius: Length
    """The radius of the circle through the wires' centers."""

    @property
    def outer_radius(self) -> Length:
        return self.radius + self.wires[0].diameter / 2

    def factor_at(self, lay: Length) -> float:
        """Its wires' stranding factor at ``lay``: their lay angle's secant at its radius."""
        return math.hypot(1, 2 * math.pi * self.radius.si / lay.si)

    def laid(self, lay: Length, hand: Hand | None) -> "Helix":
        """It, its wires turning once in each ``lay``."""
        return Helix(radius=self.radius, wires=self.wires, lay=lay, hand=hand)


class Band(Layer[Trapezoidal[Metal]]):
    """Trapezoidal wires filling the annulus between two radii, each a sector of it."""

    inner: Length
    """The radius its wires lie outside."""
    outer: Length
    """The radius its wires lie within."""

    @property
    def outer_radius(self) -> Length:
        return self.outer

    @property
    def radius(self) -> Length:
        """Halfway through it: where openline places each wire's middle."""
        return (self.inner + self.outer) / 2

    @property
    def thickness(self) -> Length:
        """Across it, from its inner radius to its outer."""
        return self.outer - self.inner

    def factor_at(self, lay: Length) -> float:
        r"""Its wires' stranding factor at ``lay``: each filament's lay angle's secant, averaged
        over its area, with :math:`k = 2\pi/\lambda` and radii :math:`a < b`,

        .. math::  \frac{2\bigl[(1+k^2b^2)^{3/2} - (1+k^2a^2)^{3/2}\bigr]}{3k^2(b^2-a^2)}"""
        k2 = (2 * math.pi / lay.si) ** 2
        a2, b2 = self.inner.si**2, self.outer.si**2
        rise = math.pow(1 + k2 * b2, 1.5) - math.pow(1 + k2 * a2, 1.5)
        return 2 * rise / (3 * k2 * (b2 - a2))

    def laid(self, lay: Length, hand: Hand | None) -> "HelicalBand":
        """It, its wires turning once in each ``lay``."""
        return HelicalBand(inner=self.inner, outer=self.outer, wires=self.wires, lay=lay, hand=hand)


class Helical(Record, ABC):
    r"""Wires turning about the axis, once in each ``lay``, the way ``hand`` turns. Each is longer
    than the conductor by its stranding factor (ASTM B232, note 6), its lay angle :math:`\theta`'s
    secant:

    .. math::  \sec\theta = \sqrt{1 + \left(\frac{2\pi a}{\lambda}\right)^2}

    at a radius :math:`a`, with :math:`\lambda` its lay."""

    lay: Length
    """The length along the conductor of one turn."""
    hand: Hand | None
    """Which way it turns; none where no document at hand gives its direction of lay."""

    def factor_at(self, lay: Length) -> float:
        """Its wires' stranding factor at ``lay``."""
        raise NotImplementedError

    @property
    def factor(self) -> float:
        r"""Its stranding factor, :math:`\sec\theta`: how much longer its wires are than the
        conductor."""
        return self.factor_at(self.lay)


class Helix(Ring, Helical):
    """A ring whose wires turn about the axis."""


class HelicalBand(Band, Helical):
    """A band whose wires turn about the axis."""


def layout(strands: Sequence[Strand[Metal]]) -> tuple[Center | Ring | Band, ...]:
    """Arrange wires in layers from the center outward; input strands run outside inward.

    Round wires take the fewest rings that fit (``_rounds``). Trapezoidal wires, outside all
    others, fill their ``layers`` from what lies within out to their ``outside_diameter``
    (``_bands``). Raise ``Missing`` where round wires' count makes no rings, or trapezoidal
    wires' layers or outside diameter are not known."""
    shaped = [strand for strand in strands if isinstance(strand, Trapezoidal)]
    if shaped and shaped != [strands[0]]:
        raise ValueError("trapezoidal wires lie outside all others")
    found: list[Center | Ring | Band] = list(_rounds(strands[len(shaped) :]))
    for strand in shaped:
        found.extend(_bands(strand, found[-1].outer_radius.si if found else 0.0))
    return tuple(found)


def _rounds(strands: Sequence[Strand[Metal]]) -> tuple[Center | Ring, ...]:
    """Round wires in layers: the fewest rings that fit, with six more wires per successive
    ring. Strands of equal wire diameter share rings, with inner strands allocated first and
    mixed wires distributed around the ring."""
    rounds = [strand for strand in reversed(strands) if isinstance(strand, Round)]
    found: list[Center | Ring] = []
    if not rounds:
        return ()
    if all(strand.diameter == rounds[0].diameter for strand in rounds):
        wires = [strand for strand in rounds for _ in range(strand.count)]
        for radius, count in _rings(len(wires), rounds[0].diameter.si, 0.0):
            here, wires = wires[:count], wires[count:]
            spread = sorted(enumerate(here), key=lambda pair: (pair[0] * 0.61803398875) % 1)
            found.append(_layer(radius, tuple(wire for _, wire in spread)))
        return tuple(found)
    for strand in rounds:
        inner = found[-1].outer_radius.si if found else 0.0
        for radius, count in _rings(strand.count, strand.diameter.si, inner):
            found.append(_layer(radius, (strand,) * count))
    return tuple(found)


def _bands(strand: Trapezoidal[Metal], inner: float) -> list[Center | Band]:
    """Trapezoidal wires laid outside a radius ``inner``, in meters: a central wire first where
    nothing lies within (ASTM B778, note 1; IEC 62219, table 2, note b), then ``layers`` bands
    at one fill ratio, their wires' area over the annulus to the outside diameter (IEC 62219,
    3.7). No document gives each layer's wires (IEC 62219, table 2, note c): openline shares
    them as bands of equal thickness would hold them, in whole wires, each band's radii then
    set by the wires it holds."""
    if strand.layers is None or strand.outside_diameter is None:
        raise Missing(f"{strand}: no document at hand gives their layers and outside diameter")
    found: list[Center | Band] = []
    count, wire = strand.count, strand.area.si / strand.count
    if inner == 0:
        found.append(Center(wires=(strand,)))
        count, inner = count - 1, strand.diameter.si / 2
    outer = strand.outside_diameter.si / 2
    fill = count * wire / (math.pi * (outer**2 - inner**2))
    if not 0 < fill <= 1:
        raise ValueError(f"{strand}: {count} wires cannot fill {2 * outer} m across")
    edges = [inner + (outer - inner) * i / strand.layers for i in range(strand.layers + 1)]
    for holds in _apportion(count, [b**2 - a**2 for a, b in pairwise(edges)]):
        within = math.sqrt(inner**2 + holds * wire / (math.pi * fill))
        found.append(Band(inner=m(inner), outer=m(within), wires=(strand,) * holds))
        inner = within
    return found


def _apportion(total: int, shares: Sequence[float]) -> list[int]:
    """``total`` whole wires in proportion to ``shares``: each its share rounded down, the
    largest remainders taking what is left."""
    exact = [total * share / sum(shares) for share in shares]
    counts = [math.floor(each) for each in exact]
    for i in sorted(range(len(exact)), key=lambda i: counts[i] - exact[i])[: total - sum(counts)]:
        counts[i] += 1
    return counts


def _layer(radius: float, wires: tuple[Round[Metal], ...]) -> Center | Ring:
    """The center wire, on the axis, or a ring of wires about it."""
    return Center(wires=wires) if radius == 0 else Ring(radius=m(radius), wires=wires)


def _rings(count: int, diameter: float, inner: float) -> list[tuple[float, int]]:
    """The circles through the centers of ``count`` round wires of ``diameter``, laid outside a
    radius ``inner``, in meters, and how many wires each holds. With nothing inside, three or four
    wires lie in one ring; others make a center wire and rings of six, twelve and on."""
    radius = diameter / 2
    if inner == 0:
        if count in (3, 4):
            return [(radius / math.sin(math.pi / count), count)]
        for n in range(8):
            if count == 1 + 3 * n * (n + 1):
                return [(0.0, 1), *((i * diameter, 6 * i) for i in range(1, n + 1))]
        raise Missing(f"{count} round wires make no rings about a center wire")
    n = _counted(count, 2 * inner / diameter)
    first = (count - 3 * n * (n - 1)) // n
    found = []
    for i in range(n):
        holds = first + 6 * i
        center = max(inner + radius, radius / math.sin(math.pi / holds))
        found.append((center, holds))
        inner = center + radius
    return found


def _counted(count: int, core: float) -> int:
    """How many rings ``count`` round wires make around a core ``core`` of their diameters
    across: each ring holds six more wires than the one beneath, and the first about
    π(core + 1)."""
    first = math.pi * (core + 1)
    fits = [
        n for n in range(1, 8) if count > 3 * n * (n - 1) and (count - 3 * n * (n - 1)) % n == 0
    ]
    if not fits:
        raise ValueError(f"{count} round wires make no rings about a core")
    return min(fits, key=lambda n: abs((count - 3 * n * (n - 1)) / n - first))
