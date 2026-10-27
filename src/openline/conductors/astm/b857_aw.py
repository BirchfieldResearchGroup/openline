"""ASTM B857, AW: ACSS/TW/AW, trapezoidal annealed aluminum 1350 around an aluminum-clad steel
core."""

from openline.types.conductors.astm import B857_AW
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round, Trapezoidal
from openline.types.materials import Aluminum1350O, AluminumCladSteel
from openline.types.units import equivalent, inch, kcmil

PARTRIDGE = B857_AW(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(266.8), 18), layers=2, outside_diameter=inch(0.58)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0788)),
)

ORIOLE = B857_AW(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Trapezoidal(
        Aluminum1350O, 17, equivalent(kcmil(336.4), 17), layers=2, outside_diameter=inch(0.69)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

FLICKER = B857_AW(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(477), 18), layers=2, outside_diameter=inch(0.78)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.094)),
)

HAWK = B857_AW(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(477), 18), layers=2, outside_diameter=inch(0.79)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1053)),
)

HEN = B857_AW(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Trapezoidal(
        Aluminum1350O, 17, equivalent(kcmil(477), 17), layers=2, outside_diameter=inch(0.83)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

PARAKEET = B857_AW(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(556.5), 18), layers=2, outside_diameter=inch(0.84)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1015)),
)

MOHAWK = B857_AW(
    code_words=("Mohawk",),
    designation=Kcmil(571.7),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(571.7), 18), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.103)),
)

DOVE = B857_AW(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(556.5), 20), layers=2, outside_diameter=inch(0.85)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1138)),
)

CALUMET = B857_AW(
    code_words=("Calumet",),
    designation=Kcmil(565.3),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(565.3), 20), layers=2, outside_diameter=inch(0.86)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1146)),
)

ROOK = B857_AW(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(636), 18), layers=2, outside_diameter=inch(0.89)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

GROSBEAK = B857_AW(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(636), 20), layers=2, outside_diameter=inch(0.91)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1216)),
)

MYSTIC = B857_AW(
    code_words=("Mystic",),
    designation=Kcmil(666.6),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(666.6), 20), layers=2, outside_diameter=inch(0.91)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1111)),
)

OSWEGO = B857_AW(
    code_words=("Oswego",),
    designation=Kcmil(664.8),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(664.8), 20), layers=2, outside_diameter=inch(0.93)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1244)),
)

TERN = B857_AW(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350O, 17, equivalent(kcmil(795), 17), layers=2, outside_diameter=inch(0.96)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0886)),
)

MAUMEE = B857_AW(
    code_words=("Maumee",),
    designation=Kcmil(768.2),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(768.2), 20), layers=2, outside_diameter=inch(0.98)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1195)),
)

PUFFIN = B857_AW(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350O, 18, equivalent(kcmil(795), 18), layers=2, outside_diameter=inch(0.98)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1108)),
)

WABASH = B857_AW(
    code_words=("Wabash",),
    designation=Kcmil(762.8),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(762.8), 20), layers=2, outside_diameter=inch(0.99)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1331)),
)

CONDOR = B857_AW(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(795), 20), layers=2, outside_diameter=inch(0.99)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

DRAKE = B857_AW(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(795), 20), layers=2, outside_diameter=inch(1.01)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.136)),
)

MALLARD = B857_AW(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Trapezoidal(
        Aluminum1350O, 22, equivalent(kcmil(795), 22), layers=2, outside_diameter=inch(1.05)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

PHOENIX = B857_AW(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(954), 30), layers=3, outside_diameter=inch(1.05)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0837)),
)

RAIL = B857_AW(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350O, 32, equivalent(kcmil(954), 32), layers=3, outside_diameter=inch(1.06)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0971)),
)

KETTLE = B857_AW(
    code_words=("Kettle",),
    designation=Kcmil(957.2),
    outer=Trapezoidal(
        Aluminum1350O, 32, equivalent(kcmil(957.2), 32), layers=3, outside_diameter=inch(1.06)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0973)),
)

FRASER = B857_AW(
    code_words=("Fraser",),
    designation=Kcmil(946.7),
    outer=Trapezoidal(
        Aluminum1350O, 35, equivalent(kcmil(946.7), 35), layers=3, outside_diameter=inch(1.08)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1154)),
)

CARDINAL = B857_AW(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(954), 20), layers=2, outside_diameter=inch(1.08)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

SNOWBIRD = B857_AW(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1033.5), 30), layers=3, outside_diameter=inch(1.09)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0871)),
)

COLUMBIA = B857_AW(
    code_words=("Columbia",),
    designation=Kcmil(966.2),
    outer=Trapezoidal(
        Aluminum1350O, 21, equivalent(kcmil(966.2), 21), layers=2, outside_diameter=inch(1.09)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1338)),
)

ORTOLAN = B857_AW(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350O, 32, equivalent(kcmil(1033.5), 32), layers=3, outside_diameter=inch(1.1)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.101)),
)

SUWANNEE = B857_AW(
    code_words=("Suwannee",),
    designation=Kcmil(959.6),
    outer=Trapezoidal(
        Aluminum1350O, 22, equivalent(kcmil(959.6), 22), layers=2, outside_diameter=inch(1.11)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1493)),
)

KCMIL_1080_20_7 = B857_AW(
    code_words=(),
    designation=Kcmil(1080),
    outer=Trapezoidal(
        Aluminum1350O, 20, equivalent(kcmil(1080), 20), layers=2, outside_diameter=inch(1.13)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1033)),
)

CURLEW = B857_AW(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Trapezoidal(
        Aluminum1350O, 21, equivalent(kcmil(1033.5), 21), layers=2, outside_diameter=inch(1.13)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1383)),
)

AVOCET = B857_AW(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1113), 30), layers=3, outside_diameter=inch(1.13)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0904)),
)

BLUEJAY = B857_AW(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350O, 33, equivalent(kcmil(1113), 33), layers=3, outside_diameter=inch(1.14)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1049)),
)

CHEYENNE = B857_AW(
    code_words=("Cheyenne",),
    designation=Kcmil(1168.1),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1168.1), 30), layers=3, outside_diameter=inch(1.16)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0926)),
)

GENESEE = B857_AW(
    code_words=("Genesee",),
    designation=Kcmil(1158),
    outer=Trapezoidal(
        Aluminum1350O, 33, equivalent(kcmil(1158), 33), layers=3, outside_diameter=inch(1.17)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1078)),
)

OXBIRD = B857_AW(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1192.5), 30), layers=3, outside_diameter=inch(1.17)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0936)),
)

FINCH = B857_AW(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Trapezoidal(
        Aluminum1350O, 38, equivalent(kcmil(1113), 38), layers=3, outside_diameter=inch(1.19)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0862)),
)

BUNTING = B857_AW(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350O, 33, equivalent(kcmil(1192.5), 33), layers=3, outside_diameter=inch(1.18)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

HUDSON = B857_AW(
    code_words=("Hudson",),
    designation=Kcmil(1158.4),
    outer=Trapezoidal(
        Aluminum1350O, 25, equivalent(kcmil(1158.4), 25), layers=2, outside_diameter=inch(1.2)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1467)),
)

CATAWBA = B857_AW(
    code_words=("Catawba", "Scissortail"),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1272), 30), layers=3, outside_diameter=inch(1.2)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.0967)),
)

GRACKLE = B857_AW(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Trapezoidal(
        Aluminum1350O, 38, equivalent(kcmil(1192.5), 38), layers=3, outside_diameter=inch(1.22)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0892)),
)

NELSON = B857_AW(
    code_words=("Nelson",),
    designation=Kcmil(1257.1),
    outer=Trapezoidal(
        Aluminum1350O, 35, equivalent(kcmil(1257.1), 35), layers=3, outside_diameter=inch(1.21)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1115)),
)

BITTERN = B857_AW(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350O, 35, equivalent(kcmil(1272), 35), layers=3, outside_diameter=inch(1.22)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

YUKON = B857_AW(
    code_words=("Yukon",),
    designation=Kcmil(1233.6),
    outer=Trapezoidal(
        Aluminum1350O, 38, equivalent(kcmil(1233.6), 38), layers=3, outside_diameter=inch(1.25)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.091)),
)

PHEASANT = B857_AW(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1272), 39), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0921)),
)

TRUCKEE = B857_AW(
    code_words=("Truckee",),
    designation=Kcmil(1372.5),
    outer=Trapezoidal(
        Aluminum1350O, 30, equivalent(kcmil(1372.5), 30), layers=3, outside_diameter=inch(1.25)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1004)),
)

DIPPER = B857_AW(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350O, 35, equivalent(kcmil(1351.5), 35), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1155)),
)

MACKENZIE = B857_AW(
    code_words=("Mackenzie",),
    designation=Kcmil(1359.7),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1359.7), 36), layers=3, outside_diameter=inch(1.26)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1159)),
)

THAMES = B857_AW(
    code_words=("Thames",),
    designation=Kcmil(1334.6),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1334.6), 39), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0944)),
)

MARTIN = B857_AW(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1351.5), 39), layers=3, outside_diameter=inch(1.3)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0949)),
)

BOBOLINK = B857_AW(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1431), 36), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1189)),
)

ST_CROIX = B857_AW(
    code_words=("St. Croix",),
    designation=Kcmil(1467.8),
    outer=Trapezoidal(
        Aluminum1350O, 33, equivalent(kcmil(1467.8), 33), layers=3, outside_diameter=inch(1.29)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1041)),
)

MIRAMICHI = B857_AW(
    code_words=("Miramichi",),
    designation=Kcmil(1455.3),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1455.3), 36), layers=3, outside_diameter=inch(1.3)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.12)),
)

PLOVER = B857_AW(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1431), 39), layers=3, outside_diameter=inch(1.34)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

MERRIMACK = B857_AW(
    code_words=("Merrimack",),
    designation=Kcmil(1433.6),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1433.6), 39), layers=3, outside_diameter=inch(1.34)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0978)),
)

PLATTE = B857_AW(
    code_words=("Platte",),
    designation=Kcmil(1569),
    outer=Trapezoidal(
        Aluminum1350O, 33, equivalent(kcmil(1569), 33), layers=3, outside_diameter=inch(1.33)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1074)),
)

POTOMAC = B857_AW(
    code_words=("Potomac",),
    designation=Kcmil(1557.4),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1557.4), 36), layers=3, outside_diameter=inch(1.35)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1241)),
)

LAPWING = B857_AW(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1590), 36), layers=3, outside_diameter=inch(1.36)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1253)),
)

RIO_GRANDE = B857_AW(
    code_words=("Rio Grande",),
    designation=Kcmil(1533.3),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1533.3), 39), layers=3, outside_diameter=inch(1.38)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1012)),
)

SCHUYLKILL = B857_AW(
    code_words=("Schuylkill",),
    designation=Kcmil(1657.4),
    outer=Trapezoidal(
        Aluminum1350O, 36, equivalent(kcmil(1657.4), 36), layers=3, outside_diameter=inch(1.39)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.128)),
)

FALCON = B857_AW(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Trapezoidal(
        Aluminum1350O, 42, equivalent(kcmil(1590), 42), layers=3, outside_diameter=inch(1.41)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.103)),
)

PECOS = B857_AW(
    code_words=("Pecos",),
    designation=Kcmil(1622),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1622), 39), layers=3, outside_diameter=inch(1.42)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1064)),
)

PEE_DEE = B857_AW(
    code_words=("Pee Dee",),
    designation=Kcmil(1758.6),
    outer=Trapezoidal(
        Aluminum1350O, 37, equivalent(kcmil(1758.6), 37), layers=3, outside_diameter=inch(1.43)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1319)),
)

CHUKAR = B857_AW(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Trapezoidal(
        Aluminum1350O, 37, equivalent(kcmil(1780), 37), layers=3, outside_diameter=inch(1.45)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

JAMES = B857_AW(
    code_words=("James",),
    designation=Kcmil(1730.6),
    outer=Trapezoidal(
        Aluminum1350O, 39, equivalent(kcmil(1730.6), 39), layers=3, outside_diameter=inch(1.47)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1075)),
)

ATHABASKA = B857_AW(
    code_words=("Athabaska",),
    designation=Kcmil(1949.6),
    outer=Trapezoidal(
        Aluminum1350O, 42, equivalent(kcmil(1949.6), 42), layers=3, outside_diameter=inch(1.5)
    ),
    core=Round(AluminumCladSteel, 7, inch(0.1392)),
)

CUMBERLAND = B857_AW(
    code_words=("Cumberland",),
    designation=Kcmil(1926.9),
    outer=Trapezoidal(
        Aluminum1350O, 42, equivalent(kcmil(1926.9), 42), layers=3, outside_diameter=inch(1.55)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1133)),
)

POWDER = B857_AW(
    code_words=("Powder",),
    designation=Kcmil(2153.8),
    outer=Trapezoidal(
        Aluminum1350O, 64, equivalent(kcmil(2153.8), 64), layers=4, outside_diameter=inch(1.6)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

BLUEBIRD = B857_AW(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Trapezoidal(
        Aluminum1350O, 64, equivalent(kcmil(2156), 64), layers=4, outside_diameter=inch(1.61)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

SANTEE = B857_AW(
    code_words=("Santee",),
    designation=Kcmil(2627.3),
    outer=Trapezoidal(
        Aluminum1350O, 64, equivalent(kcmil(2627.3), 64), layers=4, outside_diameter=inch(1.76)
    ),
    core=Round(AluminumCladSteel, 19, inch(0.1062)),
)

SCISSORTAIL = CATAWBA
