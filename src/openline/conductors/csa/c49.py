"""CSA C49: ACSR, aluminum around a zinc-coated steel core."""

from openline.types.conductors.csa import C49
from openline.types.conductors.designations import Gauge, Kcmil
from openline.types.conductors.strands import Round
from openline.types.materials import HardDrawnAluminum, ZincCoatedSteel
from openline.types.units import mm

WREN = C49(
    code_words=("Wren",),
    designation=Gauge(8),
    outer=Round(HardDrawnAluminum, 6, mm(1.33)),
    core=Round(ZincCoatedSteel, 1, mm(1.33)),
)

WARBLER = C49(
    code_words=("Warbler",),
    designation=Gauge(7),
    outer=Round(HardDrawnAluminum, 6, mm(1.5)),
    core=Round(ZincCoatedSteel, 1, mm(1.5)),
)

BANTAM = C49(
    code_words=("Bantam",),
    designation=Kcmil(13.1),
    outer=Round(HardDrawnAluminum, 3, mm(1.68)),
    core=Round(ZincCoatedSteel, 4, mm(1.68)),
)

THRUSH = C49(
    code_words=("Thrush",),
    designation=Gauge(5),
    outer=Round(HardDrawnAluminum, 6, mm(1.89)),
    core=Round(ZincCoatedSteel, 1, mm(1.89)),
)

MAGPIE = C49(
    code_words=("Magpie",),
    designation=Kcmil(20.87),
    outer=Round(HardDrawnAluminum, 3, mm(2.12)),
    core=Round(ZincCoatedSteel, 4, mm(2.12)),
)

SWALLOW = C49(
    code_words=("Swallow",),
    designation=Gauge(3),
    outer=Round(HardDrawnAluminum, 6, mm(2.38)),
    core=Round(ZincCoatedSteel, 1, mm(2.38)),
)

SHRIKE = C49(
    code_words=("Shrike",),
    designation=Kcmil(33.2),
    outer=Round(HardDrawnAluminum, 3, mm(2.67)),
    core=Round(ZincCoatedSteel, 4, mm(2.67)),
)

SNIPE = C49(
    code_words=("Snipe",),
    designation=Kcmil(52.825),
    outer=Round(HardDrawnAluminum, 3, mm(3.37)),
    core=Round(ZincCoatedSteel, 4, mm(3.37)),
)

LOON = C49(
    code_words=("Loon",),
    designation=Kcmil(66.5),
    outer=Round(HardDrawnAluminum, 3, mm(3.78)),
    core=Round(ZincCoatedSteel, 4, mm(3.78)),
)

PELICAN = C49(
    code_words=("Pelican",),
    designation=Kcmil(477),
    outer=Round(HardDrawnAluminum, 18, mm(4.14)),
    core=Round(ZincCoatedSteel, 1, mm(4.14)),
)

KCMIL_715_5_42_7 = C49(
    code_words=(),
    designation=Kcmil(715.5),
    outer=Round(HardDrawnAluminum, 42, mm(3.31)),
    core=Round(ZincCoatedSteel, 7, mm(1.84)),
)

KCMIL_795_42_7 = C49(
    code_words=(),
    designation=Kcmil(795),
    outer=Round(HardDrawnAluminum, 42, mm(3.5)),
    core=Round(ZincCoatedSteel, 7, mm(1.94)),
)

MALLARD = C49(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Round(HardDrawnAluminum, 30, mm(4.14)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)

KCMIL_1033_5_42_7 = C49(
    code_words=(),
    designation=Kcmil(1033.5),
    outer=Round(HardDrawnAluminum, 42, mm(3.99)),
    core=Round(ZincCoatedSteel, 7, mm(2.21)),
)

KCMIL_1113_42_7 = C49(
    code_words=(),
    designation=Kcmil(1113),
    outer=Round(HardDrawnAluminum, 42, mm(4.14)),
    core=Round(ZincCoatedSteel, 7, mm(2.3)),
)

PLOVER = C49(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Round(HardDrawnAluminum, 54, mm(4.14)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)
