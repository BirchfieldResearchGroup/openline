"""CSA conductor standards."""

from types import MappingProxyType

from ..materials import Aluminum1350H19, HardDrawnAluminum, Metal, Steel, SteelS1A, ZincCoatedSteel
from ..units import Length, Stress
from . import AAC, ACSR, CSA, Stranding
from .designations import Code, Gauge, Kcmil
from .strands import Hand, LayRatio, Round

__all__ = ["C49", "C61089", "C61089_A1"]

# IEC 61089:1991, 5.4.5, which CAN/CSA-C61089-11 keeps: the outer aluminum layer, and every one
# within it. Its Canadian deviation 5.4.4.1: a steel core's 6-wire layer, and its 12-wire one.
_OUTER = LayRatio(10, 14)
_INNER = LayRatio(10, 16)
_STEEL = {1: (), 7: (LayRatio(16, 26),), 19: (LayRatio(14, 22), LayRatio(16, 26))}
# CAN/CSA-C61089-11, table 2, the increments due to stranding: the aluminum's by its wires and
# layers about the axis, the steel's by its wires, each alike in every row that has it.
_ALUMINUM = {
    (6, 1): 0.0152,
    (7, 1): 0.0131,
    (8, 1): 0.0180,
    (12, 1): 0.0217,
    (16, 1): 0.0261,
    (18, 2): 0.0190,
    (19, 2): 0.0180,
    (22, 2): 0.0204,
    (24, 2): 0.0210,
    (26, 2): 0.0216,
    (30, 2): 0.0232,
    (37, 3): 0.0204,
    (42, 3): 0.0251,
    (45, 3): 0.0223,
    (48, 3): 0.0260,
    (54, 3): 0.0233,
    (61, 4): 0.0219,
    (68, 4): 0.0290,
    (72, 4): 0.0232,
    (76, 4): 0.0297,
    (84, 4): 0.0240,
    (91, 5): 0.0230,
    (127, 6): 0.0312,
}
_STEEL_INCREMENT = {1: 0.0, 7: 0.0043, 19: 0.0077}


def _homogeneous() -> MappingProxyType[tuple[int, ...], tuple[Stranding, ...]]:
    """Its strandings of aluminum alone, by how many layers lie about the central wire."""
    layers = {7: 1, 19: 2, 37: 3, 61: 4, 91: 5, 127: 6}
    return MappingProxyType(
        {
            (n,): (Stranding((_OUTER,) + (_INNER,) * (k - 1), _ALUMINUM[n, k], 1.0),)
            for n, k in layers.items()
        }
    )


def _steel_cored() -> MappingProxyType[tuple[int, ...], tuple[Stranding, ...]]:
    """Its strandings over a steel core, by how many layers the aluminum makes."""
    layers = {
        (6, 1): 1,
        (6, 7): 1,
        (7, 1): 1,
        (8, 1): 1,
        (8, 7): 1,
        (12, 7): 1,
        (16, 19): 1,
        (18, 1): 2,
        (22, 7): 2,
        (24, 7): 2,
        (26, 7): 2,
        (30, 7): 2,
        (30, 19): 2,
        (42, 7): 3,
        (45, 7): 3,
        (48, 7): 3,
        (54, 7): 3,
        (54, 19): 3,
        (68, 7): 4,
        (72, 7): 4,
        (76, 19): 4,
        (84, 19): 4,
    }
    return MappingProxyType(
        {
            (al, st): (
                Stranding((_OUTER,) + (_INNER,) * (k - 1), _ALUMINUM[al, k], 1.0),
                Stranding(_STEEL[st], _STEEL_INCREMENT[st], 1.0),
            )
            for (al, st), k in layers.items()
        }
    )


def _wires(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
    """Deviation 5.7.2: aluminum at its tensile strength, steel at its stress at 1% extension, of
    wires to CAN/CSA-C60889 and C60888. Those not at hand, an educated guess: aluminum as ASTM
    B230's 1350-H19, steel as IEC 60888's S1A, which Prysmian's Canadian strengths meet, median
    0.0%."""
    if issubclass(metal, Steel):
        return SteelS1A.extension_stress.at(diameter, metric)
    return Aluminum1350H19.tensile_strength.at(diameter, metric)


class C49(
    CSA[Kcmil | Gauge],
    ACSR[Round[HardDrawnAluminum], Round[ZincCoatedSteel]],
):
    """ACSR, aluminum around a zinc-coated steel core.

    Its strandings, hand and wires, an educated guess: those of
    ``C61089``, whose wires 77 of Midal's 86 C49 conductors share."""

    standard = "CSA C49"
    hand = Hand.RIGHT
    strandings = _steel_cored()
    stress = staticmethod(_wires)


class C61089(CSA[Code], ACSR[Round[HardDrawnAluminum], Round[ZincCoatedSteel]]):
    """ACSR, A1 aluminum around a core of zinc-coated steel, designated by code number.

    CAN/CSA-C61089-11 adopts IEC 61089:1991 with Canadian deviations. Its strandings: the lay
    ratios of the aluminum, IEC 61089, 5.4.5, which no deviation replaces, and of the steel,
    deviation 5.4.4.1; the increments, table 2, which deviation replaces and 5.6.2 takes the
    masses from; its hand, IEC 61089, 5.4.2; deviation 5.7.2, its rating, the sum of its wires'
    strengths, ``_wires``."""

    standard = "CAN/CSA C61089"
    hand = Hand.RIGHT
    strandings = _steel_cored()
    stress = staticmethod(_wires)


class C61089_A1(CSA[Code], AAC[Round[HardDrawnAluminum]]):
    """A1 aluminum alone, designated by code number.

    CAN/CSA-C61089-11: the lay ratios, IEC 61089, 5.4.5; the increments, table 2; its hand,
    IEC 61089, 5.4.2; its rating, IEC 61089, 5.7.1, the sum of its wires' strengths, ``_wires``."""

    standard = "CAN/CSA C61089, A1"
    hand = Hand.RIGHT
    strandings = _homogeneous()
    stress = staticmethod(_wires)
