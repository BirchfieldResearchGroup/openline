"""ASTM B856, AW: ACSS/AW, annealed aluminum 1350 around an aluminum-clad steel core."""

from openline.types.conductors.astm import B856_AW
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum1350O, AluminumCladSteel
from openline.types.units import inch

KCMIL_101_8_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(101.8),
    outer=Round(Aluminum1350O, 12, inch(0.0921)),
    core=Round(AluminumCladSteel, 7, inch(0.0921)),
)

KCMIL_110_8_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(110.8),
    outer=Round(Aluminum1350O, 12, inch(0.0961)),
    core=Round(AluminumCladSteel, 7, inch(0.0961)),
)

KCMIL_134_6_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(134.6),
    outer=Round(Aluminum1350O, 12, inch(0.1059)),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

KCMIL_159_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(159),
    outer=Round(Aluminum1350O, 12, inch(0.1151)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

KCMIL_176_9_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(176.9),
    outer=Round(Aluminum1350O, 12, inch(0.1214)),
    core=Round(AluminumCladSteel, 7, inch(0.1214)),
)

KCMIL_190_8_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(190.8),
    outer=Round(Aluminum1350O, 12, inch(0.1261)),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

KCMIL_266_8_26_7 = B856_AW(
    code_words=(),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 26, inch(0.1013)),
    core=Round(AluminumCladSteel, 7, inch(0.0788)),
)

JUNCO = B856_AW(
    code_words=("Junco",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 30, inch(0.0943)),
    core=Round(AluminumCladSteel, 7, inch(0.0943)),
)

KCMIL_211_3_12_7 = B856_AW(
    code_words=(),
    designation=Kcmil(211.3),
    outer=Round(Aluminum1350O, 12, inch(0.1327)),
    core=Round(AluminumCladSteel, 7, inch(0.1327)),
)

OSTRICH = B856_AW(
    code_words=("Ostrich",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350O, 26, inch(0.1074)),
    core=Round(AluminumCladSteel, 7, inch(0.0835)),
)

KCMIL_203_2_16_19 = B856_AW(
    code_words=(),
    designation=Kcmil(203.2),
    outer=Round(Aluminum1350O, 16, inch(0.1127)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

LINNET = B856_AW(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 26, inch(0.1137)),
    core=Round(AluminumCladSteel, 7, inch(0.0885)),
)

ORIOLE = B856_AW(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 30, inch(0.1059)),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

BRANT = B856_AW(
    code_words=("Brant",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 24, inch(0.1287)),
    core=Round(AluminumCladSteel, 7, inch(0.0858)),
)

IBIS = B856_AW(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 26, inch(0.1236)),
    core=Round(AluminumCladSteel, 7, inch(0.0962)),
)

LARK = B856_AW(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 30, inch(0.1151)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

FLICKER = B856_AW(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 24, inch(0.141)),
    core=Round(AluminumCladSteel, 7, inch(0.094)),
)

HAWK = B856_AW(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 26, inch(0.1354)),
    core=Round(AluminumCladSteel, 7, inch(0.1053)),
)

HEN = B856_AW(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 30, inch(0.1261)),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

PARAKEET = B856_AW(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 24, inch(0.1523)),
    core=Round(AluminumCladSteel, 7, inch(0.1015)),
)

DOVE = B856_AW(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 26, inch(0.1463)),
    core=Round(AluminumCladSteel, 7, inch(0.1138)),
)

PEACOCK = B856_AW(
    code_words=("Peacock",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 24, inch(0.1588)),
    core=Round(AluminumCladSteel, 7, inch(0.1058)),
)

EAGLE = B856_AW(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 30, inch(0.1362)),
    core=Round(AluminumCladSteel, 7, inch(0.1362)),
)

SQUAB = B856_AW(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 26, inch(0.1525)),
    core=Round(AluminumCladSteel, 7, inch(0.1186)),
)

ROOK = B856_AW(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 24, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

GROSBEAK = B856_AW(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 26, inch(0.1564)),
    core=Round(AluminumCladSteel, 7, inch(0.1216)),
)

TEAL = B856_AW(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 30, inch(0.142)),
    core=Round(AluminumCladSteel, 19, inch(0.0852)),
)

WOOD_DUCK = B856_AW(
    code_words=("Wood Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 30, inch(0.142)),
    core=Round(AluminumCladSteel, 7, inch(0.142)),
)

FLAMINGO = B856_AW(
    code_words=("Flamingo",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350O, 24, inch(0.1667)),
    core=Round(AluminumCladSteel, 7, inch(0.1111)),
)

GANNET = B856_AW(
    code_words=("Gannet",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350O, 26, inch(0.1601)),
    core=Round(AluminumCladSteel, 7, inch(0.1245)),
)

EGRET = B856_AW(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 30, inch(0.1456)),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

SCOTER = B856_AW(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 30, inch(0.1456)),
    core=Round(AluminumCladSteel, 7, inch(0.1456)),
)

STILT = B856_AW(
    code_words=("Stilt",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 24, inch(0.1727)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

STARLING = B856_AW(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 26, inch(0.1659)),
    core=Round(AluminumCladSteel, 7, inch(0.129)),
)

MACAW = B856_AW(
    code_words=("Macaw",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 42, inch(0.1376)),
    core=Round(AluminumCladSteel, 7, inch(0.0764)),
)

TERN = B856_AW(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 45, inch(0.1329)),
    core=Round(AluminumCladSteel, 7, inch(0.0886)),
)

REDWING = B856_AW(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 30, inch(0.1544)),
    core=Round(AluminumCladSteel, 19, inch(0.0927)),
)

CONDOR = B856_AW(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 54, inch(0.1213)),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

CUCKOO = B856_AW(
    code_words=("Cuckoo",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 24, inch(0.182)),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

DRAKE = B856_AW(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 26, inch(0.1749)),
    core=Round(AluminumCladSteel, 7, inch(0.136)),
)

RUDDY = B856_AW(
    code_words=("Ruddy",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350O, 45, inch(0.1414)),
    core=Round(AluminumCladSteel, 7, inch(0.0943)),
)

MALLARD = B856_AW(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 30, inch(0.1628)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

CANARY = B856_AW(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350O, 54, inch(0.1291)),
    core=Round(AluminumCladSteel, 7, inch(0.1291)),
)

RAIL = B856_AW(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 45, inch(0.1456)),
    core=Round(AluminumCladSteel, 7, inch(0.0971)),
)

TOWHEE = B856_AW(
    code_words=("Towhee",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 48, inch(0.141)),
    core=Round(AluminumCladSteel, 7, inch(0.1097)),
)

CARDINAL = B856_AW(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 54, inch(0.1329)),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

KCMIL_954_24_7 = B856_AW(
    code_words=(),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 24, inch(0.1994)),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

SNOWBIRD = B856_AW(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 42, inch(0.1569)),
    core=Round(AluminumCladSteel, 7, inch(0.0871)),
)

KCMIL_1033_5_45_7 = B856_AW(
    code_words=(),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 45, inch(0.1515)),
    core=Round(AluminumCladSteel, 7, inch(0.101)),
)

CURLEW = B856_AW(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 54, inch(0.1383)),
    core=Round(AluminumCladSteel, 7, inch(0.1383)),
)

CANVASBACK = B856_AW(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 30, inch(0.1783)),
    core=Round(AluminumCladSteel, 19, inch(0.107)),
)

BLUEJAY = B856_AW(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 45, inch(0.1573)),
    core=Round(AluminumCladSteel, 7, inch(0.1048)),
)

FINCH = B856_AW(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 54, inch(0.1436)),
    core=Round(AluminumCladSteel, 19, inch(0.0861)),
)

BUNTING = B856_AW(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 45, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

GRACKLE = B856_AW(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 54, inch(0.1486)),
    core=Round(AluminumCladSteel, 19, inch(0.0892)),
)

BITTERN = B856_AW(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 45, inch(0.1681)),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

PHEASANT = B856_AW(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 54, inch(0.1535)),
    core=Round(AluminumCladSteel, 19, inch(0.0921)),
)

DIPPER = B856_AW(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 45, inch(0.1733)),
    core=Round(AluminumCladSteel, 7, inch(0.1155)),
)

MARTIN = B856_AW(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 54, inch(0.1582)),
    core=Round(AluminumCladSteel, 19, inch(0.0949)),
)

BOBOLINK = B856_AW(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 45, inch(0.1783)),
    core=Round(AluminumCladSteel, 7, inch(0.1189)),
)

PLOVER = B856_AW(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 54, inch(0.1628)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

NUTHATCH = B856_AW(
    code_words=("Nuthatch",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350O, 45, inch(0.1832)),
    core=Round(AluminumCladSteel, 7, inch(0.1221)),
)

KCMIL_1590_42_7 = B856_AW(
    code_words=(),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 42, inch(0.1946)),
    core=Round(AluminumCladSteel, 7, inch(0.1081)),
)

LAPWING = B856_AW(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 45, inch(0.188)),
    core=Round(AluminumCladSteel, 7, inch(0.1253)),
)

PARROT = B856_AW(
    code_words=("Parrot",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350O, 54, inch(0.1672)),
    core=Round(AluminumCladSteel, 19, inch(0.1003)),
)

FALCON = B856_AW(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 54, inch(0.1716)),
    core=Round(AluminumCladSteel, 19, inch(0.103)),
)

CHUKAR = B856_AW(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Round(Aluminum1350O, 84, inch(0.1456)),
    core=Round(AluminumCladSteel, 19, inch(0.0873)),
)

MOCKINGBIRD = B856_AW(
    code_words=("Mockingbird",),
    designation=Kcmil(2034.5),
    outer=Round(Aluminum1350O, 72, inch(0.1681)),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

ROADRUNNER = B856_AW(
    code_words=("Roadrunner",),
    designation=Kcmil(2057.5),
    outer=Round(Aluminum1350O, 76, inch(0.1645)),
    core=Round(AluminumCladSteel, 19, inch(0.0768)),
)

KIWI = B856_AW(
    code_words=("Kiwi",),
    designation=Kcmil(2167),
    outer=Round(Aluminum1350O, 72, inch(0.1735)),
    core=Round(AluminumCladSteel, 7, inch(0.1157)),
)

BLUEBIRD = B856_AW(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Round(Aluminum1350O, 84, inch(0.1602)),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

THRASHER = B856_AW(
    code_words=("Thrasher",),
    designation=Kcmil(2312),
    outer=Round(Aluminum1350O, 76, inch(0.1744)),
    core=Round(AluminumCladSteel, 19, inch(0.0814)),
)

JOREE = B856_AW(
    code_words=("Joree",),
    designation=Kcmil(2515),
    outer=Round(Aluminum1350O, 76, inch(0.1819)),
    core=Round(AluminumCladSteel, 19, inch(0.0849)),
)
