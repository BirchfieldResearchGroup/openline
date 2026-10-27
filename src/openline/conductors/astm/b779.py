"""ASTM B779: ACSR/TW, trapezoidal aluminum 1350 around a coated-steel core."""

from openline.types.conductors.astm import B779
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round, Trapezoidal
from openline.types.materials import Aluminum1350H19, CoatedSteel
from openline.types.units import equivalent, in2, inch, kcmil

# Educated guess: as all 8 ACSR/TW and ACSS/TW designs of 16 wires that print their layers.
_LAYERS_OF_16 = 2

# Educated guess: as all 9 ACSR/TW and ACSS/TW designs of 17 wires that print their layers.
_LAYERS_OF_17 = 2

# Educated guess: as all 67 ACSR/TW and ACSS/TW designs of 20 wires that print their layers.
_LAYERS_OF_20 = 2

# Educated guess: as the one ACSR/TW design of 26 wires that prints its layers.
_LAYERS_OF_26 = 2

# Educated guess: as all 29 ACSR/TW and ACSS/TW designs of 30 wires that print their layers.
_LAYERS_OF_30 = 3

# Educated guess: as all 22 ACSR/TW and ACSS/TW designs of 33 wires that print their layers.
_LAYERS_OF_33 = 3

# Educated guess: as all 34 ACSR/TW and ACSS/TW designs of 39 wires that print their layers.
_LAYERS_OF_39 = 3

# Educated guess: no ACSR/TW and ACSS/TW design of 60 wires prints its layers; those of 64, the
# nearest count, print 4.
_LAYERS_OF_60 = 4


PARTRIDGE = B779(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(in2(0.2095), 14), layers=2, outside_diameter=inch(0.595)
    ),
    core=Round(CoatedSteel, 7, inch(0.0788)),
)

MERLIN = B779(
    code_words=("Merlin",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(kcmil(336.4), 14), layers=2, outside_diameter=inch(0.63)
    ),
    core=Round(CoatedSteel, 1, inch(0.1367)),
)

LINNET = B779(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.2642), 16), layers=2, outside_diameter=inch(0.659)
    ),
    core=Round(CoatedSteel, 7, inch(0.0884)),
)

ORIOLE = B779(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.2642), 16), layers=2, outside_diameter=inch(0.692)
    ),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

MONONGAHELA = B779(
    code_words=("Monongahela",),
    designation=Kcmil(405.1),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(kcmil(405.1), 14), layers=2, outside_diameter=inch(0.68)
    ),
    core=Round(CoatedSteel, 1, inch(0.152)),
)

IBIS = B779(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.3122), 20), layers=2, outside_diameter=inch(0.725)
    ),
    core=Round(CoatedSteel, 7, inch(0.0961)),
)

LARK = B779(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.3122), 16), layers=2, outside_diameter=inch(0.74)
    ),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

FLICKER = B779(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(kcmil(477), 18), layers=2, outside_diameter=inch(0.78)
    ),
    core=Round(CoatedSteel, 7, inch(0.094)),
)

HAWK = B779(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(kcmil(477), 18), layers=2, outside_diameter=inch(0.79)
    ),
    core=Round(CoatedSteel, 7, inch(0.1053)),
)

HEN = B779(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.3746), 20), layers=2, outside_diameter=inch(0.82)
    ),
    core=Round(CoatedSteel, 7, inch(0.1261)),
)

PARAKEET = B779(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(kcmil(556.5), 18), layers=2, outside_diameter=inch(0.84)
    ),
    core=Round(CoatedSteel, 7, inch(0.1015)),
)

MOHAWK = B779(
    code_words=("Mohawk",),
    designation=Kcmil(571.7),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(kcmil(571.7), 18), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(CoatedSteel, 7, inch(0.103)),
)

DOVE = B779(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(556.5), 20), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(CoatedSteel, 7, inch(0.1138)),
)

KINGBIRD = B779(
    code_words=("Kingbird", "Swift"),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 27, equivalent(kcmil(636), 27), layers=3, outside_diameter=inch(0.85)
    ),
    core=Round(CoatedSteel, 1, inch(0.1329)),
)

CALUMENT = B779(
    code_words=("Calument", "Calumet"),
    designation=Kcmil(565.3),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(565.3), 20), layers=2, outside_diameter=inch(0.86)
    ),
    core=Round(CoatedSteel, 7, inch(0.1146)),
)

EAGLE = B779(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4371), 20), layers=2, outside_diameter=inch(0.87)
    ),
    core=Round(CoatedSteel, 7, inch(0.1362)),
)

SQUAB = B779(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4752), 20), layers=2, outside_diameter=inch(0.885)
    ),
    core=Round(CoatedSteel, 7, inch(0.1186)),
)

ROOK = B779(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 19, equivalent(in2(0.4995), 19), layers=2, outside_diameter=inch(0.89)
    ),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

GROSBEAK = B779(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(636), 20), layers=2, outside_diameter=inch(0.91)
    ),
    core=Round(CoatedSteel, 7, inch(0.1216)),
)

TEAL = B779(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4752), 20), layers=2, outside_diameter=inch(0.916)
    ),
    core=Round(CoatedSteel, 19, inch(0.0852)),
)

MYSTIC = B779(
    code_words=("Mystic",),
    designation=Kcmil(666.6),
    outer=Trapezoidal(Aluminum1350H19, 18, inch(0.1924), layers=2, outside_diameter=inch(0.911)),
    core=Round(CoatedSteel, 7, inch(0.1111)),
)

OSWEGO = B779(
    code_words=("Oswego",),
    designation=Kcmil(664.8),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(664.8), 20), layers=2, outside_diameter=inch(0.93)
    ),
    core=Round(CoatedSteel, 7, inch(0.1244)),
)

EGRET = B779(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.4995), 22), layers=2, outside_diameter=inch(0.942)
    ),
    core=Round(CoatedSteel, 19, inch(0.0874)),
)

SCOTER = B779(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.4995), 22), layers=2, outside_diameter=inch(0.942)
    ),
    core=Round(CoatedSteel, 7, inch(0.1456)),
)

NECHAKO = B779(
    code_words=("Nechako",),
    designation=Kcmil(768.9),
    outer=Trapezoidal(
        Aluminum1350H19, 27, equivalent(kcmil(768.9), 27), layers=3, outside_diameter=inch(0.93)
    ),
    core=Round(CoatedSteel, 1, inch(0.152)),
)

STARLING = B779(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.562), 20), layers=2, outside_diameter=inch(0.958)
    ),
    core=Round(CoatedSteel, 7, inch(0.129)),
)

KCMIL_795_5_17_7 = B779(
    code_words=(),
    designation=Kcmil(795.5),
    outer=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(795.5), 17), layers=2, outside_diameter=inch(0.95)
    ),
    core=Round(CoatedSteel, 7, inch(0.0866)),
)

TERN = B779(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.6244), 20), layers=2, outside_diameter=inch(0.96)
    ),
    core=Round(CoatedSteel, 7, inch(0.0886)),
)

MAUMEE = B779(
    code_words=("Maumee",),
    designation=Kcmil(768.2),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(768.2), 20), layers=2, outside_diameter=inch(0.98)
    ),
    core=Round(CoatedSteel, 7, inch(0.1195)),
)

REDWING = B779(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.562), 20), layers=2, outside_diameter=inch(0.994)
    ),
    core=Round(CoatedSteel, 19, inch(0.0926)),
)

PUFFIN = B779(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Trapezoidal(Aluminum1350H19, 21, inch(0.1945), layers=2, outside_diameter=inch(0.98)),
    core=Round(CoatedSteel, 7, inch(0.1108)),
)

WABASH = B779(
    code_words=("Wabash",),
    designation=Kcmil(762.8),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(762.8), 20), layers=2, outside_diameter=inch(0.99)
    ),
    core=Round(CoatedSteel, 7, inch(0.1331)),
)

CONDOR = B779(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(795), 20), layers=2, outside_diameter=inch(0.99)
    ),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

DRAKE = B779(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(795), 20), layers=2, outside_diameter=inch(1.01)
    ),
    core=Round(CoatedSteel, 7, inch(0.136)),
)

MALLARD = B779(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Trapezoidal(Aluminum1350H19, 22, inch(0.1901), layers=2, outside_diameter=inch(1.047)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

PHOENIX = B779(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(954), 30), layers=3, outside_diameter=inch(1.05)
    ),
    core=Round(CoatedSteel, 7, inch(0.0837)),
)

CANARY = B779(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.7069), 20), layers=2, outside_diameter=inch(1.055)
    ),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

RAIL = B779(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.17), layers=_LAYERS_OF_33, outside_diameter=inch(1.06)
    ),
    core=Round(CoatedSteel, 7, inch(0.0971)),
)

KETTLE = B779(
    code_words=("Kettle",),
    designation=Kcmil(957.2),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.1703), layers=_LAYERS_OF_33, outside_diameter=inch(1.06)
    ),
    core=Round(CoatedSteel, 7, inch(0.0973)),
)

FRASER = B779(
    code_words=("Fraser",),
    designation=Kcmil(946.7),
    outer=Trapezoidal(
        Aluminum1350H19, 35, equivalent(kcmil(946.7), 35), layers=3, outside_diameter=inch(1.08)
    ),
    core=Round(CoatedSteel, 7, inch(0.1154)),
)

CARDINAL = B779(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(kcmil(954), 20), layers=2, outside_diameter=inch(1.08)
    ),
    core=Round(CoatedSteel, 7, inch(0.1329)),
)

SNOWBIRD = B779(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1033.5), 30), layers=3, outside_diameter=inch(1.09)
    ),
    core=Round(CoatedSteel, 7, inch(0.0871)),
)

COLUMBIA = B779(
    code_words=("Columbia",),
    designation=Kcmil(966.2),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.7589), 22), layers=2, outside_diameter=inch(1.092)
    ),
    core=Round(CoatedSteel, 7, inch(0.1338)),
)

ORTOLAN = B779(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.8117), 34), layers=3, outside_diameter=inch(1.102)
    ),
    core=Round(CoatedSteel, 7, inch(0.101)),
)

SUWANEE = B779(
    code_words=("Suwanee", "Suwannee"),
    designation=Kcmil(959.6),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(kcmil(959.6), 22), layers=2, outside_diameter=inch(1.11)
    ),
    core=Round(CoatedSteel, 7, inch(0.1493)),
)

KCMIL_1109_7_17_7 = B779(
    code_words=(),
    designation=Kcmil(1109.7),
    outer=Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(1109.7), 17), layers=2, outside_diameter=inch(1.1)
    ),
    core=Round(CoatedSteel, 7, inch(0.07)),
)

CURLEW = B779(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.8117), 22), layers=2, outside_diameter=inch(1.131)
    ),
    core=Round(CoatedSteel, 7, inch(0.1383)),
)

AVOCET = B779(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1113), 30), layers=3, outside_diameter=inch(1.13)
    ),
    core=Round(CoatedSteel, 7, inch(0.0904)),
)

CANVASBACK = B779(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 24, equivalent(in2(0.7493), 24), layers=2, outside_diameter=inch(1.149)
    ),
    core=Round(CoatedSteel, 19, inch(0.107)),
)

BLUEJAY = B779(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350H19, 33, equivalent(kcmil(1113), 33), layers=3, outside_diameter=inch(1.14)
    ),
    core=Round(CoatedSteel, 7, inch(0.1049)),
)

CHEYENNE = B779(
    code_words=("Cheyenne",),
    designation=Kcmil(1168.1),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1168.1), 30), layers=3, outside_diameter=inch(1.16)
    ),
    core=Round(CoatedSteel, 7, inch(0.0926)),
)

GENESEE = B779(
    code_words=("Genesee",),
    designation=Kcmil(1158),
    outer=Trapezoidal(
        Aluminum1350H19, 33, equivalent(kcmil(1158), 33), layers=3, outside_diameter=inch(1.17)
    ),
    core=Round(CoatedSteel, 7, inch(0.1078)),
)

FINCH = B779(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Trapezoidal(Aluminum1350H19, 39, inch(0.1689), layers=3, outside_diameter=inch(1.18)),
    core=Round(CoatedSteel, 19, inch(0.0862)),
)

OXBIRD = B779(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1192.5), 30), layers=3, outside_diameter=inch(1.17)
    ),
    core=Round(CoatedSteel, 7, inch(0.0936)),
)

BUNTING = B779(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.9366), 34), layers=3, outside_diameter=inch(1.181)
    ),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

HUDSON = B779(
    code_words=("Hudson",),
    designation=Kcmil(1158.4),
    outer=Trapezoidal(
        Aluminum1350H19, 39, inch(0.1723), layers=_LAYERS_OF_39, outside_diameter=inch(1.209)
    ),
    core=Round(CoatedSteel, 7, inch(0.1467)),
)

CATAWBA = B779(
    code_words=("Catawba", "Scissortail"),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1272), 30), layers=3, outside_diameter=inch(1.2)
    ),
    core=Round(CoatedSteel, 7, inch(0.0967)),
)

NELSON = B779(
    code_words=("Nelson",),
    designation=Kcmil(1257.1),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(0.9873), 36), layers=3, outside_diameter=inch(1.213)
    ),
    core=Round(CoatedSteel, 7, inch(0.1115)),
)

GRACKLE = B779(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(Aluminum1350H19, 39, inch(0.1749), layers=3, outside_diameter=inch(1.22)),
    core=Round(CoatedSteel, 19, inch(0.0892)),
)

BITTERN = B779(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(0.999), 38), layers=3, outside_diameter=inch(1.224)
    ),
    core=Round(CoatedSteel, 7, inch(0.1121)),
)

YUKON = B779(
    code_words=("Yukon",),
    designation=Kcmil(1233.6),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(kcmil(1233.6), 38), layers=3, outside_diameter=inch(1.25)
    ),
    core=Round(CoatedSteel, 19, inch(0.091)),
)

PHEASANT = B779(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1272), 39), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(CoatedSteel, 19, inch(0.0921)),
)

TRUCKEE = B779(
    code_words=("Truckee",),
    designation=Kcmil(1372.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(kcmil(1372.5), 30), layers=3, outside_diameter=inch(1.25)
    ),
    core=Round(CoatedSteel, 7, inch(0.1004)),
)

DIPPER = B779(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.0615), 36), layers=3, outside_diameter=inch(1.256)
    ),
    core=Round(CoatedSteel, 7, inch(0.1155)),
)

MACKENZIE = B779(
    code_words=("Mackenzie",),
    designation=Kcmil(1359.7),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.0679), 38), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(CoatedSteel, 7, inch(0.1159)),
)

THAMES = B779(
    code_words=("Thames",),
    designation=Kcmil(1334.6),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1334.6), 39), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(CoatedSteel, 19, inch(0.0944)),
)

MARTIN = B779(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1351.5), 39), layers=3, outside_diameter=inch(1.3)
    ),
    core=Round(CoatedSteel, 19, inch(0.0949)),
)

BOBOLINK = B779(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.2082), layers=_LAYERS_OF_33, outside_diameter=inch(1.29)
    ),
    core=Round(CoatedSteel, 7, inch(0.1189)),
)

ST_CROIX = B779(
    code_words=("St. Croix",),
    designation=Kcmil(1467.8),
    outer=Trapezoidal(
        Aluminum1350H19, 30, inch(0.2212), layers=_LAYERS_OF_30, outside_diameter=inch(1.29)
    ),
    core=Round(CoatedSteel, 7, inch(0.1041)),
)

MIRAMICHI = B779(
    code_words=("Miramichi",),
    designation=Kcmil(1455.3),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.21), layers=_LAYERS_OF_33, outside_diameter=inch(1.3)
    ),
    core=Round(CoatedSteel, 7, inch(0.12)),
)

KCMIL_1524_1_33_7 = B779(
    code_words=(),
    designation=Kcmil(1524.1),
    outer=Trapezoidal(
        Aluminum1350H19, 33, equivalent(kcmil(1524.1), 33), layers=3, outside_diameter=inch(1.3)
    ),
    core=Round(CoatedSteel, 7, inch(0.0966)),
)

PLOVER = B779(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350H19, 37, equivalent(in2(1.1239), 37), layers=3, outside_diameter=inch(1.337)
    ),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

MERRIMACK = B779(
    code_words=("Merrimack",),
    designation=Kcmil(1433.6),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1433.6), 39), layers=3, outside_diameter=inch(1.34)
    ),
    core=Round(CoatedSteel, 19, inch(0.0978)),
)

PLATTE = B779(
    code_words=("Platte",),
    designation=Kcmil(1569),
    outer=Trapezoidal(
        Aluminum1350H19, 30, inch(0.2287), layers=_LAYERS_OF_30, outside_diameter=inch(1.333)
    ),
    core=Round(CoatedSteel, 7, inch(0.1074)),
)

POTOMAC = B779(
    code_words=("Potomac",),
    designation=Kcmil(1557.4),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(kcmil(1557.4), 36), layers=3, outside_diameter=inch(1.35)
    ),
    core=Round(CoatedSteel, 7, inch(0.1241)),
)

LAPWING = B779(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.2195), layers=_LAYERS_OF_33, outside_diameter=inch(1.357)
    ),
    core=Round(CoatedSteel, 7, inch(0.1253)),
)

RIO_GRANDE = B779(
    code_words=("Rio Grande",),
    designation=Kcmil(1533.3),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1533.3), 39), layers=3, outside_diameter=inch(1.38)
    ),
    core=Round(CoatedSteel, 19, inch(0.1012)),
)

SCHUYLKILL = B779(
    code_words=("Schuylkill",),
    designation=Kcmil(1657.4),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.2241), layers=_LAYERS_OF_33, outside_diameter=inch(1.384)
    ),
    core=Round(CoatedSteel, 7, inch(0.128)),
)

FALCON = B779(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350H19, 42, equivalent(kcmil(1590), 42), layers=3, outside_diameter=inch(1.41)
    ),
    core=Round(CoatedSteel, 19, inch(0.103)),
)

PECOS = B779(
    code_words=("Pecos",),
    designation=Kcmil(1622),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(kcmil(1622), 39), layers=3, outside_diameter=inch(1.42)
    ),
    core=Round(CoatedSteel, 19, inch(0.1064)),
)

PEE_DEE = B779(
    code_words=("Pee Dee",),
    designation=Kcmil(1758.6),
    outer=Trapezoidal(
        Aluminum1350H19, 33, inch(0.2308), layers=_LAYERS_OF_33, outside_diameter=inch(1.425)
    ),
    core=Round(CoatedSteel, 7, inch(0.1319)),
)

CHUKAR = B779(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Trapezoidal(Aluminum1350H19, 36, inch(0.2224), layers=3, outside_diameter=inch(1.447)),
    core=Round(CoatedSteel, 19, inch(0.0874)),
)

JAMES = B779(
    code_words=("James",),
    designation=Kcmil(1730.6),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(1.359), 34), layers=3, outside_diameter=inch(1.47)
    ),
    core=Round(CoatedSteel, 19, inch(0.1075)),
)

KCMIL_1935_4_31_7 = B779(
    code_words=(),
    designation=Kcmil(1935.4),
    outer=Trapezoidal(
        Aluminum1350H19, 31, equivalent(kcmil(1935.4), 31), layers=3, outside_diameter=inch(1.45)
    ),
    core=Round(CoatedSteel, 7, inch(0.0866)),
)

ATHABASKA = B779(
    code_words=("Athabaska",),
    designation=Kcmil(1949.6),
    outer=Trapezoidal(
        Aluminum1350H19, 44, equivalent(in2(1.5312), 44), layers=3, outside_diameter=inch(1.504)
    ),
    core=Round(CoatedSteel, 7, inch(0.1392)),
)

CUMBERLAND = B779(
    code_words=("Cumberland",),
    designation=Kcmil(1926.9),
    outer=Trapezoidal(
        Aluminum1350H19, 42, equivalent(kcmil(1926.9), 42), layers=3, outside_diameter=inch(1.55)
    ),
    core=Round(CoatedSteel, 19, inch(0.1133)),
)

POWDER = B779(
    code_words=("Powder",),
    designation=Kcmil(2153.8),
    outer=Trapezoidal(
        Aluminum1350H19, 64, equivalent(kcmil(2153.8), 64), layers=4, outside_diameter=inch(1.6)
    ),
    core=Round(CoatedSteel, 19, inch(0.0961)),
)

BLUEBIRD = B779(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Trapezoidal(
        Aluminum1350H19, 64, equivalent(kcmil(2156), 64), layers=4, outside_diameter=inch(1.61)
    ),
    core=Round(CoatedSteel, 19, inch(0.0961)),
)

SANTEE = B779(
    code_words=("Santee",),
    designation=Kcmil(2627.3),
    outer=Trapezoidal(
        Aluminum1350H19, 60, inch(0.2093), layers=_LAYERS_OF_60, outside_diameter=inch(1.764)
    ),
    core=Round(CoatedSteel, 19, inch(0.1062)),
)

SWIFT = KINGBIRD
CALUMET = CALUMENT
SUWANNEE = SUWANEE
SCISSORTAIL = CATAWBA
