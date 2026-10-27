"""ASTM B856: ACSS, annealed aluminum 1350 around a coated-steel core."""

from openline.types.conductors.astm import B856
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum1350O, CoatedSteel
from openline.types.units import inch

PETREL = B856(
    code_words=("Petrel",),
    designation=Kcmil(101.8),
    outer=Round(Aluminum1350O, 12, inch(0.0921)),
    core=Round(CoatedSteel, 7, inch(0.0921)),
)

MINORCA = B856(
    code_words=("Minorca",),
    designation=Kcmil(110.8),
    outer=Round(Aluminum1350O, 12, inch(0.0961)),
    core=Round(CoatedSteel, 7, inch(0.0961)),
)

LEGHORN = B856(
    code_words=("Leghorn",),
    designation=Kcmil(134.6),
    outer=Round(Aluminum1350O, 12, inch(0.1059)),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

GUINEA = B856(
    code_words=("Guinea",),
    designation=Kcmil(159),
    outer=Round(Aluminum1350O, 12, inch(0.1151)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

DOTTEREL = B856(
    code_words=("Dotterel",),
    designation=Kcmil(176.9),
    outer=Round(Aluminum1350O, 12, inch(0.1214)),
    core=Round(CoatedSteel, 7, inch(0.1214)),
)

SPOONBILL = B856(
    code_words=("Spoonbill",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 22, inch(0.1101)),
    core=Round(CoatedSteel, 7, inch(0.0612)),
)

SCAUP = B856(
    code_words=("Scaup",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 24, inch(0.1054)),
    core=Round(CoatedSteel, 7, inch(0.0703)),
)

DORKING = B856(
    code_words=("Dorking",),
    designation=Kcmil(190.8),
    outer=Round(Aluminum1350O, 12, inch(0.1261)),
    core=Round(CoatedSteel, 7, inch(0.1261)),
)

PARTRIDGE = B856(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 26, inch(0.1013)),
    core=Round(CoatedSteel, 7, inch(0.0788)),
)

JUNCO = B856(
    code_words=("Junco",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350O, 30, inch(0.0943)),
    core=Round(CoatedSteel, 7, inch(0.0943)),
)

COCHIN = B856(
    code_words=("Cochin",),
    designation=Kcmil(211.3),
    outer=Round(Aluminum1350O, 12, inch(0.1327)),
    core=Round(CoatedSteel, 7, inch(0.1327)),
)

OSTRICH = B856(
    code_words=("Ostrich",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350O, 26, inch(0.1074)),
    core=Round(CoatedSteel, 7, inch(0.0835)),
)

TROGON = B856(
    code_words=("Trogon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 20, inch(0.1297)),
    core=Round(CoatedSteel, 7, inch(0.0576)),
)

WOODCOCK = B856(
    code_words=("Woodcock",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 22, inch(0.1237)),
    core=Round(CoatedSteel, 7, inch(0.0687)),
)

WIDGEON = B856(
    code_words=("Widgeon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 24, inch(0.1184)),
    core=Round(CoatedSteel, 7, inch(0.0789)),
)

BRAHMA = B856(
    code_words=("Brahma",),
    designation=Kcmil(203.2),
    outer=Round(Aluminum1350O, 16, inch(0.1127)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

LINNET = B856(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 26, inch(0.1137)),
    core=Round(CoatedSteel, 7, inch(0.0884)),
)

ORIOLE = B856(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350O, 30, inch(0.1059)),
    core=Round(CoatedSteel, 7, inch(0.1059)),
)

PTARMIGAN = B856(
    code_words=("Ptarmigan",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 20, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.0627)),
)

STORK = B856(
    code_words=("Stork",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 22, inch(0.1344)),
    core=Round(CoatedSteel, 7, inch(0.0747)),
)

BRANT = B856(
    code_words=("Brant",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 24, inch(0.1287)),
    core=Round(CoatedSteel, 7, inch(0.0858)),
)

IBIS = B856(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 26, inch(0.1236)),
    core=Round(CoatedSteel, 7, inch(0.0961)),
)

LARK = B856(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350O, 30, inch(0.1151)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

TAILORBIRD = B856(
    code_words=("Tailorbird",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 20, inch(0.1544)),
    core=Round(CoatedSteel, 7, inch(0.0686)),
)

TOUCAN = B856(
    code_words=("Toucan",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 22, inch(0.1472)),
    core=Round(CoatedSteel, 7, inch(0.0818)),
)

FLICKER = B856(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 24, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.094)),
)

HAWK = B856(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 26, inch(0.1354)),
    core=Round(CoatedSteel, 7, inch(0.1053)),
)

HEN = B856(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350O, 30, inch(0.1261)),
    core=Round(CoatedSteel, 7, inch(0.1261)),
)

TODY = B856(
    code_words=("Tody",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 20, inch(0.1668)),
    core=Round(CoatedSteel, 7, inch(0.0741)),
)

SAPSUCKER = B856(
    code_words=("Sapsucker",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 22, inch(0.159)),
    core=Round(CoatedSteel, 7, inch(0.0883)),
)

HERON = B856(
    code_words=("Heron",),
    designation=Kcmil(500),
    outer=Round(Aluminum1350O, 30, inch(0.1291)),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

PARAKEET = B856(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 24, inch(0.1523)),
    core=Round(CoatedSteel, 7, inch(0.1015)),
)

DOVE = B856(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 26, inch(0.1463)),
    core=Round(CoatedSteel, 7, inch(0.1138)),
)

TURACOS = B856(
    code_words=("Turacos",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 20, inch(0.1783)),
    core=Round(CoatedSteel, 7, inch(0.0792)),
)

PEACOCK = B856(
    code_words=("Peacock",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 24, inch(0.1588)),
    core=Round(CoatedSteel, 7, inch(0.1058)),
)

EAGLE = B856(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350O, 30, inch(0.1362)),
    core=Round(CoatedSteel, 7, inch(0.1362)),
)

GOLDFINCH = B856(
    code_words=("Goldfinch",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 22, inch(0.17)),
    core=Round(CoatedSteel, 7, inch(0.0944)),
)

SQUAB = B856(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 26, inch(0.1525)),
    core=Round(CoatedSteel, 7, inch(0.1186)),
)

ROOK = B856(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 24, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

GROSBEAK = B856(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 26, inch(0.1564)),
    core=Round(CoatedSteel, 7, inch(0.1216)),
)

TEAL = B856(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 30, inch(0.142)),
    core=Round(CoatedSteel, 19, inch(0.0852)),
)

WOOD_DUCK = B856(
    code_words=("Wood Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350O, 30, inch(0.142)),
    core=Round(CoatedSteel, 7, inch(0.142)),
)

FLAMINGO = B856(
    code_words=("Flamingo",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350O, 24, inch(0.1667)),
    core=Round(CoatedSteel, 7, inch(0.1111)),
)

GANNET = B856(
    code_words=("Gannet",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350O, 26, inch(0.1601)),
    core=Round(CoatedSteel, 7, inch(0.1245)),
)

EGRET = B856(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 30, inch(0.1456)),
    core=Round(CoatedSteel, 19, inch(0.0874)),
)

SCOTER = B856(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350O, 30, inch(0.1456)),
    core=Round(CoatedSteel, 7, inch(0.1456)),
)

STILT = B856(
    code_words=("Stilt",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 24, inch(0.1727)),
    core=Round(CoatedSteel, 7, inch(0.1151)),
)

STARLING = B856(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 26, inch(0.1659)),
    core=Round(CoatedSteel, 7, inch(0.129)),
)

MACAW = B856(
    code_words=("Macaw",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 42, inch(0.1376)),
    core=Round(CoatedSteel, 7, inch(0.0764)),
)

TERN = B856(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 45, inch(0.1329)),
    core=Round(CoatedSteel, 7, inch(0.0886)),
)

TURBIT = B856(
    code_words=("Turbit",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 20, inch(0.1994)),
    core=Round(CoatedSteel, 7, inch(0.0886)),
)

PUFFIN = B856(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 22, inch(0.1901)),
    core=Round(CoatedSteel, 7, inch(0.1056)),
)

REDWING = B856(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350O, 30, inch(0.1544)),
    core=Round(CoatedSteel, 19, inch(0.0926)),
)

CONDOR = B856(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 54, inch(0.1213)),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

CUCKOO = B856(
    code_words=("Cuckoo",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 24, inch(0.182)),
    core=Round(CoatedSteel, 7, inch(0.1213)),
)

DRAKE = B856(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 26, inch(0.1749)),
    core=Round(CoatedSteel, 7, inch(0.136)),
)

RUDDY = B856(
    code_words=("Ruddy",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350O, 45, inch(0.1414)),
    core=Round(CoatedSteel, 7, inch(0.0943)),
)

MALLARD = B856(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350O, 30, inch(0.1628)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

PHOENIX = B856(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 42, inch(0.1507)),
    core=Round(CoatedSteel, 7, inch(0.0837)),
)

CANARY = B856(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350O, 54, inch(0.1291)),
    core=Round(CoatedSteel, 7, inch(0.1291)),
)

CORNCRAKE = B856(
    code_words=("Corncrake",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 20, inch(0.2184)),
    core=Round(CoatedSteel, 7, inch(0.0971)),
)

RAIL = B856(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 45, inch(0.1456)),
    core=Round(CoatedSteel, 7, inch(0.0971)),
)

TOWHEE = B856(
    code_words=("Towhee",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 48, inch(0.141)),
    core=Round(CoatedSteel, 7, inch(0.1097)),
)

CARDINAL = B856(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 54, inch(0.1329)),
    core=Round(CoatedSteel, 7, inch(0.1329)),
)

REDBIRD = B856(
    code_words=("Redbird",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 24, inch(0.1994)),
    core=Round(CoatedSteel, 7, inch(0.1329)),
)

SNOWBIRD = B856(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 42, inch(0.1569)),
    core=Round(CoatedSteel, 7, inch(0.0871)),
)

ORTOLAN = B856(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 45, inch(0.1515)),
    core=Round(CoatedSteel, 7, inch(0.101)),
)

WHOOPER = B856(
    code_words=("Whooper",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 48, inch(0.1467)),
    core=Round(CoatedSteel, 7, inch(0.1141)),
)

CURLEW = B856(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350O, 54, inch(0.1383)),
    core=Round(CoatedSteel, 7, inch(0.1383)),
)

AVOCET = B856(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 42, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.0904)),
)

CANVASBACK = B856(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350O, 30, inch(0.1783)),
    core=Round(CoatedSteel, 19, inch(0.107)),
)

BLUEJAY = B856(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 45, inch(0.1573)),
    core=Round(CoatedSteel, 7, inch(0.1048)),
)

BULLFINCH = B856(
    code_words=("Bullfinch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 48, inch(0.1523)),
    core=Round(CoatedSteel, 7, inch(0.1184)),
)

OXBIRD = B856(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 42, inch(0.1685)),
    core=Round(CoatedSteel, 7, inch(0.0936)),
)

FINCH = B856(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350O, 54, inch(0.1436)),
    core=Round(CoatedSteel, 19, inch(0.0861)),
)

BUNTING = B856(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 45, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1085)),
)

CORMORANT = B856(
    code_words=("Cormorant",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 48, inch(0.1576)),
    core=Round(CoatedSteel, 7, inch(0.1226)),
)

SCISSORTAIL = B856(
    code_words=("Scissortail",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 42, inch(0.174)),
    core=Round(CoatedSteel, 7, inch(0.0967)),
)

GRACKLE = B856(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350O, 54, inch(0.1486)),
    core=Round(CoatedSteel, 19, inch(0.0892)),
)

BITTERN = B856(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 45, inch(0.1681)),
    core=Round(CoatedSteel, 7, inch(0.1121)),
)

DIVER = B856(
    code_words=("Diver",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 48, inch(0.1628)),
    core=Round(CoatedSteel, 7, inch(0.1266)),
)

RINGDOVE = B856(
    code_words=("Ringdove",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 42, inch(0.1794)),
    core=Round(CoatedSteel, 7, inch(0.0997)),
)

PHEASANT = B856(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350O, 54, inch(0.1535)),
    core=Round(CoatedSteel, 19, inch(0.0921)),
)

DIPPER = B856(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 45, inch(0.1733)),
    core=Round(CoatedSteel, 7, inch(0.1155)),
)

KCMIL_1351_5_48_7 = B856(
    code_words=(),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 48, inch(0.1678)),
    core=Round(CoatedSteel, 7, inch(0.1305)),
)

POPINJAY = B856(
    code_words=("Popinjay",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 42, inch(0.1846)),
    core=Round(CoatedSteel, 7, inch(0.1026)),
)

MARTIN = B856(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350O, 54, inch(0.1582)),
    core=Round(CoatedSteel, 19, inch(0.0949)),
)

BOBOLINK = B856(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 45, inch(0.1783)),
    core=Round(CoatedSteel, 7, inch(0.1189)),
)

WAGTAIL = B856(
    code_words=("Wagtail",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 48, inch(0.1727)),
    core=Round(CoatedSteel, 7, inch(0.1343)),
)

PLOVER = B856(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350O, 54, inch(0.1628)),
    core=Round(CoatedSteel, 19, inch(0.0977)),
)

NUTHATCH = B856(
    code_words=("Nuthatch",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350O, 45, inch(0.1832)),
    core=Round(CoatedSteel, 7, inch(0.1221)),
)

RATITE = B856(
    code_words=("Ratite",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 42, inch(0.1946)),
    core=Round(CoatedSteel, 7, inch(0.1081)),
)

LAPWING = B856(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 45, inch(0.188)),
    core=Round(CoatedSteel, 7, inch(0.1253)),
)

PARROT = B856(
    code_words=("Parrot",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350O, 54, inch(0.1672)),
    core=Round(CoatedSteel, 19, inch(0.1003)),
)

HORNBILL = B856(
    code_words=("Hornbill",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 48, inch(0.182)),
    core=Round(CoatedSteel, 7, inch(0.1416)),
)

FALCON = B856(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350O, 54, inch(0.1716)),
    core=Round(CoatedSteel, 19, inch(0.103)),
)

CHUKAR = B856(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Round(Aluminum1350O, 84, inch(0.1456)),
    core=Round(CoatedSteel, 19, inch(0.0873)),
)

SEAHAWK = B856(
    code_words=("Seahawk",),
    designation=Kcmil(1869),
    outer=Round(Aluminum1350O, 68, inch(0.1658)),
    core=Round(CoatedSteel, 7, inch(0.0921)),
)

MOCKINGBIRD = B856(
    code_words=("Mockingbird",),
    designation=Kcmil(2034.5),
    outer=Round(Aluminum1350O, 72, inch(0.1681)),
    core=Round(CoatedSteel, 7, inch(0.1121)),
)

ROADRUNNER = B856(
    code_words=("Roadrunner",),
    designation=Kcmil(2057.5),
    outer=Round(Aluminum1350O, 76, inch(0.1645)),
    core=Round(CoatedSteel, 19, inch(0.0768)),
)

KIWI = B856(
    code_words=("Kiwi",),
    designation=Kcmil(2167),
    outer=Round(Aluminum1350O, 72, inch(0.1735)),
    core=Round(CoatedSteel, 7, inch(0.1157)),
)

BLUEBIRD = B856(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Round(Aluminum1350O, 84, inch(0.1602)),
    core=Round(CoatedSteel, 19, inch(0.0961)),
)

THRASHER = B856(
    code_words=("Thrasher",),
    designation=Kcmil(2312),
    outer=Round(Aluminum1350O, 76, inch(0.1744)),
    core=Round(CoatedSteel, 19, inch(0.0814)),
)

JOREE = B856(
    code_words=("Joree",),
    designation=Kcmil(2515),
    outer=Round(Aluminum1350O, 76, inch(0.1819)),
    core=Round(CoatedSteel, 19, inch(0.0849)),
)
