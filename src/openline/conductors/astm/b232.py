"""ASTM B232: ACSR, aluminum 1350 around a coated-steel core."""

from openline.types.conductors.astm import B232
from openline.types.conductors.designations import Gauge, Kcmil, Mm2
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum1350H19, CoatedSteel
from openline.types.units import inch, mm

MM2_12_5_6_1 = B232(
    code_words=(),
    designation=Mm2(12.5),
    outer=Round(Aluminum1350H19, 6, mm(1.63)),
    core=Round(CoatedSteel, 1, mm(1.63)),
)

BANTAM = B232(
    code_words=("Bantam",),
    designation=Kcmil(13.125),
    outer=Round(Aluminum1350H19, 3, inch(0.0661)),
    core=Round(CoatedSteel, 4, inch(0.0661)),
)

TURKEY = B232(
    code_words=("Turkey",),
    designation=Gauge(6),
    outer=Round(Aluminum1350H19, 6, inch(0.0661)),
    core=Round(CoatedSteel, 1, inch(0.0661)),
)

MM2_16_6_1 = B232(
    code_words=(),
    designation=Mm2(16),
    outer=Round(Aluminum1350H19, 6, mm(1.84)),
    core=Round(CoatedSteel, 1, mm(1.84)),
)

THRUSH = B232(
    code_words=("Thrush",),
    designation=Gauge(5),
    outer=Round(Aluminum1350H19, 6, inch(0.0743)),
    core=Round(CoatedSteel, 1, inch(0.0743)),
)

MM2_20_6_1 = B232(
    code_words=(),
    designation=Mm2(20),
    outer=Round(Aluminum1350H19, 6, mm(2.06)),
    core=Round(CoatedSteel, 1, mm(2.06)),
)

MAGPIE = B232(
    code_words=("Magpie",),
    designation=Kcmil(20.87),
    outer=Round(Aluminum1350H19, 3, inch(0.0834)),
    core=Round(CoatedSteel, 4, inch(0.0834)),
)

SWAN = B232(
    code_words=("Swan",),
    designation=Gauge(4),
    outer=Round(Aluminum1350H19, 6, inch(0.0834)),
    core=Round(CoatedSteel, 1, inch(0.0834)),
)

MM2_20_7_1 = B232(
    code_words=(),
    designation=Mm2(20),
    outer=Round(Aluminum1350H19, 7, mm(1.91)),
    core=Round(CoatedSteel, 1, mm(2.55)),
)

SWANATE = B232(
    code_words=("Swanate",),
    designation=Gauge(4),
    outer=Round(Aluminum1350H19, 7, inch(0.0772)),
    core=Round(CoatedSteel, 1, inch(0.1029)),
)

MM2_25_6_1 = B232(
    code_words=(),
    designation=Mm2(25),
    outer=Round(Aluminum1350H19, 6, mm(2.3)),
    core=Round(CoatedSteel, 1, mm(2.3)),
)

SWALLOW = B232(
    code_words=("Swallow",),
    designation=Gauge(3),
    outer=Round(Aluminum1350H19, 6, inch(0.0936)),
    core=Round(CoatedSteel, 1, inch(0.0936)),
)

MM2_25_7_1 = B232(
    code_words=(),
    designation=Mm2(25),
    outer=Round(Aluminum1350H19, 7, mm(2.13)),
    core=Round(CoatedSteel, 1, mm(2.84)),
)

ALBATROSS = B232(
    code_words=("Albatross",),
    designation=Kcmil(54.95),
    outer=Round(Aluminum1350H19, 7, inch(0.0886)),
    core=Round(CoatedSteel, 1, inch(0.1181)),
)

MM2_31_5_6_1 = B232(
    code_words=(),
    designation=Mm2(31.5),
    outer=Round(Aluminum1350H19, 6, mm(2.59)),
    core=Round(CoatedSteel, 1, mm(2.59)),
)

SHRIKE = B232(
    code_words=("Shrike",),
    designation=Kcmil(33.185),
    outer=Round(Aluminum1350H19, 3, inch(0.1052)),
    core=Round(CoatedSteel, 4, inch(0.1052)),
)

SPARROW = B232(
    code_words=("Sparrow",),
    designation=Gauge(2),
    outer=Round(Aluminum1350H19, 6, inch(0.1052)),
    core=Round(CoatedSteel, 1, inch(0.1052)),
)

MM2_31_5_7_1 = B232(
    code_words=(),
    designation=Mm2(31.5),
    outer=Round(Aluminum1350H19, 7, mm(2.39)),
    core=Round(CoatedSteel, 1, mm(3.19)),
)

SPARATE = B232(
    code_words=("Sparate",),
    designation=Gauge(2),
    outer=Round(Aluminum1350H19, 7, inch(0.0974)),
    core=Round(CoatedSteel, 1, inch(0.1299)),
)

MM2_40_6_1 = B232(
    code_words=(),
    designation=Mm2(40),
    outer=Round(Aluminum1350H19, 6, mm(2.91)),
    core=Round(CoatedSteel, 1, mm(2.91)),
)

ROBIN = B232(
    code_words=("Robin",),
    designation=Gauge(1),
    outer=Round(Aluminum1350H19, 6, inch(0.1181)),
    core=Round(CoatedSteel, 1, inch(0.1181)),
)

MM2_40_8_1 = B232(
    code_words=(),
    designation=Mm2(40),
    outer=Round(Aluminum1350H19, 8, mm(2.52)),
    core=Round(CoatedSteel, 1, mm(4.2)),
)

GROUSE = B232(
    code_words=("Grouse",),
    designation=Kcmil(80),
    outer=Round(Aluminum1350H19, 8, inch(0.1)),
    core=Round(CoatedSteel, 1, inch(0.167)),
)

MM2_50_6_1 = B232(
    code_words=(),
    designation=Mm2(50),
    outer=Round(Aluminum1350H19, 6, mm(3.26)),
    core=Round(CoatedSteel, 1, mm(3.26)),
)

SNIPE = B232(
    code_words=("Snipe",),
    designation=Kcmil(52.77),
    outer=Round(Aluminum1350H19, 3, inch(0.1326)),
    core=Round(CoatedSteel, 4, inch(0.1326)),
)

RAVEN = B232(
    code_words=("Raven",),
    designation=Gauge(0),
    outer=Round(Aluminum1350H19, 6, inch(0.1327)),
    core=Round(CoatedSteel, 1, inch(0.1327)),
)

SHOEBILL = B232(
    code_words=("Shoebill",),
    designation=Kcmil(57.5),
    outer=Round(Aluminum1350H19, 3, inch(0.1384)),
    core=Round(CoatedSteel, 4, inch(0.1384)),
)

MM2_63_6_1 = B232(
    code_words=(),
    designation=Mm2(63),
    outer=Round(Aluminum1350H19, 6, mm(3.66)),
    core=Round(CoatedSteel, 1, mm(3.66)),
)

LOON = B232(
    code_words=("Loon",),
    designation=Kcmil(66.54),
    outer=Round(Aluminum1350H19, 3, inch(0.1489)),
    core=Round(CoatedSteel, 4, inch(0.1489)),
)

QUAIL = B232(
    code_words=("Quail",),
    designation=Gauge(-1),
    outer=Round(Aluminum1350H19, 6, inch(0.1489)),
    core=Round(CoatedSteel, 1, inch(0.1489)),
)

MM2_50_12_7 = B232(
    code_words=(),
    designation=Mm2(50),
    outer=Round(Aluminum1350H19, 12, mm(2.3)),
    core=Round(CoatedSteel, 7, mm(2.3)),
)

PETREL = B232(
    code_words=("Petrel",),
    designation=Kcmil(101.8),
    outer=Round(Aluminum1350H19, 12, inch(0.0921)),
    core=Round(CoatedSteel, 7, inch(0.0921)),
)

BOBWHITE = B232(
    code_words=("Bobwhite",),
    designation=Gauge(-1),
    outer=Round(Aluminum1350H19, 7, inch(0.1379)),
    core=Round(CoatedSteel, 1, inch(0.1839)),
)

MM2_56_12_7 = B232(
    code_words=(),
    designation=Mm2(56),
    outer=Round(Aluminum1350H19, 12, mm(2.44)),
    core=Round(CoatedSteel, 7, mm(2.44)),
)

MINORCA = B232(
    code_words=("Minorca",),
    designation=Kcmil(110.8),
    outer=Round(Aluminum1350H19, 12, inch(0.0961)),
    core=Round(CoatedSteel, 7, inch(0.0961)),
)

MM2_80_6_1 = B232(
    code_words=(),
    designation=Mm2(80),
    outer=Round(Aluminum1350H19, 6, mm(4.12)),
    core=Round(CoatedSteel, 1, mm(4.12)),
)

PIGEON = B232(
    code_words=("Pigeon",),
    designation=Gauge(-2),
    outer=Round(Aluminum1350H19, 6, inch(0.1672)),
    core=Round(CoatedSteel, 1, inch(0.1672)),
)

MM2_63_12_7 = B232(
    code_words=(),
    designation=Mm2(63),
    outer=Round(Aluminum1350H19, 12, mm(2.59)),
    core=Round(CoatedSteel, 7, mm(2.59)),
)

LEGHORN = B232(
    code_words=("Leghorn",),
    designation=Kcmil(134.6),
    outer=Round(Aluminum1350H19, 12, inch(0.1059)),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

MM2_71_12_7 = B232(
    code_words=(),
    designation=Mm2(71),
    outer=Round(Aluminum1350H19, 12, mm(2.74)),
    core=Round(CoatedSteel, 7, mm(2.74)),
)

BARBET = B232(
    code_words=("Barbet",),
    designation=Gauge(-3),
    outer=Round(Aluminum1350H19, 18, inch(0.1084)),
    core=Round(CoatedSteel, 1, inch(0.1084)),
)

VULTURE = B232(
    code_words=("Vulture",),
    designation=Gauge(-3),
    outer=Round(Aluminum1350H19, 5, inch(0.2057)),
    core=Round(CoatedSteel, 1, inch(0.1371)),
)

MM2_100_6_1 = B232(
    code_words=(),
    designation=Mm2(100),
    outer=Round(Aluminum1350H19, 6, mm(4.61)),
    core=Round(CoatedSteel, 1, mm(4.61)),
)

JAEGER = B232(
    code_words=("Jaeger",),
    designation=Kcmil(228.2),
    outer=Round(Aluminum1350H19, 18, inch(0.1126)),
    core=Round(CoatedSteel, 1, inch(0.1126)),
)

PENGUIN = B232(
    code_words=("Penguin",),
    designation=Gauge(-3),
    outer=Round(Aluminum1350H19, 6, inch(0.1878)),
    core=Round(CoatedSteel, 1, inch(0.1878)),
)

MM2_80_12_7 = B232(
    code_words=(),
    designation=Mm2(80),
    outer=Round(Aluminum1350H19, 12, mm(2.91)),
    core=Round(CoatedSteel, 7, mm(2.91)),
)

GUINEA = B232(
    code_words=("Guinea",),
    designation=Kcmil(159),
    outer=Round(Aluminum1350H19, 12, inch(0.1151)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

AUK = B232(
    code_words=("Auk",),
    designation=Kcmil(203),
    outer=Round(Aluminum1350H19, 8, inch(0.1593)),
    core=Round(CoatedSteel, 7, inch(0.0885)),
)

MM2_125_18_1 = B232(
    code_words=(),
    designation=Mm2(125),
    outer=Round(Aluminum1350H19, 18, mm(2.97)),
    core=Round(CoatedSteel, 1, mm(2.97)),
)

MM2_125_24_7 = B232(
    code_words=(),
    designation=Mm2(125),
    outer=Round(Aluminum1350H19, 24, mm(2.58)),
    core=Round(CoatedSteel, 7, mm(1.72)),
)

DOTTEREL = B232(
    code_words=("Dotterel",),
    designation=Kcmil(176.9),
    outer=Round(Aluminum1350H19, 12, inch(0.1214)),
    core=Round(CoatedSteel, 7, inch(0.1214)),
)

MM2_90_12_7 = B232(
    code_words=(),
    designation=Mm2(90),
    outer=Round(Aluminum1350H19, 12, mm(3.09)),
    core=Round(CoatedSteel, 7, mm(3.09)),
)

WAXWING = B232(
    code_words=("Waxwing",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 18, inch(0.1217)),
    core=Round(CoatedSteel, 1, inch(0.1217)),
)

EIDER = B232(
    code_words=("Eider",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 45, inch(0.077)),
    core=Round(CoatedSteel, 7, inch(0.0513)),
)

MM2_125_26_7 = B232(
    code_words=(),
    designation=Mm2(125),
    outer=Round(Aluminum1350H19, 26, mm(2.47)),
    core=Round(CoatedSteel, 7, mm(1.92)),
)

MM2_140_18_1 = B232(
    code_words=(),
    designation=Mm2(140),
    outer=Round(Aluminum1350H19, 18, mm(3.15)),
    core=Round(CoatedSteel, 1, mm(3.15)),
)

SPOONBILL = B232(
    code_words=("Spoonbill",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 22, inch(0.1101)),
    core=Round(CoatedSteel, 7, inch(0.0612)),
)

SCAUP = B232(
    code_words=("Scaup",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 24, inch(0.1054)),
    core=Round(CoatedSteel, 7, inch(0.0703)),
)

OWL = B232(
    code_words=("Owl",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 6, inch(0.2109)),
    core=Round(CoatedSteel, 7, inch(0.0703)),
)

DORKING = B232(
    code_words=("Dorking",),
    designation=Kcmil(190.8),
    outer=Round(Aluminum1350H19, 12, inch(0.1261)),
    core=Round(CoatedSteel, 7, inch(0.1261)),
)

PARTRIDGE = B232(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 26, inch(0.1013)),
    core=Round(CoatedSteel, 7, inch(0.0788)),
)

MM2_100_12_7 = B232(
    code_words=(),
    designation=Mm2(100),
    outer=Round(Aluminum1350H19, 12, mm(3.26)),
    core=Round(CoatedSteel, 7, mm(3.26)),
)

MM2_140_24_7 = B232(
    code_words=(),
    designation=Mm2(140),
    outer=Round(Aluminum1350H19, 24, mm(2.73)),
    core=Round(CoatedSteel, 7, mm(1.82)),
)

PHOEBE = B232(
    code_words=("Phoebe",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350H19, 18, inch(0.1291)),
    core=Round(CoatedSteel, 1, inch(0.1291)),
)

MM2_140_26_7 = B232(
    code_words=(),
    designation=Mm2(140),
    outer=Round(Aluminum1350H19, 26, mm(2.62)),
    core=Round(CoatedSteel, 7, mm(2.04)),
)

JUNCO = B232(
    code_words=("Junco",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 30, inch(0.0943)),
    core=Round(CoatedSteel, 7, inch(0.0943)),
)

MM2_160_18_1 = B232(
    code_words=(),
    designation=Mm2(160),
    outer=Round(Aluminum1350H19, 18, mm(3.36)),
    core=Round(CoatedSteel, 1, mm(3.36)),
)

COCHIN = B232(
    code_words=("Cochin",),
    designation=Kcmil(211.3),
    outer=Round(Aluminum1350H19, 12, inch(0.1327)),
    core=Round(CoatedSteel, 7, inch(0.1327)),
)

GADWALL = B232(
    code_words=("Gadwall",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350H19, 24, inch(0.1118)),
    core=Round(CoatedSteel, 7, inch(0.0745)),
)

OSTRICH = B232(
    code_words=("Ostrich",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350H19, 26, inch(0.1074)),
    core=Round(CoatedSteel, 7, inch(0.0835)),
)

MERLIN = B232(
    code_words=("Merlin",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 18, inch(0.1367)),
    core=Round(CoatedSteel, 1, inch(0.1367)),
)

MM2_160_24_7 = B232(
    code_words=(),
    designation=Mm2(160),
    outer=Round(Aluminum1350H19, 24, mm(2.91)),
    core=Round(CoatedSteel, 7, mm(1.94)),
)

TROGON = B232(
    code_words=("Trogon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 20, inch(0.1297)),
    core=Round(CoatedSteel, 7, inch(0.0576)),
)

HUMMINGBIRD = B232(
    code_words=("Hummingbird",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 45, inch(0.0865)),
    core=Round(CoatedSteel, 7, inch(0.0577)),
)

MM2_160_26_7 = B232(
    code_words=(),
    designation=Mm2(160),
    outer=Round(Aluminum1350H19, 26, mm(2.8)),
    core=Round(CoatedSteel, 7, mm(2.18)),
)

WOODCOCK = B232(
    code_words=("Woodcock",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 22, inch(0.1237)),
    core=Round(CoatedSteel, 7, inch(0.0687)),
)

PIPER = B232(
    code_words=("Piper",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350H19, 30, inch(0.1)),
    core=Round(CoatedSteel, 7, inch(0.1)),
)

MM2_100_16_19 = B232(
    code_words=(),
    designation=Mm2(100),
    outer=Round(Aluminum1350H19, 16, mm(2.82)),
    core=Round(CoatedSteel, 19, mm(2.44)),
)

MM2_180_18_1 = B232(
    code_words=(),
    designation=Mm2(180),
    outer=Round(Aluminum1350H19, 18, mm(3.57)),
    core=Round(CoatedSteel, 1, mm(3.57)),
)

WIDGEON = B232(
    code_words=("Widgeon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 24, inch(0.1184)),
    core=Round(CoatedSteel, 7, inch(0.0789)),
)

BRAHMA = B232(
    code_words=("Brahma",),
    designation=Kcmil(203.2),
    outer=Round(Aluminum1350H19, 16, inch(0.1127)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

MM2_160_30_7 = B232(
    code_words=(),
    designation=Mm2(160),
    outer=Round(Aluminum1350H19, 30, mm(2.61)),
    core=Round(CoatedSteel, 7, mm(2.61)),
)

LINNET = B232(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 26, inch(0.1137)),
    core=Round(CoatedSteel, 7, inch(0.0884)),
)

MM2_180_24_7 = B232(
    code_words=(),
    designation=Mm2(180),
    outer=Round(Aluminum1350H19, 24, mm(3.09)),
    core=Round(CoatedSteel, 7, mm(2.06)),
)

MM2_180_26_7 = B232(
    code_words=(),
    designation=Mm2(180),
    outer=Round(Aluminum1350H19, 26, mm(2.97)),
    core=Round(CoatedSteel, 7, mm(2.31)),
)

ORIOLE = B232(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 30, inch(0.1059)),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

MM2_200_18_1 = B232(
    code_words=(),
    designation=Mm2(200),
    outer=Round(Aluminum1350H19, 18, mm(3.76)),
    core=Round(CoatedSteel, 1, mm(3.76)),
)

ERNE = B232(
    code_words=("Erne",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 42, inch(0.0973)),
    core=Round(CoatedSteel, 7, inch(0.0541)),
)

CHICKADEE = B232(
    code_words=("Chickadee",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 18, inch(0.1486)),
    core=Round(CoatedSteel, 1, inch(0.1486)),
)

PTARMIGAN = B232(
    code_words=("Ptarmigan",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 20, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.0627)),
)

LONGSPUR = B232(
    code_words=("Longspur",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 45, inch(0.094)),
    core=Round(CoatedSteel, 7, inch(0.0627)),
)

STORK = B232(
    code_words=("Stork",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 22, inch(0.1344)),
    core=Round(CoatedSteel, 7, inch(0.0747)),
)

MM2_180_30_7 = B232(
    code_words=(),
    designation=Mm2(180),
    outer=Round(Aluminum1350H19, 30, mm(2.76)),
    core=Round(CoatedSteel, 7, mm(2.76)),
)

MM2_200_24_7 = B232(
    code_words=(),
    designation=Mm2(200),
    outer=Round(Aluminum1350H19, 24, mm(3.26)),
    core=Round(CoatedSteel, 7, mm(2.17)),
)

BRANT = B232(
    code_words=("Brant",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1287)),
    core=Round(CoatedSteel, 7, inch(0.0858)),
)

MM2_200_26_7 = B232(
    code_words=(),
    designation=Mm2(200),
    outer=Round(Aluminum1350H19, 26, mm(3.13)),
    core=Round(CoatedSteel, 7, mm(2.43)),
)

IBIS = B232(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1236)),
    core=Round(CoatedSteel, 7, inch(0.0961)),
)

MM2_224_18_1 = B232(
    code_words=(),
    designation=Mm2(224),
    outer=Round(Aluminum1350H19, 18, mm(3.98)),
    core=Round(CoatedSteel, 1, mm(3.98)),
)

MM2_200_30_7 = B232(
    code_words=(),
    designation=Mm2(200),
    outer=Round(Aluminum1350H19, 30, mm(2.91)),
    core=Round(CoatedSteel, 7, mm(2.91)),
)

LARK = B232(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1151)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

MM2_224_24_7 = B232(
    code_words=(),
    designation=Mm2(224),
    outer=Round(Aluminum1350H19, 24, mm(3.45)),
    core=Round(CoatedSteel, 7, mm(2.3)),
)

KESTREL = B232(
    code_words=("Kestrel",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 42, inch(0.1066)),
    core=Round(CoatedSteel, 7, inch(0.0592)),
)

PELICAN = B232(
    code_words=("Pelican",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 18, inch(0.1628)),
    core=Round(CoatedSteel, 1, inch(0.1628)),
)

TAILORBIRD = B232(
    code_words=("Tailorbird",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 20, inch(0.1544)),
    core=Round(CoatedSteel, 7, inch(0.0686)),
)

JACKDAW = B232(
    code_words=("Jackdaw",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 45, inch(0.103)),
    core=Round(CoatedSteel, 7, inch(0.0687)),
)

MM2_224_26_7 = B232(
    code_words=(),
    designation=Mm2(224),
    outer=Round(Aluminum1350H19, 26, mm(3.31)),
    core=Round(CoatedSteel, 7, mm(2.57)),
)

PINTAIL = B232(
    code_words=("Pintail",),
    designation=Kcmil(419),
    outer=Round(Aluminum1350H19, 30, inch(0.1182)),
    core=Round(CoatedSteel, 7, inch(0.1182)),
)

MM2_250_18_1 = B232(
    code_words=(),
    designation=Mm2(250),
    outer=Round(Aluminum1350H19, 18, mm(4.21)),
    core=Round(CoatedSteel, 1, mm(4.21)),
)

TOUCAN = B232(
    code_words=("Toucan",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 22, inch(0.1472)),
    core=Round(CoatedSteel, 7, inch(0.0818)),
)

FLICKER = B232(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 24, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.094)),
)

MM2_224_30_7 = B232(
    code_words=(),
    designation=Mm2(224),
    outer=Round(Aluminum1350H19, 30, mm(3.08)),
    core=Round(CoatedSteel, 7, mm(3.08)),
)

NIGHTINGALE = B232(
    code_words=("Nightingale",),
    designation=Kcmil(517),
    outer=Round(Aluminum1350H19, 20, inch(0.1608)),
    core=Round(CoatedSteel, 7, inch(0.0715)),
)

HAWK = B232(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 26, inch(0.1354)),
    core=Round(CoatedSteel, 7, inch(0.1053)),
)

MM2_250_24_7 = B232(
    code_words=(),
    designation=Mm2(250),
    outer=Round(Aluminum1350H19, 24, mm(3.64)),
    core=Round(CoatedSteel, 7, mm(2.43)),
)

MM2_250_26_7 = B232(
    code_words=(),
    designation=Mm2(250),
    outer=Round(Aluminum1350H19, 26, mm(3.5)),
    core=Round(CoatedSteel, 7, mm(2.72)),
)

MM2_280_18_1 = B232(
    code_words=(),
    designation=Mm2(280),
    outer=Round(Aluminum1350H19, 18, mm(4.45)),
    core=Round(CoatedSteel, 1, mm(4.45)),
)

BLACKBIRD = B232(
    code_words=("Blackbird",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1151)),
    core=Round(CoatedSteel, 7, inch(0.0639)),
)

OSPREY = B232(
    code_words=("Osprey",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 18, inch(0.1758)),
    core=Round(CoatedSteel, 1, inch(0.1758)),
)

HEN = B232(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 30, inch(0.1261)),
    core=Round(CoatedSteel, 7, inch(0.1261)),
)

RHEA = B232(
    code_words=("Rhea",),
    designation=Kcmil(286.2),
    outer=Round(Aluminum1350H19, 18, inch(0.1261)),
    core=Round(CoatedSteel, 19, inch(0.1261)),
)

TODY = B232(
    code_words=("Tody",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 20, inch(0.1668)),
    core=Round(CoatedSteel, 7, inch(0.0741)),
)

SUNBIRD = B232(
    code_words=("Sunbird",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1112)),
    core=Round(CoatedSteel, 7, inch(0.0741)),
)

MM2_250_30_7 = B232(
    code_words=(),
    designation=Mm2(250),
    outer=Round(Aluminum1350H19, 30, mm(3.26)),
    core=Round(CoatedSteel, 7, mm(3.26)),
)

SAPSUCKER = B232(
    code_words=("Sapsucker",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 22, inch(0.159)),
    core=Round(CoatedSteel, 7, inch(0.0883)),
)

HERON = B232(
    code_words=("Heron",),
    designation=Kcmil(500),
    outer=Round(Aluminum1350H19, 30, inch(0.1291)),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

MM2_280_24_7 = B232(
    code_words=(),
    designation=Mm2(280),
    outer=Round(Aluminum1350H19, 24, mm(3.85)),
    core=Round(CoatedSteel, 7, mm(2.57)),
)

PARAKEET = B232(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1523)),
    core=Round(CoatedSteel, 7, inch(0.1015)),
)

MM2_280_26_7 = B232(
    code_words=(),
    designation=Mm2(280),
    outer=Round(Aluminum1350H19, 26, mm(3.7)),
    core=Round(CoatedSteel, 7, mm(2.88)),
)

DOVE = B232(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1463)),
    core=Round(CoatedSteel, 7, inch(0.1138)),
)

SANDPIPER = B232(
    code_words=("Sandpiper",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 45, inch(0.116)),
    core=Round(CoatedSteel, 7, inch(0.0773)),
)

SWIFT = B232(
    code_words=("Swift",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 36, inch(0.1329)),
    core=Round(CoatedSteel, 1, inch(0.1329)),
)

MM2_315_18_1 = B232(
    code_words=(),
    designation=Mm2(315),
    outer=Round(Aluminum1350H19, 18, mm(4.72)),
    core=Round(CoatedSteel, 1, mm(4.72)),
)

PIPIT = B232(
    code_words=("Pipit",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 42, inch(0.1231)),
    core=Round(CoatedSteel, 7, inch(0.0684)),
)

KINGBIRD = B232(
    code_words=("Kingbird",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 18, inch(0.188)),
    core=Round(CoatedSteel, 1, inch(0.188)),
)

TURACOS = B232(
    code_words=("Turacos",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 20, inch(0.1783)),
    core=Round(CoatedSteel, 7, inch(0.0792)),
)

KILLDEER = B232(
    code_words=("Killdeer",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 45, inch(0.1189)),
    core=Round(CoatedSteel, 7, inch(0.0793)),
)

MM2_280_30_7 = B232(
    code_words=(),
    designation=Mm2(280),
    outer=Round(Aluminum1350H19, 30, mm(3.45)),
    core=Round(CoatedSteel, 7, mm(3.45)),
)

DUCK = B232(
    code_words=("Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 54, inch(0.1058)),
    core=Round(CoatedSteel, 7, inch(0.1058)),
)

PEACOCK = B232(
    code_words=("Peacock",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 24, inch(0.1588)),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

EAGLE = B232(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1362)),
    core=Round(CoatedSteel, 7, inch(0.1362)),
)

GOLDFINCH = B232(
    code_words=("Goldfinch",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 22, inch(0.17)),
    core=Round(CoatedSteel, 7, inch(0.0944)),
)

SQUAB = B232(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 26, inch(0.1525)),
    core=Round(CoatedSteel, 7, inch(0.1186)),
)

MM2_315_24_7 = B232(
    code_words=(),
    designation=Mm2(315),
    outer=Round(Aluminum1350H19, 24, mm(4.09)),
    core=Round(CoatedSteel, 7, mm(2.73)),
)

CROSSBILL = B232(
    code_words=("Crossbill",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 45, inch(0.1217)),
    core=Round(CoatedSteel, 7, inch(0.0811)),
)

GOOSE = B232(
    code_words=("Goose",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 54, inch(0.1085)),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

ROOK = B232(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 24, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

MM2_315_26_7 = B232(
    code_words=(),
    designation=Mm2(315),
    outer=Round(Aluminum1350H19, 26, mm(3.93)),
    core=Round(CoatedSteel, 7, mm(3.06)),
)

GROSBEAK = B232(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 26, inch(0.1564)),
    core=Round(CoatedSteel, 7, inch(0.1216)),
)

TEAL = B232(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 30, inch(0.142)),
    core=Round(CoatedSteel, 19, inch(0.0852)),
)

WOOD_DUCK = B232(
    code_words=("Wood Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 30, inch(0.142)),
    core=Round(CoatedSteel, 7, inch(0.142)),
)

GULL = B232(
    code_words=("Gull",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 54, inch(0.1111)),
    core=Round(CoatedSteel, 7, inch(0.1111)),
)

FLAMINGO = B232(
    code_words=("Flamingo",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 24, inch(0.1667)),
    core=Round(CoatedSteel, 7, inch(0.1111)),
)

GREBE = B232(
    code_words=("Grebe",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1261)),
    core=Round(CoatedSteel, 7, inch(0.0841)),
)

MM2_315_30_19 = B232(
    code_words=(),
    designation=Mm2(315),
    outer=Round(Aluminum1350H19, 30, mm(3.66)),
    core=Round(CoatedSteel, 19, mm(2.2)),
)

GANNET = B232(
    code_words=("Gannet",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 26, inch(0.1601)),
    core=Round(CoatedSteel, 7, inch(0.1245)),
)

EGRET = B232(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 30, inch(0.1456)),
    core=Round(CoatedSteel, 19, inch(0.0874)),
)

SCOTER = B232(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 30, inch(0.1456)),
    core=Round(CoatedSteel, 7, inch(0.1456)),
)

MM2_355_24_7 = B232(
    code_words=(),
    designation=Mm2(355),
    outer=Round(Aluminum1350H19, 24, mm(4.34)),
    core=Round(CoatedSteel, 7, mm(2.89)),
)

CROW = B232(
    code_words=("Crow",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 54, mm(2.92)),
    core=Round(CoatedSteel, 7, mm(2.92)),
)

STILT = B232(
    code_words=("Stilt",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1727)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

MM2_355_26_7 = B232(
    code_words=(),
    designation=Mm2(355),
    outer=Round(Aluminum1350H19, 26, mm(4.17)),
    core=Round(CoatedSteel, 7, mm(3.24)),
)

COOT = B232(
    code_words=("Coot",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 36, inch(0.1486)),
    core=Round(CoatedSteel, 1, inch(0.1486)),
)

STARLING = B232(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1659)),
    core=Round(CoatedSteel, 7, inch(0.129)),
)

MACAW = B232(
    code_words=("Macaw",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 42, inch(0.1376)),
    core=Round(CoatedSteel, 7, inch(0.0764)),
)

TERN = B232(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 45, inch(0.1329)),
    core=Round(CoatedSteel, 7, inch(0.0886)),
)

TURBIT = B232(
    code_words=("Turbit",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 20, inch(0.1994)),
    core=Round(CoatedSteel, 7, inch(0.0886)),
)

MM2_355_30_19 = B232(
    code_words=(),
    designation=Mm2(355),
    outer=Round(Aluminum1350H19, 30, mm(3.88)),
    core=Round(CoatedSteel, 19, mm(2.33)),
)

PUFFIN = B232(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 22, inch(0.1901)),
    core=Round(CoatedSteel, 7, inch(0.1056)),
)

REDWING = B232(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1544)),
    core=Round(CoatedSteel, 19, inch(0.0926)),
)

BUTEO = B232(
    code_words=("Buteo",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1544)),
    core=Round(CoatedSteel, 7, inch(0.1544)),
)

MM2_400_24_7 = B232(
    code_words=(),
    designation=Mm2(400),
    outer=Round(Aluminum1350H19, 24, mm(4.61)),
    core=Round(CoatedSteel, 7, mm(3.07)),
)

CONDOR = B232(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 54, inch(0.1213)),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

CUCKOO = B232(
    code_words=("Cuckoo",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 24, inch(0.182)),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

MM2_400_26_7 = B232(
    code_words=(),
    designation=Mm2(400),
    outer=Round(Aluminum1350H19, 26, mm(4.43)),
    core=Round(CoatedSteel, 7, mm(3.45)),
)

DRAKE = B232(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 26, inch(0.1749)),
    core=Round(CoatedSteel, 7, inch(0.136)),
)

WILLET = B232(
    code_words=("Willet",),
    designation=Kcmil(874.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1394)),
    core=Round(CoatedSteel, 7, inch(0.0929)),
)

MM2_450_45_7 = B232(
    code_words=(),
    designation=Mm2(450),
    outer=Round(Aluminum1350H19, 45, mm(3.57)),
    core=Round(CoatedSteel, 7, mm(2.38)),
)

RUDDY = B232(
    code_words=("Ruddy",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 45, inch(0.1414)),
    core=Round(CoatedSteel, 7, inch(0.0943)),
)

TURNSTONE = B232(
    code_words=("Turnstone",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 20, inch(0.2121)),
    core=Round(CoatedSteel, 7, inch(0.0943)),
)

MM2_400_30_19 = B232(
    code_words=(),
    designation=Mm2(400),
    outer=Round(Aluminum1350H19, 30, mm(4.12)),
    core=Round(CoatedSteel, 19, mm(2.47)),
)

MALLARD = B232(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 30, inch(0.1628)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

SKIMMER = B232(
    code_words=("Skimmer",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 30, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1628)),
)

CATBIRD = B232(
    code_words=("Catbird",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 36, inch(0.1628)),
    core=Round(CoatedSteel, 1, inch(0.1628)),
)

CRANE = B232(
    code_words=("Crane",),
    designation=Kcmil(874.5),
    outer=Round(Aluminum1350H19, 54, mm(3.23)),
    core=Round(CoatedSteel, 7, mm(3.23)),
)

PHOENIX = B232(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 42, inch(0.1507)),
    core=Round(CoatedSteel, 7, inch(0.0837)),
)

MM2_450_54_7 = B232(
    code_words=(),
    designation=Mm2(450),
    outer=Round(Aluminum1350H19, 54, mm(3.26)),
    core=Round(CoatedSteel, 7, mm(3.26)),
)

REDSTART = B232(
    code_words=("Redstart",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 24, inch(0.1936)),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

CANARY = B232(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 54, inch(0.1291)),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

CORNCRAKE = B232(
    code_words=("Corncrake",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 20, inch(0.2184)),
    core=Round(CoatedSteel, 7, inch(0.0971)),
)

RAIL = B232(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 45, inch(0.1456)),
    core=Round(CoatedSteel, 7, inch(0.0971)),
)

TOWHEE = B232(
    code_words=("Towhee",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 48, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.1097)),
)

MM2_500_45_7 = B232(
    code_words=(),
    designation=Mm2(500),
    outer=Round(Aluminum1350H19, 45, mm(3.76)),
    core=Round(CoatedSteel, 7, mm(2.51)),
)

TANAGER = B232(
    code_words=("Tanager",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 36, inch(0.1694)),
    core=Round(CoatedSteel, 1, inch(0.1694)),
)

CARDINAL = B232(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 54, inch(0.1329)),
    core=Round(CoatedSteel, 7, inch(0.1329)),
)

REDBIRD = B232(
    code_words=("Redbird",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 24, inch(0.1994)),
    core=Round(CoatedSteel, 7, inch(0.1329)),
)

SNOWBIRD = B232(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1569)),
    core=Round(CoatedSteel, 7, inch(0.0872)),
)

ORTOLAN = B232(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1515)),
    core=Round(CoatedSteel, 7, inch(0.101)),
)

BALDPATE = B232(
    code_words=("Baldpate",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 30, inch(0.1732)),
    core=Round(CoatedSteel, 7, inch(0.1732)),
)

MM2_500_54_7 = B232(
    code_words=(),
    designation=Mm2(500),
    outer=Round(Aluminum1350H19, 54, mm(3.43)),
    core=Round(CoatedSteel, 7, mm(3.43)),
)

VIREO = B232(
    code_words=("Vireo",),
    designation=Kcmil(1027.4),
    outer=Round(Aluminum1350H19, 48, inch(0.1463)),
    core=Round(CoatedSteel, 7, inch(0.1138)),
)

WHOOPER = B232(
    code_words=("Whooper",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1467)),
    core=Round(CoatedSteel, 7, inch(0.1141)),
)

CURLEW = B232(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1383)),
    core=Round(CoatedSteel, 7, inch(0.1383)),
)

AVOCET = B232(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 42, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.0904)),
)

CANVASBACK = B232(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 30, inch(0.1783)),
    core=Round(CoatedSteel, 19, inch(0.107)),
)

MERGANSER = B232(
    code_words=("Merganser",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 30, inch(0.1783)),
    core=Round(CoatedSteel, 7, inch(0.1783)),
)

MM2_560_45_7 = B232(
    code_words=(),
    designation=Mm2(560),
    outer=Round(Aluminum1350H19, 45, mm(3.98)),
    core=Round(CoatedSteel, 7, mm(2.65)),
)

BLUEJAY = B232(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 45, inch(0.1573)),
    core=Round(CoatedSteel, 7, inch(0.1049)),
)

BULLFINCH = B232(
    code_words=("Bullfinch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 48, inch(0.1523)),
    core=Round(CoatedSteel, 7, inch(0.1185)),
)

MM2_560_54_19 = B232(
    code_words=(),
    designation=Mm2(560),
    outer=Round(Aluminum1350H19, 54, mm(3.63)),
    core=Round(CoatedSteel, 19, mm(2.18)),
)

OXBIRD = B232(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1685)),
    core=Round(CoatedSteel, 7, inch(0.0936)),
)

FINCH = B232(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 54, inch(0.1436)),
    core=Round(CoatedSteel, 19, inch(0.0862)),
)

BUNTING = B232(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

CORMORANT = B232(
    code_words=("Cormorant",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1576)),
    core=Round(CoatedSteel, 7, inch(0.1226)),
)

SKYLARK = B232(
    code_words=("Skylark",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 36, inch(0.188)),
    core=Round(CoatedSteel, 1, inch(0.188)),
)

MM2_630_45_7 = B232(
    code_words=(),
    designation=Mm2(630),
    outer=Round(Aluminum1350H19, 45, mm(4.22)),
    core=Round(CoatedSteel, 7, mm(2.81)),
)

SCISSORTAIL = B232(
    code_words=("Scissortail",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 42, inch(0.174)),
    core=Round(CoatedSteel, 7, inch(0.0967)),
)

GRACKLE = B232(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1486)),
    core=Round(CoatedSteel, 19, inch(0.0892)),
)

BITTERN = B232(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 45, inch(0.1681)),
    core=Round(CoatedSteel, 7, inch(0.1121)),
)

DIVER = B232(
    code_words=("Diver",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 48, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1266)),
)

MM2_630_54_19 = B232(
    code_words=(),
    designation=Mm2(630),
    outer=Round(Aluminum1350H19, 54, mm(3.85)),
    core=Round(CoatedSteel, 19, mm(2.31)),
)

RINGDOVE = B232(
    code_words=("Ringdove",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1794)),
    core=Round(CoatedSteel, 7, inch(0.0997)),
)

PHEASANT = B232(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 54, inch(0.1535)),
    core=Round(CoatedSteel, 19, inch(0.0921)),
)

DIPPER = B232(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1733)),
    core=Round(CoatedSteel, 7, inch(0.1155)),
)

KCMIL_1351_5_48_7 = B232(
    code_words=(),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1678)),
    core=Round(CoatedSteel, 7, inch(0.1305)),
)

FRIGATE = B232(
    code_words=("Frigate",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 22, inch(0.2479)),
    core=Round(CoatedSteel, 7, inch(0.1377)),
)

MM2_710_45_7 = B232(
    code_words=(),
    designation=Mm2(710),
    outer=Round(Aluminum1350H19, 45, mm(4.48)),
    core=Round(CoatedSteel, 7, mm(2.99)),
)

POPINJAY = B232(
    code_words=("Popinjay",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 42, inch(0.1846)),
    core=Round(CoatedSteel, 7, inch(0.1026)),
)

MARTIN = B232(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1582)),
    core=Round(CoatedSteel, 19, inch(0.0949)),
)

BOBOLINK = B232(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 45, inch(0.1783)),
    core=Round(CoatedSteel, 7, inch(0.1189)),
)

WAGTAIL = B232(
    code_words=("Wagtail",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 48, inch(0.1727)),
    core=Round(CoatedSteel, 7, inch(0.1343)),
)

MM2_710_54_19 = B232(
    code_words=(),
    designation=Mm2(710),
    outer=Round(Aluminum1350H19, 54, mm(4.09)),
    core=Round(CoatedSteel, 19, mm(2.45)),
)

PLOVER = B232(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 54, inch(0.1628)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

NUTHATCH = B232(
    code_words=("Nuthatch",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1832)),
    core=Round(CoatedSteel, 7, inch(0.1221)),
)

RATITE = B232(
    code_words=("Ratite",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 42, inch(0.1946)),
    core=Round(CoatedSteel, 7, inch(0.1081)),
)

MM2_800_45_7 = B232(
    code_words=(),
    designation=Mm2(800),
    outer=Round(Aluminum1350H19, 45, mm(4.76)),
    core=Round(CoatedSteel, 7, mm(3.17)),
)

LAPWING = B232(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 45, inch(0.188)),
    core=Round(CoatedSteel, 7, inch(0.1253)),
)

PARROT = B232(
    code_words=("Parrot",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1672)),
    core=Round(CoatedSteel, 19, inch(0.1003)),
)

HORNBILL = B232(
    code_words=("Hornbill",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 48, inch(0.182)),
    core=Round(CoatedSteel, 7, inch(0.1416)),
)

MM2_800_54_19 = B232(
    code_words=(),
    designation=Mm2(800),
    outer=Round(Aluminum1350H19, 54, mm(4.34)),
    core=Round(CoatedSteel, 19, mm(2.6)),
)

FALCON = B232(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 54, inch(0.1716)),
    core=Round(CoatedSteel, 19, inch(0.103)),
)

MM2_900_72_7 = B232(
    code_words=(),
    designation=Mm2(900),
    outer=Round(Aluminum1350H19, 72, mm(3.99)),
    core=Round(CoatedSteel, 7, mm(2.66)),
)

SMEW = B232(
    code_words=("Smew",),
    designation=Kcmil(1780),
    outer=Round(Aluminum1350H19, 76, inch(0.153)),
    core=Round(CoatedSteel, 19, inch(0.0714)),
)

MM2_900_84_19 = B232(
    code_words=(),
    designation=Mm2(900),
    outer=Round(Aluminum1350H19, 84, mm(3.69)),
    core=Round(CoatedSteel, 19, mm(2.21)),
)

WOODPECKER = B232(
    code_words=("Woodpecker",),
    designation=Kcmil(1843),
    outer=Round(Aluminum1350H19, 72, inch(0.16)),
    core=Round(CoatedSteel, 7, inch(0.1067)),
)

CHUKAR = B232(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Round(Aluminum1350H19, 84, inch(0.1456)),
    core=Round(CoatedSteel, 19, inch(0.0874)),
)

SEAHAWK = B232(
    code_words=("Seahawk",),
    designation=Kcmil(1869),
    outer=Round(Aluminum1350H19, 68, inch(0.1658)),
    core=Round(CoatedSteel, 7, inch(0.0921)),
)

MM2_1000_72_7 = B232(
    code_words=(),
    designation=Mm2(1000),
    outer=Round(Aluminum1350H19, 72, mm(4.21)),
    core=Round(CoatedSteel, 7, mm(2.81)),
)

MOCKINGBIRD = B232(
    code_words=("Mockingbird",),
    designation=Kcmil(2034.5),
    outer=Round(Aluminum1350H19, 72, inch(0.1681)),
    core=Round(CoatedSteel, 7, inch(0.1121)),
)

MM2_1000_84_19 = B232(
    code_words=(),
    designation=Mm2(1000),
    outer=Round(Aluminum1350H19, 84, mm(3.89)),
    core=Round(CoatedSteel, 19, mm(2.33)),
)

MYNAH = B232(
    code_words=("Mynah",),
    designation=Kcmil(2000),
    outer=Round(Aluminum1350H19, 84, inch(0.1543)),
    core=Round(CoatedSteel, 19, inch(0.0926)),
)

ROADRUNNER = B232(
    code_words=("Roadrunner",),
    designation=Kcmil(2057.5),
    outer=Round(Aluminum1350H19, 76, inch(0.1645)),
    core=Round(CoatedSteel, 19, inch(0.0768)),
)

KIWI = B232(
    code_words=("Kiwi",),
    designation=Kcmil(2167),
    outer=Round(Aluminum1350H19, 72, inch(0.1735)),
    core=Round(CoatedSteel, 7, inch(0.1157)),
)

COCKATOO = B232(
    code_words=("Cockatoo",),
    designation=Kcmil(2156),
    outer=Round(Aluminum1350H19, 76, inch(0.1684)),
    core=Round(CoatedSteel, 19, inch(0.0786)),
)

DODO = B232(
    code_words=("Dodo",),
    designation=Kcmil(2129),
    outer=Round(Aluminum1350H19, 84, inch(0.1592)),
    core=Round(CoatedSteel, 19, inch(0.0955)),
)

MM2_1120_72_7 = B232(
    code_words=(),
    designation=Mm2(1120),
    outer=Round(Aluminum1350H19, 72, mm(4.45)),
    core=Round(CoatedSteel, 7, mm(2.97)),
)

MM2_1120_76_19 = B232(
    code_words=(),
    designation=Mm2(1120),
    outer=Round(Aluminum1350H19, 76, mm(4.33)),
    core=Round(CoatedSteel, 19, mm(2.02)),
)

BLUEBIRD = B232(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Round(Aluminum1350H19, 84, inch(0.1602)),
    core=Round(CoatedSteel, 19, inch(0.0961)),
)

MM2_1120_84_19 = B232(
    code_words=(),
    designation=Mm2(1120),
    outer=Round(Aluminum1350H19, 84, mm(4.12)),
    core=Round(CoatedSteel, 19, mm(2.47)),
)

THRASHER = B232(
    code_words=("Thrasher",),
    designation=Kcmil(2312),
    outer=Round(Aluminum1350H19, 76, inch(0.1744)),
    core=Round(CoatedSteel, 19, inch(0.0814)),
)

KINGFISHER = B232(
    code_words=("Kingfisher",),
    designation=Kcmil(2385),
    outer=Round(Aluminum1350H19, 72, inch(0.182)),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

COCKATIEL = B232(
    code_words=("Cockatiel",),
    designation=Kcmil(2300),
    outer=Round(Aluminum1350H19, 84, inch(0.1655)),
    core=Round(CoatedSteel, 19, inch(0.0993)),
)

MM2_1250_72_7 = B232(
    code_words=(),
    designation=Mm2(1250),
    outer=Round(Aluminum1350H19, 72, mm(4.7)),
    core=Round(CoatedSteel, 7, mm(3.13)),
)

MM2_1250_76_19 = B232(
    code_words=(),
    designation=Mm2(1250),
    outer=Round(Aluminum1350H19, 76, mm(4.58)),
    core=Round(CoatedSteel, 19, mm(2.14)),
)

JOREE = B232(
    code_words=("Joree",),
    designation=Kcmil(2515),
    outer=Round(Aluminum1350H19, 76, inch(0.1819)),
    core=Round(CoatedSteel, 19, inch(0.0849)),
)

MM2_1250_84_19 = B232(
    code_words=(),
    designation=Mm2(1250),
    outer=Round(Aluminum1350H19, 84, mm(4.35)),
    core=Round(CoatedSteel, 19, mm(2.61)),
)
