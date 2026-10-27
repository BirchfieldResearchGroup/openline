"""Bare overhead conductors, grouped by construction and standard: each its names and its wires,
nothing openline calculates.

Families specify wire materials and shapes, for example
``ACSR[Round[Aluminum1350H19], Round[CoatedSteel]]``. Standards such as ``astm.B232`` define
designations and stranding rules. Printing a conductor produces its data sheet."""

from collections.abc import Mapping
from dataclasses import fields
from functools import cached_property
from typing import ClassVar

from .. import Design, Record
from ..materials import (
    AluminumAlloy,
    AluminumCladSteel,
    AnnealedAluminum,
    CopperCladSteel,
    HardDrawnAluminum,
    Metal,
    Steel,
)
from ..units import Area, Length, Stress, m2
from .designations import Designation
from .strands import Band, Hand, Layer, LayRatio, Ring, Strand, layout

__all__ = [
    "AAAC",
    "AAC",
    "AACSR",
    "ACAR",
    "ACS",
    "ACSR",
    "ACSS",
    "ASTM",
    "BS",
    "CCS",
    "CSA",
    "IEC",
    "Conductor",
    "Homogeneous",
    "Reinforced",
    "SteelCored",
    "Stranding",
    "Surface",
]


class Surface(Record):
    """Conductor surface properties used in heat-balance calculations.

    Values describe the surface condition or coating assumed for the study.
    """

    emissivity: float
    """Thermal emissivity, from 0 to 1."""
    absorptivity: float
    """Solar absorptivity, from 0 to 1."""


class Stranding(Record, kw_only=False):
    """Lay-ratio ranges from outside in, the increment the lay gives its wires where the
    standard fixes the lay by it, and the share of their strength the conductor is rated at.

    For ASTM B232 aluminum in 26/7 construction:
    ``Stranding((LayRatio(10, 13), LayRatio(10, 16)), 0.025, 0.93)``."""

    lay_ratios: tuple[LayRatio, ...]
    """The range of the lay over the outside diameter of each ring its wires lie in, from the
    outside in, a ring of two strands each one's; none for a wire on the axis, or where the
    standard fixes no lay."""
    increment: float | None = None
    """The target by which to infer lay: 0.025 lengthens its wires by 2.5%. None where
    preferences give the lay, or only bounds are known. Approximate mass/resistance increments
    need not equal the increment of preferred lays (ASTM B856, 11.1)."""
    rating_factor: float | None = None
    """The share of its wires' strength the conductor is rated at: 0.93 is 93%; none where the
    standard rates it otherwise."""


class Conductor(Design):
    """A bare conductor identified by standard, designation, wire counts, and diameters."""

    standard: ClassVar[str]
    """The standard it is made to: ASTM B232. Only a standard's class gives one."""
    family: ClassVar[str]
    """Its family, as documents abbreviate it: ACSR. Only a family's class gives one."""
    strandings: ClassVar[Mapping[tuple[int, ...], tuple[Stranding, ...]]] = {}
    """What its standard gives for each stranding, a strand at a time from the outside in, by the
    count of each strand, ``(26, 7)``; none where openline does not have the standard."""
    hand: ClassVar[Hand | None] = None
    """Which way its outer ring turns; each ring within turns the other way. Only a standard's
    class gives one; none where no document at hand gives its direction of lay."""
    grades: ClassVar[tuple[type[Steel], ...]] = ()
    """The grades of core wire its standard names, where its design leaves the grade open: ASTM
    B232's GA2 to MA5. A rating takes one of them (``mechanical.strength``)."""

    code_words: tuple[str, ...]
    """The names its documents give it, ``("Drake",)``; none for most IEC sizes."""
    designation: Designation
    """How its standard names it."""

    @property
    def parts(self) -> tuple[tuple[str, Strand[Metal]], ...]:
        """Its groups of wires by the name its type gives each, from the outside in:
        ``(("outer", ...), ("core", ...))``."""
        return tuple(
            (field.name, strand)
            for field in fields(self)
            if isinstance(strand := getattr(self, field.name), Strand)
        )

    @property
    def strands(self) -> tuple[Strand[Metal], ...]:
        """Its groups of wires, from the outside in."""
        return tuple(strand for _, strand in self.parts)

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """What its standard gives for its stranding, a strand at a time from the outside in;
        none where the standard fixes no lay for it, or openline does not have the standard."""
        return self.strandings.get(tuple(strand.count for strand in self.strands))

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """The stress its standard rates a wire of ``metal`` and ``diameter`` at, from the
        metric table of the wire's standard where the conductor is sized in SI units: the
        wire's tensile strength (ASTM B231, 9; ASTM B399, 9.3), unless its standard rates it
        otherwise."""
        return metal.tensile_strength.at(diameter, metric)

    @cached_property
    def layers(self) -> tuple[Layer[Strand[Metal]], ...]:
        r"""Its wires about its axis, from the center out (``strands.layout``), found once: its
        rings and bands laid where its standard gives lay ratios. A ring of a preferred lay ratio
        :math:`\ell^\ast` lies at it; the remaining rings lie at the one fraction
        :math:`\tau_s` of their lay ratios' ranges that gives the strand's increment
        :math:`\eta_s` (ASTM B232, note 6). Without an increment, those rings use their
        ranges' midpoints, a model assumption rather than a standard preference:

        .. math::

            1 + \eta_s = \frac{1}{|s|}\sum_{i \in s} \sec\theta_i, \qquad
            \lambda = 2\bigl(\ell^- + \tau_s(\ell^+ - \ell^-)\bigr)(a + r)

        with :math:`|s|` the strand's wires, :math:`\sec\theta_i` each one's stranding factor (one
        for the center wire), :math:`\ell^-` and :math:`\ell^+` a ring's least and most lay
        ratios, and :math:`2(a + r)` its outside diameter, :math:`a` its radius and :math:`r` its
        wires'; a band's, its outer one. The outer layer turns the standard's ``hand``, each
        within it the other way."""
        found = layout(self.strands)
        given = self.stranding
        if given is None:
            return found
        rings = [layer for layer in reversed(found) if isinstance(layer, Ring | Band)]
        turns = (self.hand, self.hand.opposite) if self.hand is not None else (None, None)
        hands = {ring: turns[i % 2] for i, ring in enumerate(rings)}
        lays: dict[Ring | Band, Length] = {}
        for strand, stranding in zip(self.strands, given, strict=True):
            if not stranding.lay_ratios:
                continue
            own = {
                ring: ratio
                for ring, ratio in zip(
                    (ring for ring in rings if strand in ring.wires),
                    stranding.lay_ratios,
                    strict=True,
                )
            }
            for ring, lay in _lays(strand, stranding, own).items():
                if lays.setdefault(ring, lay) != lay:
                    raise ValueError(f"{self.title}: two strands give one ring two lays")
        return tuple(
            layer.laid(lays[layer], hands[layer])
            if isinstance(layer, Ring | Band) and layer in lays
            else layer
            for layer in found
        )

    @property
    def names(self) -> tuple[str, ...]:
        return self.code_words

    @property
    def title(self) -> str:
        """Display name with designation, stranding, and standard."""
        counts = "/".join(str(strand.count) for strand in self.strands)
        named = filter(None, ("/".join(self.code_words), str(self.designation), counts))
        return f"{', '.join(named)} ({self.standard})"

    @property
    def order(self) -> float:
        """Cross-sectional area, used to sort conductors from smallest to largest."""
        return self.area.si

    @property
    def wire_counts(self) -> tuple[int, ...]:
        """Wire counts of each strand group, from outer wires to core: ``(26, 7)``."""
        return tuple(strand.count for strand in self.strands)

    @property
    def area(self) -> Area:
        """Total cross-section of its wires."""
        return sum((strand.area for strand in self.strands), m2(0))

    @property
    def diameter(self) -> Length:
        """Outside diameter, across its outer layer (``layers``): its round wires' outer ring, or
        its trapezoidal wires' outside diameter."""
        return 2 * self.layers[-1].outer_radius


def _lays(
    strand: Strand[Metal], stranding: Stranding, ratios: Mapping[Ring | Band, LayRatio]
) -> dict[Ring | Band, Length]:
    """Keep preferred lays; infer the remaining lays from an increment, or use range midpoints
    as a model assumption when no increment is given."""
    preferred = {
        ring: 2 * ring.outer_radius * ratio.preferred
        for ring, ratio in ratios.items()
        if ratio.preferred is not None
    }
    if len(preferred) == len(ratios):
        return preferred
    fraction = (
        0.5 if stranding.increment is None else _fraction(strand, stranding.increment, ratios)
    )
    return {ring: _lay(ring, ratio, fraction) for ring, ratio in ratios.items()}


def _lay(ring: Ring | Band, ratio: LayRatio, fraction: float) -> Length:
    """A ring's preferred lay, or a fraction of its ratio's range, over its outside diameter."""
    chosen = ratio.preferred
    if chosen is None:
        chosen = ratio.least + fraction * (ratio.most - ratio.least)
    return 2 * ring.outer_radius * chosen


def _fraction(
    strand: Strand[Metal], increment: float, ratios: Mapping[Ring | Band, LayRatio]
) -> float:
    """The fraction of its rings' lay ratios at which a strand's wires average its increment, by
    bisection to within 1e-12."""
    rings = list(ratios)
    if not rings:
        return 0.0

    def mean(fraction: float) -> float:
        laid = sum(
            ring.wires.count(strand) * ring.factor_at(_lay(ring, ratios[ring], fraction))
            for ring in rings
        )
        straight = strand.count - sum(ring.wires.count(strand) for ring in rings)
        return (laid + straight) / strand.count

    low, high = 0.0, 1.0
    if not mean(high) <= 1 + increment <= mean(low):
        raise ValueError(f"no lay in its ratios' ranges lengthens {strand} by {increment:.2%}")
    while high - low > 1e-12:
        middle = (low + high) / 2
        low, high = (middle, high) if mean(middle) > 1 + increment else (low, middle)
    return (low + high) / 2


class Homogeneous[W: Strand[Metal]](Conductor):
    """Wires of one metal."""

    wires: W
    """The wires."""


class Reinforced[O: Strand[Metal], C: Strand[Metal]](Conductor):
    """Outer wires around a core of another material."""

    outer: O
    """Wires around the core."""
    core: C
    """Wires of the core."""


class AAC[W: Strand[HardDrawnAluminum]](Homogeneous[W]):
    """All aluminum."""

    family = "AAC"


class AAAC[W: Strand[AluminumAlloy]](Homogeneous[W]):
    """All aluminum alloy."""

    family = "AAAC"


class ACS[W: Strand[AluminumCladSteel]](Homogeneous[W]):
    """All aluminum-clad steel."""

    family = "ACS"


class CCS[W: Strand[CopperCladSteel]](Homogeneous[W]):
    """All copper-clad steel."""

    family = "CCS"


class SteelCored[O: Strand[Metal], C: Strand[Steel]](Reinforced[O, C]):
    """Wires around a steel core."""

    @property
    def core_diameter(self) -> Length:
        """Diameter of the steel core, across its outer layer."""
        return 2 * layout((self.core,))[-1].outer_radius

    @property
    def core_radius(self) -> Length:
        """Radius of the steel core."""
        return self.core_diameter / 2


class ACSR[O: Strand[HardDrawnAluminum], C: Strand[Steel]](SteelCored[O, C]):
    """Aluminum conductor, steel reinforced."""

    family = "ACSR"


class AACSR[O: Strand[AluminumAlloy], C: Strand[Steel]](SteelCored[O, C]):
    """Aluminum alloy conductor, steel reinforced."""

    family = "AACSR"


class ACSS[O: Strand[AnnealedAluminum], C: Strand[Steel]](SteelCored[O, C]):
    """Aluminum conductor, steel supported: annealed aluminum, the steel bearing the load."""

    family = "ACSS"


class ACAR[O: Strand[HardDrawnAluminum], C: Strand[AluminumAlloy]](Reinforced[O, C]):
    """Aluminum conductor, alloy reinforced."""

    family = "ACAR"


class ASTM[D: Designation](Conductor):
    """Made to an ASTM standard, designated as ``D``."""

    designation: D
    """How the standard names it."""


class CSA[D: Designation](Conductor):
    """Made to a CSA standard, designated as ``D``."""

    designation: D
    """How the standard names it."""


class BS[D: Designation](Conductor):
    """Made to a British standard, designated as ``D``."""

    designation: D
    """How the standard names it."""


class IEC[D: Designation](Conductor):
    """Made to an IEC standard, designated as ``D``."""

    designation: D
    """How the standard names it."""
