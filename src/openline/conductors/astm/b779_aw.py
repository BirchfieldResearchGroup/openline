"""ASTM B779, AW: ACSR/TW/AW, trapezoidal aluminum 1350 around an aluminum-clad steel core."""

from openline.types.conductors.astm import B779_AW
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round, Trapezoidal
from openline.types.materials import Aluminum1350H19, AluminumCladSteel
from openline.types.units import equivalent, in2, inch

PARTRIDGE = B779_AW(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(in2(0.2095), 14), layers=2, outside_diameter=inch(0.595)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0788)),
)

MERLIN = B779_AW(
    code_words=("Merlin",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(in2(0.2642), 14), layers=2, outside_diameter=inch(0.63)
    ),
    core=Round(AluminumCladSteel, 1, inch(0.1367)),
)

LINNET = B779_AW(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.2642), 16), layers=2, outside_diameter=inch(0.659)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0884)),
)

ORIOLE = B779_AW(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.2642), 16), layers=2, outside_diameter=inch(0.692)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

MONONGAHELA = B779_AW(
    code_words=("Monongahela",),
    designation=Kcmil(405.1),
    outer=Trapezoidal(
        Aluminum1350H19, 14, equivalent(in2(0.3182), 14), layers=2, outside_diameter=inch(0.68)
    ),
    core=Round(AluminumCladSteel, 1, inch(0.152)),
)

IBIS = B779_AW(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.3122), 20), layers=2, outside_diameter=inch(0.725)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0961)),
)

LARK = B779_AW(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Trapezoidal(
        Aluminum1350H19, 16, equivalent(in2(0.3122), 16), layers=2, outside_diameter=inch(0.74)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

FLICKER = B779_AW(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(in2(0.3746), 18), layers=2, outside_diameter=inch(0.776)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.094)),
)

HAWK = B779_AW(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(in2(0.3746), 18), layers=2, outside_diameter=inch(0.79)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1053)),
)

HEN = B779_AW(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.3746), 20), layers=2, outside_diameter=inch(0.82)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

PARAKEET = B779_AW(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(in2(0.4371), 18), layers=2, outside_diameter=inch(0.84)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1015)),
)

MOHAWK = B779_AW(
    code_words=("Mohawk",),
    designation=Kcmil(571.7),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(in2(0.449), 18), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.103)),
)

DOVE = B779_AW(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4371), 20), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1138)),
)

SWIFT = B779_AW(
    code_words=("Swift",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 27, equivalent(in2(0.4995), 27), layers=3, outside_diameter=inch(0.85)
    ),
    core=Round(AluminumCladSteel, 1, inch(0.1329)),
)

CALUMET = B779_AW(
    code_words=("Calumet",),
    designation=Kcmil(565.3),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.444), 20), layers=2, outside_diameter=inch(0.86)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1146)),
)

EAGLE = B779_AW(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4371), 20), layers=2, outside_diameter=inch(0.87)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1362)),
)

SQUAB = B779_AW(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4752), 20), layers=2, outside_diameter=inch(0.885)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1186)),
)

ROOK = B779_AW(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4995), 20), layers=2, outside_diameter=inch(0.893)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

GROSBEAK = B779_AW(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4995), 20), layers=2, outside_diameter=inch(0.909)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1216)),
)

TEAL = B779_AW(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.4752), 20), layers=2, outside_diameter=inch(0.916)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0852)),
)

MYSTIC = B779_AW(
    code_words=("Mystic",),
    designation=Kcmil(666.6),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.5235), 20), layers=2, outside_diameter=inch(0.913)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1111)),
)

OSWEGO = B779_AW(
    code_words=("Oswego",),
    designation=Kcmil(664.8),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.5221), 20), layers=2, outside_diameter=inch(0.927)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1244)),
)

EGRET = B779_AW(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.4995), 22), layers=2, outside_diameter=inch(0.942)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

SCOTER = B779_AW(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.4995), 22), layers=2, outside_diameter=inch(0.942)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1456)),
)

NECHAKO = B779_AW(
    code_words=("Nechako",),
    designation=Kcmil(768.9),
    outer=Trapezoidal(
        Aluminum1350H19, 27, equivalent(in2(0.6039), 27), layers=3, outside_diameter=inch(0.93)
    ),
    core=Round(AluminumCladSteel, 1, inch(0.152)),
)

STARLING = B779_AW(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.562), 20), layers=2, outside_diameter=inch(0.958)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.129)),
)

TERN = B779_AW(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.6244), 20), layers=2, outside_diameter=inch(0.96)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0886)),
)

MAUMEE = B779_AW(
    code_words=("Maumee",),
    designation=Kcmil(768.2),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.6033), 20), layers=2, outside_diameter=inch(0.977)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1195)),
)

PUFFIN = B779_AW(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 18, equivalent(in2(0.6244), 18), layers=2, outside_diameter=inch(0.98)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1056)),
)

REDWING = B779_AW(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.562), 20), layers=2, outside_diameter=inch(0.994)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0926)),
)

WABASH = B779_AW(
    code_words=("Wabash",),
    designation=Kcmil(762.8),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.5991), 20), layers=2, outside_diameter=inch(0.99)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1331)),
)

CONDOR = B779_AW(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.6244), 20), layers=2, outside_diameter=inch(0.993)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

DRAKE = B779_AW(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.6244), 20), layers=2, outside_diameter=inch(1.01)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.136)),
)

MALLARD = B779_AW(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.6244), 22), layers=2, outside_diameter=inch(1.05)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

PHOENIX = B779_AW(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.7493), 30), layers=3, outside_diameter=inch(1.044)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0837)),
)

CANARY = B779_AW(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.7069), 20), layers=2, outside_diameter=inch(1.055)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1291)),
)

RAIL = B779_AW(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 32, equivalent(in2(0.7493), 32), layers=3, outside_diameter=inch(1.061)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0971)),
)

KETTLE = B779_AW(
    code_words=("Kettle",),
    designation=Kcmil(957.2),
    outer=Trapezoidal(
        Aluminum1350H19, 32, equivalent(in2(0.7518), 32), layers=3, outside_diameter=inch(1.06)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0973)),
)

FRASER = B779_AW(
    code_words=("Fraser",),
    designation=Kcmil(946.7),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.7435), 34), layers=3, outside_diameter=inch(1.077)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1154)),
)

CARDINAL = B779_AW(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 20, equivalent(in2(0.7493), 20), layers=2, outside_diameter=inch(1.08)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

SNOWBIRD = B779_AW(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.8117), 30), layers=3, outside_diameter=inch(1.089)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0872)),
)

COLUMBIA = B779_AW(
    code_words=("Columbia",),
    designation=Kcmil(966.2),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.7589), 22), layers=2, outside_diameter=inch(1.092)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1338)),
)

ORTOLAN = B779_AW(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.8117), 34), layers=3, outside_diameter=inch(1.102)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.101)),
)

SUWANNEE = B779_AW(
    code_words=("Suwannee",),
    designation=Kcmil(959.6),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.7537), 22), layers=2, outside_diameter=inch(1.11)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1493)),
)

CURLEW = B779_AW(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350H19, 22, equivalent(in2(0.8117), 22), layers=2, outside_diameter=inch(1.131)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1383)),
)

AVOCET = B779_AW(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.8741), 30), layers=3, outside_diameter=inch(1.13)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0904)),
)

CANVASBACK = B779_AW(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350H19, 24, equivalent(in2(0.7493), 24), layers=2, outside_diameter=inch(1.149)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.107)),
)

BLUEJAY = B779_AW(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.8741), 34), layers=3, outside_diameter=inch(1.143)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1049)),
)

CHEYENNE = B779_AW(
    code_words=("Cheyenne",),
    designation=Kcmil(1168.1),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.9174), 30), layers=3, outside_diameter=inch(1.155)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0926)),
)

GENESEE = B779_AW(
    code_words=("Genesee",),
    designation=Kcmil(1158),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.9095), 34), layers=3, outside_diameter=inch(1.165)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1078)),
)

OXBIRD = B779_AW(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.9366), 30), layers=3, outside_diameter=inch(1.17)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0936)),
)

FINCH = B779_AW(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(0.8741), 38), layers=3, outside_diameter=inch(1.19)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0862)),
)

BUNTING = B779_AW(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350H19, 34, equivalent(in2(0.9366), 34), layers=3, outside_diameter=inch(1.181)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

HUDSON = B779_AW(
    code_words=("Hudson",),
    designation=Kcmil(1158.4),
    outer=Trapezoidal(
        Aluminum1350H19, 24, equivalent(in2(0.9098), 24), layers=2, outside_diameter=inch(1.196)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1467)),
)

SCISSORTAIL = B779_AW(
    code_words=("Scissortail",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(0.999), 30), layers=3, outside_diameter=inch(1.203)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0967)),
)

GRACKLE = B779_AW(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(0.9366), 38), layers=3, outside_diameter=inch(1.225)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0892)),
)

NELSON = B779_AW(
    code_words=("Nelson",),
    designation=Kcmil(1257.1),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(0.9873), 36), layers=3, outside_diameter=inch(1.213)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1115)),
)

BITTERN = B779_AW(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(0.999), 38), layers=3, outside_diameter=inch(1.224)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

YUKON = B779_AW(
    code_words=("Yukon",),
    designation=Kcmil(1233.6),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(0.9689), 38), layers=3, outside_diameter=inch(1.245)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.091)),
)

PHEASANT = B779_AW(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(in2(0.999), 39), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0921)),
)

TRUCKEE = B779_AW(
    code_words=("Truckee",),
    designation=Kcmil(1372.5),
    outer=Trapezoidal(
        Aluminum1350H19, 30, equivalent(in2(1.078), 30), layers=3, outside_diameter=inch(1.248)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1004)),
)

DIPPER = B779_AW(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.0615), 36), layers=3, outside_diameter=inch(1.256)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1155)),
)

MACKENZIE = B779_AW(
    code_words=("Mackenzie",),
    designation=Kcmil(1359.7),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.0679), 38), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1159)),
)

THAMES = B779_AW(
    code_words=("Thames",),
    designation=Kcmil(1334.6),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.0482), 38), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0944)),
)

MARTIN = B779_AW(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350H19, 42, equivalent(in2(1.0615), 42), layers=3, outside_diameter=inch(1.3)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0949)),
)

BOBOLINK = B779_AW(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.1239), 36), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1189)),
)

ST_CROIX = B779_AW(
    code_words=("St. Croix",),
    designation=Kcmil(1467.8),
    outer=Trapezoidal(
        Aluminum1350H19, 33, equivalent(in2(1.1528), 33), layers=3, outside_diameter=inch(1.292)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1041)),
)

MIRAMICHI = B779_AW(
    code_words=("Miramichi",),
    designation=Kcmil(1455.3),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.143), 36), layers=3, outside_diameter=inch(1.302)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.12)),
)

PLOVER = B779_AW(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350H19, 40, equivalent(in2(1.1239), 40), layers=3, outside_diameter=inch(1.337)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

MERRIMACK = B779_AW(
    code_words=("Merrimack",),
    designation=Kcmil(1433.6),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(in2(1.1259), 39), layers=3, outside_diameter=inch(1.34)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0978)),
)

PLATTE = B779_AW(
    code_words=("Platte",),
    designation=Kcmil(1569),
    outer=Trapezoidal(
        Aluminum1350H19, 33, equivalent(in2(1.2323), 33), layers=3, outside_diameter=inch(1.334)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1074)),
)

POTOMAC = B779_AW(
    code_words=("Potomac",),
    designation=Kcmil(1557.4),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.2232), 36), layers=3, outside_diameter=inch(1.35)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1241)),
)

LAPWING = B779_AW(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.2488), 36), layers=3, outside_diameter=inch(1.358)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1253)),
)

RIO_GRANDE = B779_AW(
    code_words=("Rio Grande",),
    designation=Kcmil(1533.3),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.2043), 38), layers=3, outside_diameter=inch(1.38)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1012)),
)

SCHUYLKILL = B779_AW(
    code_words=("Schuylkill",),
    designation=Kcmil(1657.4),
    outer=Trapezoidal(
        Aluminum1350H19, 36, equivalent(in2(1.3017), 36), layers=3, outside_diameter=inch(1.386)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.128)),
)

FALCON = B779_AW(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350H19, 42, equivalent(in2(1.2488), 42), layers=3, outside_diameter=inch(1.41)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.103)),
)

PECOS = B779_AW(
    code_words=("Pecos",),
    designation=Kcmil(1622),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(in2(1.2739), 39), layers=3, outside_diameter=inch(1.42)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1064)),
)

PEE_DEE = B779_AW(
    code_words=("Pee Dee",),
    designation=Kcmil(1758.6),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.3812), 38), layers=3, outside_diameter=inch(1.43)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1319)),
)

CHUKAR = B779_AW(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Trapezoidal(
        Aluminum1350H19, 38, equivalent(in2(1.398), 38), layers=3, outside_diameter=inch(1.445)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

JAMES = B779_AW(
    code_words=("James",),
    designation=Kcmil(1730.6),
    outer=Trapezoidal(
        Aluminum1350H19, 39, equivalent(in2(1.3592), 39), layers=3, outside_diameter=inch(1.47)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1075)),
)

ATHABASKA = B779_AW(
    code_words=("Athabaska",),
    designation=Kcmil(1949.6),
    outer=Trapezoidal(
        Aluminum1350H19, 44, equivalent(in2(1.5312), 44), layers=3, outside_diameter=inch(1.504)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1392)),
)

CUMBERLAND = B779_AW(
    code_words=("Cumberland",),
    designation=Kcmil(1926.9),
    outer=Trapezoidal(
        Aluminum1350H19, 42, equivalent(in2(1.5134), 42), layers=3, outside_diameter=inch(1.55)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1133)),
)

POWDER = B779_AW(
    code_words=("Powder",),
    designation=Kcmil(2153.8),
    outer=Trapezoidal(
        Aluminum1350H19, 64, equivalent(in2(1.6916), 64), layers=4, outside_diameter=inch(1.596)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

BLUEBIRD = B779_AW(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Trapezoidal(
        Aluminum1350H19, 64, equivalent(in2(1.6933), 64), layers=4, outside_diameter=inch(1.608)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

SANTEE = B779_AW(
    code_words=("Santee",),
    designation=Kcmil(2627.3),
    outer=Trapezoidal(
        Aluminum1350H19, 64, equivalent(in2(2.0635), 64), layers=4, outside_diameter=inch(1.761)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1062)),
)
