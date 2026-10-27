"""British conductor standards: BS EN 50182 constructions."""

from types import MappingProxyType

from ..materials import AluminumAL3
from . import AAAC, BS, Stranding
from .designations import Code
from .strands import Hand, LayRatio, Round

__all__ = ["BS_EN50182_AL3"]

# EN 50182:2001, table 2: the outer aluminum layer, and every one within it.
_OUTER = LayRatio(10, 14)
_INNER = LayRatio(10, 16)


class BS_EN50182_AL3(BS[Code], AAAC[Round[AluminumAL3]]):
    """Aluminum alloy AL3, designated by code number.

    Its strandings: EN 50182:2001, table 2, the lay ratios, table 4, the increments, and 5.9.1,
    rated at the sum of its wires' strengths; its hand, 5.5.2."""

    standard = "BS EN 50182, AL3"
    hand = Hand.RIGHT
    strandings = MappingProxyType(
        {
            (7,): (Stranding((_OUTER,), 0.0111, 1.0),),
            (19,): (Stranding((_OUTER, _INNER), 0.0168, 1.0),),
            (37,): (Stranding((_OUTER, _INNER, _INNER), 0.0203, 1.0),),
            (61,): (Stranding((_OUTER, _INNER, _INNER, _INNER), 0.0236, 1.0),),
            (91,): (Stranding((_OUTER, *(_INNER,) * 4), 0.0278, 1.0),),
        }
    )
