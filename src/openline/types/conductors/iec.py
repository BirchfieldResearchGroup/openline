"""IEC 61089 conductor constructions."""

from types import MappingProxyType
from typing import ClassVar

from ..materials import (
    AluminumA1,
    AluminumA2,
    AluminumA3,
    Metal,
    Steel,
    SteelS1A,
    SteelS1B,
    SteelS2A,
    SteelS2B,
    SteelS3A,
    ZincCoatedSteel,
)
from ..units import Length, Stress
from . import AAAC, AAC, AACSR, ACAR, ACSR, IEC, Stranding
from .designations import Code
from .strands import Hand, LayRatio, Round

__all__ = [
    "A1",
    "A1_A2",
    "A1_A3",
    "A2",
    "A3",
    "IEC61089",
    "A1_Syz",
    "A2_Syz",
    "A3_Syz",
]

# IEC 61089:1991, 5.4.5: the outer aluminium layer, and every one within it; 5.4.4: a steel
# core's 6-wire layer, and its 12-wire one.
_OUTER = LayRatio(10, 14)
_INNER = LayRatio(10, 16)
_STEEL_6 = LayRatio(16, 26)
_STEEL_12 = LayRatio(14, 22)
_STEEL = {1: (), 7: (_STEEL_6,), 19: (_STEEL_12, _STEEL_6)}


def _aluminium(layers: int, outer: bool, factor: float) -> Stranding:
    """An aluminium strand of so many layers, the conductor's outer one among them or not, rated
    at ``factor`` of its wires' strength."""
    return Stranding(((_OUTER,) if outer else ()) + (_INNER,) * (layers - outer), None, factor)


def _homogeneous() -> MappingProxyType[tuple[int, ...], tuple[Stranding, ...]]:
    """Its 7-, 19-, 37-, 61- and 91-wire strandings, at the sum of its wires' strength (5.7.1)."""
    layers = {7: 1, 19: 2, 37: 3, 61: 4, 91: 5}
    return MappingProxyType({(n,): (_aluminium(k, True, 1.0),) for n, k in layers.items()})


def _steel_cored() -> MappingProxyType[tuple[int, ...], tuple[Stranding, ...]]:
    """Its strandings over a steel core: the aluminium layers, and the core, each at the sum of
    its wires' strength (5.7.2)."""
    layers = {
        (6, 1): 1,
        (18, 1): 2,
        (22, 7): 2,
        (26, 7): 2,
        (45, 7): 3,
        (54, 7): 3,
        (54, 19): 3,
        (72, 7): 4,
        (72, 19): 4,
        (84, 7): 4,
        (84, 19): 4,
    }
    return MappingProxyType(
        {
            (al, st): (_aluminium(k, True, 1.0), Stranding(_STEEL[st], None, 1.0))
            for (al, st), k in layers.items()
        }
    )


def _alloy_cored() -> MappingProxyType[tuple[int, ...], tuple[Stranding, ...]]:
    """Its strandings over an alloy core of wires as thick: A1 at the sum of its wires' strength,
    the alloy at 95% of it (5.7.3); 4/3's one layer is of both."""
    layers = {
        (4, 3): (1, 1, True),
        (12, 7): (1, 1, False),
        (18, 19): (1, 2, False),
        (24, 37): (1, 3, False),
        (30, 7): (2, 1, False),
        (42, 19): (2, 2, False),
        (54, 7): (3, 1, False),
        (54, 37): (2, 3, False),
        (72, 19): (3, 2, False),
    }
    return MappingProxyType(
        {
            counts: (_aluminium(a1, True, 1.0), _aluminium(alloy, shared, 0.95))
            for counts, (a1, alloy, shared) in layers.items()
        }
    )


class IEC61089(IEC[Code]):
    """IEC 61089: round-wire conductors, designated by construction and code number.

    IEC 61089:1991, as COMESA FDHS 307:2007 adopts it: each layer at the mean of its lay ratios
    (5.4.4, 5.4.5), on which 5.6.2 bases its masses; its hand, 5.4.2; 5.7 rates its aluminium
    at its tensile strength and its steel at its stress at 1% extension."""

    standard: ClassVar[str] = "IEC 61089"
    hand = Hand.RIGHT

    @staticmethod
    def stress(metal: type[Metal], diameter: Length, metric: bool) -> Stress:
        """5.7: aluminium at its tensile strength, steel at its stress at 1% extension."""
        if issubclass(metal, Steel):
            return metal.extension_stress.at(diameter, metric)
        return metal.tensile_strength.at(diameter, metric)


class A1(IEC61089, AAC[Round[AluminumA1]]):
    """Aluminium A1."""

    standard = "IEC 61089, A1"
    strandings = _homogeneous()


class A2(IEC61089, AAAC[Round[AluminumA2]]):
    """Aluminium alloy A2."""

    standard = "IEC 61089, A2"
    strandings = _homogeneous()


class A3(IEC61089, AAAC[Round[AluminumA3]]):
    """Aluminium alloy A3."""

    standard = "IEC 61089, A3"
    strandings = _homogeneous()


class A1_Syz(IEC61089, ACSR[Round[AluminumA1], Round[ZincCoatedSteel]]):
    """Aluminium A1 around a core of zinc-coated steel.

    Its grades of core, which its designation names, Syz (3.4): S1A to S3A (1.2)."""

    standard = "IEC 61089, A1/Syz"
    grades = (SteelS1A, SteelS1B, SteelS2A, SteelS2B, SteelS3A)
    strandings = _steel_cored()


class A2_Syz(IEC61089, AACSR[Round[AluminumA2], Round[ZincCoatedSteel]]):
    """Aluminium alloy A2 around a core of zinc-coated steel.

    Its grades of core: S1A, S1B and S3A (1.2)."""

    standard = "IEC 61089, A2/Syz"
    grades = (SteelS1A, SteelS1B, SteelS3A)
    strandings = _steel_cored()


class A3_Syz(IEC61089, AACSR[Round[AluminumA3], Round[ZincCoatedSteel]]):
    """Aluminium alloy A3 around a core of zinc-coated steel.

    Its grades of core: S1A, S1B and S3A (1.2)."""

    standard = "IEC 61089, A3/Syz"
    grades = (SteelS1A, SteelS1B, SteelS3A)
    strandings = _steel_cored()


class A1_A2(IEC61089, ACAR[Round[AluminumA1], Round[AluminumA2]]):
    """Aluminium A1 around a core of aluminium alloy A2."""

    standard = "IEC 61089, A1/A2"
    strandings = _alloy_cored()


class A1_A3(IEC61089, ACAR[Round[AluminumA1], Round[AluminumA3]]):
    """Aluminium A1 around a core of aluminium alloy A3."""

    standard = "IEC 61089, A1/A3"
    strandings = _alloy_cored()
