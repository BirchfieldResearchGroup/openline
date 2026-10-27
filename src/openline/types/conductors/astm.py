"""ASTM conductor standards, with separate A460 classes for wire conductivity grades."""

from types import MappingProxyType

from ..materials import (
    Aluminum1350H19,
    Aluminum1350O,
    Aluminum6201T81,
    AluminumCladSteel,
    AluminumCladSteelAW2,
    AluminumCladSteelAW3,
    CoatedSteel,
    CopperCladSteel,
    CopperCladSteel30EHS,
    CopperCladSteel30HS,
    CopperCladSteel40HS,
    Metal,
    Steel,
    SteelGA2,
    SteelGA3,
    SteelGA4,
    SteelGA5,
    SteelGC2,
    SteelMA2,
    SteelMA3,
    SteelMA4,
    SteelMA5,
)
from ..units import Length, Stress, inch
from . import AAAC, AAC, ACAR, ACS, ACSR, ACSS, ASTM, CCS, Stranding
from .designations import Gauge, Kcmil, Mm2, WireGauge
from .strands import Hand, LayRatio, Round, Trapezoidal

__all__ = [
    "A460",
    "A460_30EHS",
    "A460_30HS",
    "A460_40HS",
    "B231",
    "B232",
    "B399",
    "B416",
    "B524",
    "B549",
    "B778",
    "B779",
    "B779_AW",
    "B856",
    "B856_AW",
    "B857",
    "B857_AW",
]


# ASTM B231-16 (2021) and B399-04 (2021), 7.1, each class AA layer; ASTM B524-99, 6.1,
# B416-98 (2018), 6.2, and B228-04, 6.2, each layer: 13.5 preferred.
_AA = LayRatio(10, 16, 13.5)
# ASTM B232-17, table 5: each aluminum ring's lay ratios, from the outside in, by how many rings.
_FOUR = (LayRatio(10, 13), LayRatio(10, 16), LayRatio(10, 17), LayRatio(10, 17))
_THREE = _FOUR[:3]
_TWO = _FOUR[:2]
_ONE = (LayRatio(10, 14.5),)
# ASTM B500/B500M-24, 7.1 and 7.2: a stranded steel core's 6-wire layer, and its 12-wire one.
_CORE_7 = (LayRatio(16, 26),)
_CORE_19 = (LayRatio(14, 22), LayRatio(16, 26))
# ASTM B856-03, table 2: ACSS layers from outside in. The third and fourth aluminum
# layers have limits only; openline uses their midpoints, not a standard preference.
_ACSS_ONE = (LayRatio(10, 14.5, 12.5),)
_ACSS_TWO = (LayRatio(10, 13, 11), LayRatio(10, 16, 13))
_ACSS_THREE = (*_ACSS_TWO, LayRatio(10, 17))
_ACSS_FOUR = (*_ACSS_THREE, LayRatio(10, 17))
_ACSS_CORE_7 = (LayRatio(18, 30, 25),)
_ACSS_CORE_19 = (LayRatio(16, 24, 20), *_ACSS_CORE_7)


# ASTM B231-16 (2021) and B399-04 (2021), 7.2: a class A layer's lay ratio, 8 to 16.
_CLASS_A = LayRatio(8, 16)


# Educated guess: ACSR strandings neither B232's table 6 nor
# B549's tables give, laid and rated as the rows of as many aluminum layers and core wires.
_OFF_TABLE: dict[tuple[int, ...], tuple[Stranding, ...]] = {
    (5, 1): (Stranding(_ONE, 0.015, 0.96), Stranding((), 0.0, 0.96)),
    # Few wires about a 7-wire core reach no 2.5% within 10 to 14.5: the range's middle.
    (6, 7): (Stranding(_ONE, None, 0.96), Stranding(_CORE_7, 0.004, 0.96)),
    (8, 7): (Stranding(_ONE, None, 0.96), Stranding(_CORE_7, 0.004, 0.96)),
    (18, 19): (Stranding(_ONE, 0.025, 0.96), Stranding(_CORE_19, 0.006, 0.93)),
    (20, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
    (22, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
    (68, 7): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_7, 0.004, 0.96)),
}


def _class_lay(
    given: tuple[Stranding, ...] | None, classes: tuple[str, ...]
) -> tuple[Stranding, ...] | None:
    """Class AA's preferred lay; class A's, 7.2's range for every layer, at its middle. Educated
    guess: 7.2 prefers no ratio, and for 37 wires or more bounds
    only the two outer layers."""
    if given is None or "AA" in classes:
        return given
    return tuple(
        Stranding((_CLASS_A,) * len(each.lay_ratios), rating_factor=each.rating_factor)
        for each in given
    )


class A460[M: CopperCladSteel](ASTM[Gauge | WireGauge], CCS[Round[M]]):
    """Copper-clad steel strand, laid and rated as ASTM B228 lays and rates copper-clad steel
    conductors, as Southwire's strengths follow.

    Its strandings: ASTM B228-04, 6.1 and 6.2, the lay ratios, and table 1, footnote B, the
    rating factors; its hand, 6.3."""

    standard = "ASTM A460"
    hand = Hand.LEFT
    strandings = MappingProxyType(
        {
            (3,): (Stranding((LayRatio(14, 20, 16.5),), rating_factor=0.95),),
            (7,): (Stranding((_AA,), rating_factor=0.90),),
            (19,): (Stranding((_AA,) * 2, rating_factor=0.90),),
        }
    )

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """ASTM B228-11a (2021), table 1, footnote B: each wire at its tensile strength over the
        least area its diameter may vary to, ASTM B227-70, 6.2: 1.5% from 0.2043 in to 0.1000 in,
        0.0015 in below."""
        least = diameter * 0.985 if diameter > inch(0.1000) else diameter - inch(0.0015)
        return metal.tensile_strength.at(diameter, metric) * (least / diameter) ** 2


class A460_30HS(A460[CopperCladSteel30HS]):
    """Wires of 30% conductivity, high strength."""

    standard = "ASTM A460, 30HS"


class A460_30EHS(A460[CopperCladSteel30EHS]):
    """Wires of 30% conductivity, extra high strength."""

    standard = "ASTM A460, 30EHS"


class A460_40HS(A460[CopperCladSteel40HS]):
    """Wires of 40% conductivity, high strength."""

    standard = "ASTM A460, 40HS"


class B231(ASTM[Kcmil | Gauge | Mm2], AAC[Round[Aluminum1350H19]]):
    """Aluminum 1350, round wires, of class AA, A or both.

    Its strandings: ASTM B231-16 (2021), table 6, the rating factors, and 7.1, the lay ratios of
    a class AA conductor's layers; its hand, 7.4. A class A conductor's lay, 7.2, prefers no
    ratio: openline lays only class AA."""

    standard = "ASTM B231"
    hand = Hand.RIGHT
    strandings = MappingProxyType(
        {
            (7,): (Stranding((_AA,), rating_factor=0.96),),
            (19,): (Stranding((_AA,) * 2, rating_factor=0.93),),
            (37,): (Stranding((_AA,) * 3, rating_factor=0.91),),
            (61,): (Stranding((_AA,) * 4, rating_factor=0.90),),
            (91,): (Stranding((_AA,) * 5, rating_factor=0.89),),
            (127,): (Stranding((_AA,) * 6, rating_factor=0.89),),
        }
    )

    classes: tuple[str, ...]
    """Its classes, as its listings print them, in alphabetical order: ``("A", "AA")``."""

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """Class AA's; a class A conductor's rating factors alone, as 7.2 fixes it no lay."""
        return _class_lay(super().stranding, self.classes)


class B232(
    ASTM[Kcmil | Gauge | Mm2],
    ACSR[Round[Aluminum1350H19], Round[CoatedSteel]],
):
    """ACSR, aluminum 1350 around a coated-steel core.

    Its strandings: ASTM B232-17, table 6; the lay ratios of its aluminum rings, table 5, its
    class AA rows; its hand, 8.3; its grades of core, 1.2."""

    standard = "ASTM B232"
    hand = Hand.RIGHT
    grades = (
        SteelGA2,
        SteelMA2,
        SteelGC2,
        SteelGA3,
        SteelMA3,
        SteelGA4,
        SteelMA4,
        SteelGA5,
        SteelMA5,
    )
    strandings = MappingProxyType(
        {
            (6, 1): (Stranding(_ONE, 0.015, 0.96), Stranding((), 0.0, 0.96)),
            (7, 1): (Stranding(_ONE, 0.015, 0.96), Stranding((), 0.0, 0.96)),
            (8, 1): (Stranding(_ONE, 0.020, 0.96), Stranding((), 0.0, 0.96)),
            (18, 1): (Stranding(_TWO, 0.020, 0.93), Stranding((), 0.0, 0.96)),
            (36, 1): (Stranding(_THREE, 0.020, 0.91), Stranding((), 0.0, 0.96)),
            (12, 7): (Stranding(_ONE, 0.025, 0.96), Stranding(_CORE_7, 0.004, 0.96)),
            (24, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (26, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (30, 7): (Stranding(_TWO, 0.0275, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (42, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),  # estimate
            (45, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (48, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),  # estimate
            (54, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (72, 7): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_7, 0.004, 0.96)),
            (16, 19): (Stranding(_ONE, 0.025, 0.96), Stranding(_CORE_19, 0.006, 0.93)),
            (30, 19): (Stranding(_TWO, 0.0275, 0.93), Stranding(_CORE_19, 0.006, 0.93)),
            (54, 19): (Stranding(_THREE, 0.030, 0.91), Stranding(_CORE_19, 0.006, 0.93)),
            (76, 19): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_19, 0.006, 0.93)),
            (84, 19): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_19, 0.006, 0.93)),
            **_OFF_TABLE,
        }
    )

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """10.1: aluminum at its tensile strength, steel at its least stress at 1% extension."""
        if issubclass(metal, Steel):
            return metal.extension_stress.at(diameter, metric)
        return metal.tensile_strength.at(diameter, metric)


class B399(ASTM[Kcmil | Gauge], AAAC[Round[Aluminum6201T81]]):
    """Aluminum alloy 6201-T81, round wires, of class AA, A or both.

    ASTM B399/B399M-04 (2021), 7.1, class AA's lay; 7.4, its hand. Class A has no preferred
    lay (7.2). Rating factors: B399/B399M-23, table 5."""

    standard = "ASTM B399"
    hand = Hand.RIGHT
    strandings = MappingProxyType(
        {
            (7,): (Stranding((_AA,), rating_factor=0.96),),
            (19,): (Stranding((_AA,) * 2, rating_factor=0.93),),
            (37,): (Stranding((_AA,) * 3, rating_factor=0.91),),
            (61,): (Stranding((_AA,) * 4, rating_factor=0.90),),
        }
    )

    classes: tuple[str, ...]
    """Its classes, as its listings print them, in alphabetical order: ``("A", "AA")``."""

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """Class AA's; a class A conductor's rating factors alone, as 7.2 fixes it no lay."""
        return _class_lay(super().stranding, self.classes)


class B416(ASTM[WireGauge], ACS[Round[AluminumCladSteel]]):
    """Aluminum-clad steel strand.

    ASTM B416-98 (2023): 6.1, a 3-wire strand's lay; 7, its rating factors, of its wires'
    tensile strength (ASTM B415, 20% column); its hand, left (4.1.3). ASTM B416-98 (2018), 6.2:
    each layer of its 7-, 19- and 37-wire strands, 13.5 preferred."""

    standard = "ASTM B416"
    hand = Hand.LEFT
    strandings = MappingProxyType(
        {
            (3,): (Stranding((LayRatio(14, 20, 16.5),), rating_factor=0.95),),
            (7,): (Stranding((_AA,), rating_factor=0.90),),
            (19,): (Stranding((_AA,) * 2, rating_factor=0.90),),
            (37,): (Stranding((_AA,) * 3, rating_factor=0.90),),
        }
    )


def _acar(aluminum: int, alloy: int, factors: tuple[float, float]) -> tuple[Stranding, Stranding]:
    """A row of ASTM B524-99's table 6: how many layers each metal's wires lie in, a layer of
    both counting for each (note A), at 6.1's lay, and each metal's rating factor."""
    return (
        Stranding((_AA,) * aluminum, rating_factor=factors[0]),
        Stranding((_AA,) * alloy, rating_factor=factors[1]),
    )


class B524(
    ASTM[Kcmil | Mm2],
    ACAR[Round[Aluminum1350H19], Round[Aluminum6201T81]],
):
    """ACAR, aluminum 1350 around aluminum alloy 6201-T81.

    Its strandings: ASTM B524/B524M-99, table 6, the rating factors, and 6.1, each layer's lay
    ratio, 13.5 preferred; its hand, 6.2."""

    standard = "ASTM B524"
    hand = Hand.RIGHT
    strandings = MappingProxyType(
        {
            (4, 3): _acar(1, 1, (0.96, 0.96)),
            (15, 4): _acar(2, 1, (0.93, 0.96)),
            (12, 7): _acar(1, 1, (0.96, 0.96)),
            (33, 4): _acar(3, 1, (0.91, 0.96)),
            (30, 7): _acar(2, 1, (0.93, 0.96)),
            (24, 13): _acar(2, 2, (0.93, 0.93)),
            (18, 19): _acar(1, 2, (0.96, 0.93)),
            (54, 7): _acar(3, 1, (0.91, 0.96)),
            (48, 13): _acar(3, 2, (0.91, 0.93)),
            (42, 19): _acar(2, 2, (0.93, 0.93)),
            (33, 28): _acar(2, 3, (0.93, 0.91)),
            (72, 19): _acar(3, 2, (0.91, 0.93)),
            (63, 28): _acar(3, 3, (0.91, 0.91)),
            (54, 37): _acar(2, 3, (0.93, 0.91)),
        }
    )

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """8.1: aluminum 1350 at its tensile strength; aluminum alloy 6201 at its stress at 1%
        extension, taken as 95% of its tensile strength."""
        tensile = metal.tensile_strength.at(diameter, metric)
        return 0.95 * tensile if issubclass(metal, Aluminum6201T81) else tensile


class B549(
    ASTM[Kcmil | Gauge],
    ACSR[Round[Aluminum1350H19], Round[AluminumCladSteel]],
):
    """ACSR/AW, aluminum 1350 around an aluminum-clad steel core.

    Its strandings: ASTM B549-13, table 2, the lay ratios of its class AA aluminum layers, and
    ASTM B500/B500M, its core's (8.1); table 3, the rating factors; table 4, the increments that
    fix the lay, as B232's do; its hand, 8.2. 10.1 rates its aluminum at its tensile strength
    and its core at its stress at 1% extension, of a grade ASTM B502/B502M-23 gives. Its mixed
    layers of aluminum and aluminum-clad wires, AWAC, openline does not lay."""

    standard = "ASTM B549"
    hand = Hand.RIGHT
    grades = (AluminumCladSteelAW2, AluminumCladSteelAW3)
    strandings = MappingProxyType(
        {
            (6, 1): (Stranding((LayRatio(12, 16),), 0.015, 0.96), Stranding((), 0.0, 0.96)),
            (7, 1): (Stranding((LayRatio(12, 16),), 0.015, 0.96), Stranding((), 0.0, 0.96)),
            # Table 4's 2.0% lies beyond what table 2's 12 to 16 gives Grouse/AW's wires, 1.8%
            # at 12: the range's middle.
            (8, 1): (Stranding((LayRatio(12, 16),), None, 0.96), Stranding((), 0.0, 0.96)),
            (18, 1): (Stranding(_TWO, 0.020, 0.93), Stranding((), 0.0, 0.96)),
            (36, 1): (Stranding(_THREE, 0.020, 0.91), Stranding((), 0.0, 0.96)),
            (12, 7): (Stranding(_ONE, 0.025, 0.96), Stranding(_CORE_7, 0.004, 0.96)),
            (24, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (26, 7): (Stranding(_TWO, 0.025, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (30, 7): (Stranding(_TWO, 0.0275, 0.93), Stranding(_CORE_7, 0.004, 0.96)),
            (42, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (45, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (48, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (54, 7): (Stranding(_THREE, 0.025, 0.91), Stranding(_CORE_7, 0.004, 0.96)),
            (72, 7): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_7, 0.004, 0.96)),
            (16, 19): (Stranding(_ONE, 0.025, 0.96), Stranding(_CORE_19, 0.006, 0.93)),
            (30, 19): (Stranding(_TWO, 0.0275, 0.93), Stranding(_CORE_19, 0.006, 0.93)),
            (54, 19): (Stranding(_THREE, 0.030, 0.91), Stranding(_CORE_19, 0.006, 0.93)),
            (76, 19): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_19, 0.006, 0.93)),
            (84, 19): (Stranding(_FOUR, 0.030, 0.90), Stranding(_CORE_19, 0.006, 0.93)),
            **{key: value for key, value in _OFF_TABLE.items() if key[0] > 6},
        }
    )

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """10.1: aluminum at its tensile strength, the core at its stress at 1% extension."""
        if issubclass(metal, Steel):
            return metal.extension_stress.at(diameter, metric)
        return metal.tensile_strength.at(diameter, metric)


class B778(ASTM[Kcmil], AAC[Trapezoidal[Aluminum1350H19]]):
    """AAC/TW, aluminum 1350, trapezoidal wires about a round one.

    ASTM B778-22: 6.1 to 6.3, the lay ratios of its outside layer, the one beneath it and those
    within; its hand, 6.5 of the B778-19 its redline shows. No increment at hand: its layers lie
    at the middle of their ranges. Its rating factors, an educated guess: B231's, table 6, for as
    many layers about the center."""

    standard = "ASTM B778"
    hand = Hand.RIGHT

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """6.1 to 6.3, from the outside in, for as many layers as its wires make; none where they
        are not known."""
        layers = self.wires.layers
        if layers is None:
            return None
        ratios = (LayRatio(10, 14), LayRatio(10, 16), *(LayRatio(10, 17),) * (layers - 2))
        return (Stranding(ratios[:layers], rating_factor=_B231_RATING.get(layers)),)


class B779(
    ASTM[Kcmil],
    ACSR[Trapezoidal[Aluminum1350H19], Round[CoatedSteel]],
):
    """ACSR/TW, trapezoidal aluminum 1350 around a coated-steel core.

    Its grades of core: ASTM B779-22, 3.1.4 to 3.1.8. Tables 1 and 2, footnote C, rate its steel
    at its stress at 1% extension. Its stranding, ``_b779``, and its hand are educated guesses."""

    standard = "ASTM B779"
    # Educated guess: the B779-22 at hand stops before it gives its hand; right, as B857-14, 7.7,
    # lays ACSS/TW, whose lay ``_b779`` takes, and B232-17, 8.3, ACSR.
    hand = Hand.RIGHT
    grades = (SteelGA2, SteelMA2, SteelGC2, SteelGA3, SteelMA3)

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """``_b779``: as its aluminum's layers and its core's wires give."""
        return _b779(self.outer.layers, self.core.count)

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """Aluminum at its tensile strength, steel at its stress at 1% extension."""
        if issubclass(metal, Steel):
            return metal.extension_stress.at(diameter, metric)
        return metal.tensile_strength.at(diameter, metric)


class B779_AW(
    ASTM[Kcmil],
    ACSR[Trapezoidal[Aluminum1350H19], Round[AluminumCladSteel]],
):
    """ACSR/TW/AW, trapezoidal aluminum 1350 around an aluminum-clad steel core.

    Its grades of core: AW2 and AW3, ASTM B779-22, 3.1.2 and 3.1.3, of ASTM B502 wire. Laid and
    rated as ``B779``."""

    standard = "ASTM B779, AW"
    hand = B779.hand
    grades = (AluminumCladSteelAW2, AluminumCladSteelAW3)
    stranding = B779.stranding
    stress = staticmethod(B779.stress)


class B856(
    ASTM[Kcmil],
    ACSS[Round[Aluminum1350O], Round[CoatedSteel]],
):
    """ACSS, annealed aluminum 1350 around a coated-steel core.

    ASTM B856-03, table 2 gives lay limits and preferences; 7.2, its hand; table 3, rating
    factors. Inner aluminum layers without a preference use the midpoint of their range as
    a model assumption. Table 3's approximate mass/resistance increments do not fix the lay
    (11.1). Construction 42/7 and 48/7 have rating factors but no lay in table 2.

    Clause 9.1 rates aluminum at its minimum lot-average tensile strength and steel at its
    minimum ultimate tensile strength, as the inherited ``stress`` selects. Its grades of
    core: ASTM B856-22, 3.3.4 to 3.3.12."""

    standard = "ASTM B856"
    grades = (
        SteelGA2,
        SteelMA2,
        SteelGC2,
        SteelGA3,
        SteelMA3,
        SteelGA4,
        SteelMA4,
        SteelGA5,
        SteelMA5,
    )
    hand = Hand.RIGHT
    strandings = MappingProxyType(
        {
            (12, 7): (
                Stranding(_ACSS_ONE, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (24, 7): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (26, 7): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (30, 7): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            # Educated guess: table 2 gives 42/7 and 48/7 no lay,
            # and 20/7, 22/7 and 68/7 neither lay nor rating; each as the rows of as many layers.
            (20, 7): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (22, 7): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (42, 7): (
                Stranding(_ACSS_THREE, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (45, 7): (
                Stranding(_ACSS_THREE, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (48, 7): (
                Stranding(_ACSS_THREE, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (68, 7): (
                Stranding(_ACSS_FOUR, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (54, 7): (
                Stranding(_ACSS_THREE, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (72, 7): (
                Stranding(_ACSS_FOUR, rating_factor=0.96),
                Stranding(_ACSS_CORE_7, rating_factor=1.00),
            ),
            (16, 19): (
                Stranding(_ACSS_ONE, rating_factor=0.96),
                Stranding(_ACSS_CORE_19, rating_factor=1.00),
            ),
            (30, 19): (
                Stranding(_ACSS_TWO, rating_factor=0.96),
                Stranding(_ACSS_CORE_19, rating_factor=1.00),
            ),
            (54, 19): (
                Stranding(_ACSS_THREE, rating_factor=0.96),
                Stranding(_ACSS_CORE_19, rating_factor=1.00),
            ),
            (76, 19): (
                Stranding(_ACSS_FOUR, rating_factor=0.96),
                Stranding(_ACSS_CORE_19, rating_factor=1.00),
            ),
            (84, 19): (
                Stranding(_ACSS_FOUR, rating_factor=0.96),
                Stranding(_ACSS_CORE_19, rating_factor=1.00),
            ),
        }
    )


class B856_AW(
    ASTM[Kcmil],
    ACSS[Round[Aluminum1350O], Round[AluminumCladSteel]],
):
    """ACSS/AW, annealed aluminum 1350 around an aluminum-clad steel core.

    Laid and rated as ``B856``. Its grades of core: AW, ASTM B856-03, table 4, of ASTM B502 wire;
    AW2 and AW3, ASTM B856-22, table 1."""

    standard = "ASTM B856, AW"
    grades = (AluminumCladSteel, AluminumCladSteelAW2, AluminumCladSteelAW3)
    hand = B856.hand
    strandings = B856.strandings


# ASTM B231-16 (2021), table 6: the rating factor by layers about the center wire.
_B231_RATING = {1: 0.96, 2: 0.93, 3: 0.91, 4: 0.90, 5: 0.89, 6: 0.89}
# ASTM B857-14, 7.4 to 7.6: a steel core's 6-, 12- and 18-wire layers, from the outside in.
_B857_CORE = {1: (), 7: _CORE_7, 19: _CORE_19, 37: (LayRatio(14, 20), *_CORE_19)}
# Table 4: the aluminum's layers and the core's wires it rates, at 96% and 100%.
_B857_RATED = {(2, 7), (2, 19), (2, 37), (3, 7), (3, 19), (3, 37), (4, 19), (4, 37)}


def _b857(layers: int | None, core: int) -> tuple[Stranding, ...] | None:
    """ASTM B857-14's stranding of trapezoidal aluminum in ``layers`` about a core of ``core``
    wires: 7.1 to 7.3, the aluminum's lay ratios from the outside in, 11 and 13 preferred, those
    within at their ranges' midpoints, as ``B856``'s; 7.4 to 7.6, the core's; table 4, the
    rating factors. Table 5's increments are approximate (11.1) and do not fix the lay. None
    where its layers are not known."""
    if layers is None or core not in _B857_CORE:
        return None
    aluminum = (LayRatio(10, 13, 11), LayRatio(10, 16, 13), *(LayRatio(10, 17),) * (layers - 2))
    rated = (layers, core) in _B857_RATED
    return (
        Stranding(aluminum[:layers], rating_factor=0.96 if rated else None),
        Stranding(_B857_CORE[core], rating_factor=1.00 if rated else None),
    )


# Educated guess: ASTM B232-17, table 6, its two-layer aluminum's
# rating factor for every layer, and its core's by wires, which B779-22's tables 1 and 2 meet
# best, median 0.0%.
_B779_ALUMINUM = 0.93
_B779_CORE = {1: 0.96, 7: 0.96, 19: 0.93}


def _b779(layers: int | None, core: int) -> tuple[Stranding, ...] | None:
    """ASTM B779's stranding of trapezoidal aluminum in ``layers`` about a core of ``core``
    wires, an educated guess: B857-14's lay, 7.1 to 7.6, of which
    B779-22, 7.1, gives the outside layer's range alike; B232-17's rating factors, table 6, the
    two-layer aluminum's for every layer, the core's by its wires. None where its layers are not
    known."""
    if layers is None or core not in _B857_CORE:
        return None
    aluminum = (LayRatio(10, 13, 11), LayRatio(10, 16, 13), *(LayRatio(10, 17),) * (layers - 2))
    return (
        Stranding(aluminum[:layers], rating_factor=_B779_ALUMINUM),
        Stranding(_B857_CORE[core], rating_factor=_B779_CORE.get(core)),
    )


class B857(
    ASTM[Kcmil],
    ACSS[Trapezoidal[Aluminum1350O], Round[CoatedSteel]],
):
    """ACSS/TW, trapezoidal annealed aluminum 1350 around a coated-steel core.

    Its grades of core: ASTM B857-22, 3.3.4 to 3.3.12; its hand, B857-14, 7.7. Clause 9.1 rates
    its aluminum as round wires of equal area at their minimum lot-average tensile strength, and
    its steel at its minimum ultimate tensile strength, as the inherited ``stress`` selects."""

    standard = "ASTM B857"
    hand = Hand.RIGHT
    grades = (
        SteelGA2,
        SteelMA2,
        SteelGC2,
        SteelGA3,
        SteelMA3,
        SteelGA4,
        SteelMA4,
        SteelGA5,
        SteelMA5,
    )

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """``_b857``: as its aluminum's layers and its core's wires give."""
        return _b857(self.outer.layers, self.core.count)


class B857_AW(
    ASTM[Kcmil],
    ACSS[Trapezoidal[Aluminum1350O], Round[AluminumCladSteel]],
):
    """ACSS/TW/AW, trapezoidal annealed aluminum 1350 around an aluminum-clad steel core.

    Laid and rated as ``B857``. Its grades of core: AW2 and AW3, ASTM B857-14, 3.3.2 and 3.3.3,
    of ASTM B502 wire."""

    standard = "ASTM B857, AW"
    hand = Hand.RIGHT
    grades = (AluminumCladSteelAW2, AluminumCladSteelAW3)

    @property
    def stranding(self) -> tuple[Stranding, ...] | None:
        """``_b857``: as its aluminum's layers and its core's wires give."""
        return _b857(self.outer.layers, self.core.count)
