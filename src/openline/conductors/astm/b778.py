"""ASTM B778: AAC/TW, aluminum 1350, trapezoidal wires about a round one."""

from openline.types.conductors.astm import B778
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Trapezoidal
from openline.types.materials import Aluminum1350H19
from openline.types.units import equivalent, inch, kcmil

# Educated guess: no AAC/TW design of 15 wires prints its layers; those of 17, the nearest count,
# print 2.
_LAYERS_OF_15 = 2

# Educated guess: no AAC/TW design of 28 wires prints its layers; those of 31, the nearest count,
# print 3.
_LAYERS_OF_28 = 3

# Educated guess: no AAC/TW design of 45 wires prints its layers; those of 49, the nearest count,
# print 4.
_LAYERS_OF_45 = 4

# Educated guess: no AAC/TW design of 46 wires prints its layers; those of 49, the nearest count,
# print 4.
_LAYERS_OF_46 = 4


LOGAN = B778(
    code_words=("Logan",),
    designation=Kcmil(322.5),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(322.5), 17), layers=2, outside_diameter=inch(0.6)
    ),
)

TULIP = B778(
    code_words=("Tulip",),
    designation=Kcmil(336.4),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(336.4), 17), layers=2, outside_diameter=inch(0.612)
    ),
)

KCMIL_384_5_17 = B778(
    code_words=(),
    designation=Kcmil(384.5),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(384.5), 17), layers=2, outside_diameter=inch(0.65)
    ),
)

CANNA = B778(
    code_words=("Canna",),
    designation=Kcmil(397.5),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(397.5), 17), layers=2, outside_diameter=inch(0.661)
    ),
)

WHEELER = B778(
    code_words=("Wheeler",),
    designation=Kcmil(449.4),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(449.4), 17), layers=2, outside_diameter=inch(0.7)
    ),
)

COSMOS = B778(
    code_words=("Cosmos",),
    designation=Kcmil(477),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(477), 17), layers=2, outside_diameter=inch(0.72)
    ),
)

ZINNIA = B778(
    code_words=("Zinnia",),
    designation=Kcmil(500),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(500), 17), layers=2, outside_diameter=inch(0.736)
    ),
)

KCMIL_521_7_17 = B778(
    code_words=(),
    designation=Kcmil(521.7),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(521.7), 17), layers=2, outside_diameter=inch(0.75)
    ),
)

MISTLETOE = B778(
    code_words=("Mistletoe",),
    designation=Kcmil(556.5),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(556.5), 17), layers=2, outside_diameter=inch(0.775)
    ),
)

ROBSON = B778(
    code_words=("Robson",),
    designation=Kcmil(595.8),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(595.8), 17), layers=2, outside_diameter=inch(0.8)
    ),
)

MEADOWSWEET = B778(
    code_words=("Meadowsweet",),
    designation=Kcmil(600),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(600), 17), layers=2, outside_diameter=inch(0.803)
    ),
)

ORCHID = B778(
    code_words=("Orchid",),
    designation=Kcmil(636),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(636), 17), layers=2, outside_diameter=inch(0.825)
    ),
)

KCMIL_678_2_17 = B778(
    code_words=(),
    designation=Kcmil(678.2),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(678.2), 17), layers=2, outside_diameter=inch(0.85)
    ),
)

VERBENA = B778(
    code_words=("Verbena",),
    designation=Kcmil(700),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(700), 17), layers=2, outside_diameter=inch(0.864)
    ),
)

NASTURTIUM = B778(
    code_words=("Nasturtium",),
    designation=Kcmil(750),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(750), 17), layers=2, outside_diameter=inch(0.893)
    ),
)

MCKINLEY = B778(
    code_words=("McKinley",),
    designation=Kcmil(761.5),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(761.5), 17), layers=2, outside_diameter=inch(0.9)
    ),
)

ARBUTUS = B778(
    code_words=("Arbutus",),
    designation=Kcmil(795),
    wires=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(795), 17), layers=2, outside_diameter=inch(0.919)
    ),
)

KCMIL_854_2_15 = B778(
    code_words=(),
    designation=Kcmil(854.2),
    wires=Trapezoidal(
        Aluminum1350H19, 15, inch(0.2386), layers=_LAYERS_OF_15, outside_diameter=inch(0.947)
    ),
)

COCKSCOMB = B778(
    code_words=("Cockscomb",),
    designation=Kcmil(900),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1793), layers=_LAYERS_OF_28, outside_diameter=inch(0.987)
    ),
)

RAINIER = B778(
    code_words=("Rainier",),
    designation=Kcmil(918.8),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1811), layers=_LAYERS_OF_28, outside_diameter=inch(0.996)
    ),
)

MAGNOLIA = B778(
    code_words=("Magnolia",),
    designation=Kcmil(954),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1846), layers=_LAYERS_OF_28, outside_diameter=inch(1.014)
    ),
)

HAWKWEED = B778(
    code_words=("Hawkweed",),
    designation=Kcmil(1000),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.189), layers=_LAYERS_OF_28, outside_diameter=inch(1.037)
    ),
)

KCMIL_1020_28 = B778(
    code_words=(),
    designation=Kcmil(1020),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1909), layers=_LAYERS_OF_28, outside_diameter=inch(1.047)
    ),
)

BLUEBELL = B778(
    code_words=("Bluebell",),
    designation=Kcmil(1033.5),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1921), layers=_LAYERS_OF_28, outside_diameter=inch(1.054)
    ),
)

MARIGOLD = B778(
    code_words=("Marigold",),
    designation=Kcmil(1113.1),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.1994), layers=_LAYERS_OF_28, outside_diameter=inch(1.092)
    ),
)

HELENS = B778(
    code_words=("Helens",),
    designation=Kcmil(1123.1),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2003), layers=_LAYERS_OF_28, outside_diameter=inch(1.097)
    ),
)

HAWTHORN = B778(
    code_words=("Hawthorn",),
    designation=Kcmil(1192.5),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2064), layers=_LAYERS_OF_28, outside_diameter=inch(1.128)
    ),
)

KCMIL_1234_2_28 = B778(
    code_words=(),
    designation=Kcmil(1234.2),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2099), layers=_LAYERS_OF_28, outside_diameter=inch(1.147)
    ),
)

NARCISSUS = B778(
    code_words=("Narcissus",),
    designation=Kcmil(1272),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2131), layers=_LAYERS_OF_28, outside_diameter=inch(1.164)
    ),
)

MAZAMA = B778(
    code_words=("Mazama",),
    designation=Kcmil(1346.8),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2193), layers=_LAYERS_OF_28, outside_diameter=inch(1.196)
    ),
)

COLUMBINE = B778(
    code_words=("Columbine",),
    designation=Kcmil(1351.5),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2197), layers=_LAYERS_OF_28, outside_diameter=inch(1.198)
    ),
)

CARNATION = B778(
    code_words=("Carnation",),
    designation=Kcmil(1431),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2261), layers=_LAYERS_OF_28, outside_diameter=inch(1.232)
    ),
)

KCMIL_1467_9_28 = B778(
    code_words=(),
    designation=Kcmil(1467.9),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.229), layers=_LAYERS_OF_28, outside_diameter=inch(1.247)
    ),
)

HOOD = B778(
    code_words=("Hood",),
    designation=Kcmil(1583.2),
    wires=Trapezoidal(
        Aluminum1350H19, 34, equivalent(kcmil(1583.2), 34), layers=3, outside_diameter=inch(1.3)
    ),
)

COREOPSIS = B778(
    code_words=("Coreopsis",),
    designation=Kcmil(1590),
    wires=Trapezoidal(
        Aluminum1350H19, 28, inch(0.2383), layers=_LAYERS_OF_28, outside_diameter=inch(1.296)
    ),
)

KCMIL_1682_7_45 = B778(
    code_words=(),
    designation=Kcmil(1682.7),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.1934), layers=_LAYERS_OF_45, outside_diameter=inch(1.347)
    ),
)

JESSAMINE = B778(
    code_words=("Jessamine",),
    designation=Kcmil(1750),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.1972), layers=_LAYERS_OF_45, outside_diameter=inch(1.372)
    ),
)

WHITNEY = B778(
    code_words=("Whitney",),
    designation=Kcmil(1812.7),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.2007), layers=_LAYERS_OF_45, outside_diameter=inch(1.396)
    ),
)

KCMIL_1954_3_45 = B778(
    code_words=(),
    designation=Kcmil(1954.3),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.2084), layers=_LAYERS_OF_45, outside_diameter=inch(1.447)
    ),
)

COWSLIP = B778(
    code_words=("Cowslip",),
    designation=Kcmil(2000),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.2108), layers=_LAYERS_OF_45, outside_diameter=inch(1.463)
    ),
)

POWELL = B778(
    code_words=("Powell",),
    designation=Kcmil(2093.6),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.2157), layers=_LAYERS_OF_45, outside_diameter=inch(1.496)
    ),
)

KCMIL_2245_4_45 = B778(
    code_words=(),
    designation=Kcmil(2245.4),
    wires=Trapezoidal(
        Aluminum1350H19, 45, inch(0.2234), layers=_LAYERS_OF_45, outside_diameter=inch(1.547)
    ),
)

JEFFERSON = B778(
    code_words=("Jefferson",),
    designation=Kcmil(2388.1),
    wires=Trapezoidal(
        Aluminum1350H19, 46, inch(0.2278), layers=_LAYERS_OF_46, outside_diameter=inch(1.597)
    ),
)

LUPINE = B778(
    code_words=("Lupine",),
    designation=Kcmil(2500),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(2500), 71), layers=5, outside_diameter=inch(1.648)
    ),
)

KCMIL_2514_8_71 = B778(
    code_words=(),
    designation=Kcmil(2514.8),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(2514.8), 71), layers=5, outside_diameter=inch(1.65)
    ),
)

SHASTA = B778(
    code_words=("Shasta",),
    designation=Kcmil(2667.2),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(2667.2), 71), layers=5, outside_diameter=inch(1.7)
    ),
)

KCMIL_2844_5_71 = B778(
    code_words=(),
    designation=Kcmil(2844.5),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(2844.5), 71), layers=5, outside_diameter=inch(1.75)
    ),
)

TRILLIUM = B778(
    code_words=("Trillium",),
    designation=Kcmil(3000),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(3000), 71), layers=5, outside_diameter=inch(1.799)
    ),
)

ADAMS = B778(
    code_words=("Adams",),
    designation=Kcmil(3006.2),
    wires=Trapezoidal(
        Aluminum1350H19, 71, equivalent(kcmil(3006.2), 71), layers=5, outside_diameter=inch(1.8)
    ),
)
