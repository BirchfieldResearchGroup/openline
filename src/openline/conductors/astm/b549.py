"""ASTM B549: ACSR/AW, aluminum 1350 around an aluminum-clad steel core."""

from openline.types.conductors.astm import B549
from openline.types.conductors.designations import Gauge, Kcmil
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum1350H19, AluminumCladSteel
from openline.types.units import inch

MAGPIE = B549(
    code_words=("Magpie",),
    designation=Kcmil(20.87),
    outer=Round(Aluminum1350H19, 3, inch(0.0834)),
    core=Round(AluminumCladSteel, 4, inch(0.0834)),
)

SWAN = B549(
    code_words=("Swan",),
    designation=Gauge(4),
    outer=Round(Aluminum1350H19, 6, inch(0.0834)),
    core=Round(AluminumCladSteel, 1, inch(0.0834)),
)

SWANATE = B549(
    code_words=("Swanate",),
    designation=Gauge(4),
    outer=Round(Aluminum1350H19, 7, inch(0.0772)),
    core=Round(AluminumCladSteel, 1, inch(0.1029)),
)

SWALLOW = B549(
    code_words=("Swallow",),
    designation=Gauge(3),
    outer=Round(Aluminum1350H19, 6, inch(0.0937)),
    core=Round(AluminumCladSteel, 1, inch(0.0937)),
)

ALBATROSS = B549(
    code_words=("Albatross",),
    designation=Kcmil(54.95),
    outer=Round(Aluminum1350H19, 7, inch(0.0886)),
    core=Round(AluminumCladSteel, 1, inch(0.1181)),
)

SHRIKE = B549(
    code_words=("Shrike",),
    designation=Kcmil(33.185),
    outer=Round(Aluminum1350H19, 3, inch(0.1052)),
    core=Round(AluminumCladSteel, 4, inch(0.1052)),
)

SPARROW = B549(
    code_words=("Sparrow",),
    designation=Gauge(2),
    outer=Round(Aluminum1350H19, 6, inch(0.1052)),
    core=Round(AluminumCladSteel, 1, inch(0.1052)),
)

SPARATE = B549(
    code_words=("Sparate",),
    designation=Gauge(2),
    outer=Round(Aluminum1350H19, 7, inch(0.0974)),
    core=Round(AluminumCladSteel, 1, inch(0.1299)),
)

ROBIN = B549(
    code_words=("Robin",),
    designation=Gauge(1),
    outer=Round(Aluminum1350H19, 6, inch(0.1181)),
    core=Round(AluminumCladSteel, 1, inch(0.1181)),
)

GROUSE = B549(
    code_words=("Grouse",),
    designation=Kcmil(80),
    outer=Round(Aluminum1350H19, 8, inch(0.1)),
    core=Round(AluminumCladSteel, 1, inch(0.167)),
)

SNIPE = B549(
    code_words=("Snipe",),
    designation=Kcmil(52.77),
    outer=Round(Aluminum1350H19, 3, inch(0.1326)),
    core=Round(AluminumCladSteel, 4, inch(0.1326)),
)

RAVEN = B549(
    code_words=("Raven",),
    designation=Gauge(0),
    outer=Round(Aluminum1350H19, 6, inch(0.1327)),
    core=Round(AluminumCladSteel, 1, inch(0.1327)),
)

SHOEBILL = B549(
    code_words=("Shoebill",),
    designation=Kcmil(57.5),
    outer=Round(Aluminum1350H19, 3, inch(0.1384)),
    core=Round(AluminumCladSteel, 4, inch(0.1384)),
)

LOON = B549(
    code_words=("Loon",),
    designation=Kcmil(66.54),
    outer=Round(Aluminum1350H19, 3, inch(0.1489)),
    core=Round(AluminumCladSteel, 4, inch(0.1489)),
)

QUAIL = B549(
    code_words=("Quail",),
    designation=Gauge(-1),
    outer=Round(Aluminum1350H19, 6, inch(0.1489)),
    core=Round(AluminumCladSteel, 1, inch(0.1489)),
)

PETREL = B549(
    code_words=("Petrel",),
    designation=Kcmil(101.8),
    outer=Round(Aluminum1350H19, 12, inch(0.0921)),
    core=Round(AluminumCladSteel, 7, inch(0.0921)),
)

MINORCA = B549(
    code_words=("Minorca",),
    designation=Kcmil(110.8),
    outer=Round(Aluminum1350H19, 12, inch(0.0961)),
    core=Round(AluminumCladSteel, 7, inch(0.0961)),
)

PIGEON = B549(
    code_words=("Pigeon",),
    designation=Gauge(-2),
    outer=Round(Aluminum1350H19, 6, inch(0.1672)),
    core=Round(AluminumCladSteel, 1, inch(0.1672)),
)

LEGHORN = B549(
    code_words=("Leghorn",),
    designation=Kcmil(134.6),
    outer=Round(Aluminum1350H19, 12, inch(0.1059)),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

JAEGER = B549(
    code_words=("Jaeger",),
    designation=Kcmil(228.2),
    outer=Round(Aluminum1350H19, 18, inch(0.1126)),
    core=Round(AluminumCladSteel, 1, inch(0.1126)),
)

PENGUIN = B549(
    code_words=("Penguin",),
    designation=Gauge(-3),
    outer=Round(Aluminum1350H19, 6, inch(0.1878)),
    core=Round(AluminumCladSteel, 1, inch(0.1878)),
)

GUINEA = B549(
    code_words=("Guinea",),
    designation=Kcmil(159),
    outer=Round(Aluminum1350H19, 12, inch(0.1151)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

AUK = B549(
    code_words=("Auk",),
    designation=Kcmil(203),
    outer=Round(Aluminum1350H19, 8, inch(0.1593)),
    core=Round(AluminumCladSteel, 7, inch(0.0885)),
)

DOTTEREL = B549(
    code_words=("Dotterel",),
    designation=Kcmil(176.9),
    outer=Round(Aluminum1350H19, 12, inch(0.1214)),
    core=Round(AluminumCladSteel, 7, inch(0.1214)),
)

WAXWING = B549(
    code_words=("Waxwing",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 18, inch(0.1217)),
    core=Round(AluminumCladSteel, 1, inch(0.1217)),
)

SPOONBILL = B549(
    code_words=("Spoonbill",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 22, inch(0.1101)),
    core=Round(AluminumCladSteel, 7, inch(0.0612)),
)

SCAUP = B549(
    code_words=("Scaup",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 24, inch(0.1054)),
    core=Round(AluminumCladSteel, 7, inch(0.0703)),
)

DORKING = B549(
    code_words=("Dorking",),
    designation=Kcmil(190.8),
    outer=Round(Aluminum1350H19, 12, inch(0.1261)),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

PARTRIDGE = B549(
    code_words=("Partridge",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 26, inch(0.1013)),
    core=Round(AluminumCladSteel, 7, inch(0.0788)),
)

JUNCO = B549(
    code_words=("Junco",),
    designation=Kcmil(266.8),
    outer=Round(Aluminum1350H19, 30, inch(0.0943)),
    core=Round(AluminumCladSteel, 7, inch(0.0943)),
)

COCHIN = B549(
    code_words=("Cochin",),
    designation=Kcmil(211.3),
    outer=Round(Aluminum1350H19, 12, inch(0.1327)),
    core=Round(AluminumCladSteel, 7, inch(0.1327)),
)

OSTRICH = B549(
    code_words=("Ostrich",),
    designation=Kcmil(300),
    outer=Round(Aluminum1350H19, 26, inch(0.1074)),
    core=Round(AluminumCladSteel, 7, inch(0.0835)),
)

MERLIN = B549(
    code_words=("Merlin",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 18, inch(0.1367)),
    core=Round(AluminumCladSteel, 1, inch(0.1367)),
)

TROGON = B549(
    code_words=("Trogon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 20, inch(0.1297)),
    core=Round(AluminumCladSteel, 7, inch(0.0576)),
)

WOODCOCK = B549(
    code_words=("Woodcock",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 22, inch(0.1237)),
    core=Round(AluminumCladSteel, 7, inch(0.0687)),
)

WIDGEON = B549(
    code_words=("Widgeon",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 24, inch(0.1184)),
    core=Round(AluminumCladSteel, 7, inch(0.0789)),
)

BRAHMA = B549(
    code_words=("Brahma",),
    designation=Kcmil(203.2),
    outer=Round(Aluminum1350H19, 16, inch(0.1127)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

LINNET = B549(
    code_words=("Linnet",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 26, inch(0.1137)),
    core=Round(AluminumCladSteel, 7, inch(0.0884)),
)

ORIOLE = B549(
    code_words=("Oriole",),
    designation=Kcmil(336.4),
    outer=Round(Aluminum1350H19, 30, inch(0.1059)),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

CHICKADEE = B549(
    code_words=("Chickadee",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 18, inch(0.1486)),
    core=Round(AluminumCladSteel, 1, inch(0.1486)),
)

PTARMIGAN = B549(
    code_words=("Ptarmigan",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 20, inch(0.141)),
    core=Round(AluminumCladSteel, 7, inch(0.0627)),
)

STORK = B549(
    code_words=("Stork",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 22, inch(0.1344)),
    core=Round(AluminumCladSteel, 7, inch(0.0747)),
)

BRANT = B549(
    code_words=("Brant",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1287)),
    core=Round(AluminumCladSteel, 7, inch(0.0858)),
)

IBIS = B549(
    code_words=("Ibis",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1236)),
    core=Round(AluminumCladSteel, 7, inch(0.0961)),
)

LARK = B549(
    code_words=("Lark",),
    designation=Kcmil(397.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1151)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

PELICAN = B549(
    code_words=("Pelican",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 18, inch(0.1628)),
    core=Round(AluminumCladSteel, 1, inch(0.1628)),
)

TAILORBIRD = B549(
    code_words=("Tailorbird",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 20, inch(0.1544)),
    core=Round(AluminumCladSteel, 7, inch(0.0686)),
)

TOUCAN = B549(
    code_words=("Toucan",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 22, inch(0.1472)),
    core=Round(AluminumCladSteel, 7, inch(0.0818)),
)

FLICKER = B549(
    code_words=("Flicker",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 24, inch(0.141)),
    core=Round(AluminumCladSteel, 7, inch(0.094)),
)

HAWK = B549(
    code_words=("Hawk",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 26, inch(0.1354)),
    core=Round(AluminumCladSteel, 7, inch(0.1053)),
)

OSPREY = B549(
    code_words=("Osprey",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 18, inch(0.1758)),
    core=Round(AluminumCladSteel, 1, inch(0.1758)),
)

HEN = B549(
    code_words=("Hen",),
    designation=Kcmil(477),
    outer=Round(Aluminum1350H19, 30, inch(0.1261)),
    core=Round(AluminumCladSteel, 7, inch(0.1261)),
)

TODY = B549(
    code_words=("Tody",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 20, inch(0.1668)),
    core=Round(AluminumCladSteel, 7, inch(0.0741)),
)

SAPSUCKER = B549(
    code_words=("Sapsucker",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 22, inch(0.159)),
    core=Round(AluminumCladSteel, 7, inch(0.0883)),
)

HERON = B549(
    code_words=("Heron",),
    designation=Kcmil(500),
    outer=Round(Aluminum1350H19, 30, inch(0.1291)),
    core=Round(AluminumCladSteel, 7, inch(0.1291)),
)

PARAKEET = B549(
    code_words=("Parakeet",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1523)),
    core=Round(AluminumCladSteel, 7, inch(0.1015)),
)

DOVE = B549(
    code_words=("Dove",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1463)),
    core=Round(AluminumCladSteel, 7, inch(0.1138)),
)

SWIFT = B549(
    code_words=("Swift",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 36, inch(0.1329)),
    core=Round(AluminumCladSteel, 1, inch(0.1329)),
)

KINGBIRD = B549(
    code_words=("Kingbird",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 18, inch(0.188)),
    core=Round(AluminumCladSteel, 1, inch(0.188)),
)

TURACOS = B549(
    code_words=("Turacos",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 20, inch(0.1783)),
    core=Round(AluminumCladSteel, 7, inch(0.0792)),
)

DUCK = B549(
    code_words=("Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 54, inch(0.1058)),
    core=Round(AluminumCladSteel, 7, inch(0.1058)),
)

PEACOCK = B549(
    code_words=("Peacock",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 24, inch(0.1588)),
    core=Round(AluminumCladSteel, 7, inch(0.1059)),
)

EAGLE = B549(
    code_words=("Eagle",),
    designation=Kcmil(556.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1362)),
    core=Round(AluminumCladSteel, 7, inch(0.1362)),
)

GOLDFINCH = B549(
    code_words=("Goldfinch",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 22, inch(0.17)),
    core=Round(AluminumCladSteel, 7, inch(0.0944)),
)

SQUAB = B549(
    code_words=("Squab",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 26, inch(0.1525)),
    core=Round(AluminumCladSteel, 7, inch(0.1186)),
)

GOOSE = B549(
    code_words=("Goose",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 54, inch(0.1085)),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

ROOK = B549(
    code_words=("Rook",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 24, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

GROSBEAK = B549(
    code_words=("Grosbeak",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 26, inch(0.1564)),
    core=Round(AluminumCladSteel, 7, inch(0.1216)),
)

TEAL = B549(
    code_words=("Teal",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 30, inch(0.142)),
    core=Round(AluminumCladSteel, 19, inch(0.0852)),
)

WOOD_DUCK = B549(
    code_words=("Wood Duck",),
    designation=Kcmil(605),
    outer=Round(Aluminum1350H19, 30, inch(0.142)),
    core=Round(AluminumCladSteel, 7, inch(0.142)),
)

GULL = B549(
    code_words=("Gull",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 54, inch(0.1111)),
    core=Round(AluminumCladSteel, 7, inch(0.1111)),
)

FLAMINGO = B549(
    code_words=("Flamingo",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 24, inch(0.1667)),
    core=Round(AluminumCladSteel, 7, inch(0.1111)),
)

GANNET = B549(
    code_words=("Gannet",),
    designation=Kcmil(666.6),
    outer=Round(Aluminum1350H19, 26, inch(0.1601)),
    core=Round(AluminumCladSteel, 7, inch(0.1245)),
)

EGRET = B549(
    code_words=("Egret",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 30, inch(0.1456)),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

SCOTER = B549(
    code_words=("Scoter",),
    designation=Kcmil(636),
    outer=Round(Aluminum1350H19, 30, inch(0.1456)),
    core=Round(AluminumCladSteel, 7, inch(0.1456)),
)

CROW = B549(
    code_words=("Crow",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1151)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

STILT = B549(
    code_words=("Stilt",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 24, inch(0.1727)),
    core=Round(AluminumCladSteel, 7, inch(0.1151)),
)

COOT = B549(
    code_words=("Coot",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 36, inch(0.1486)),
    core=Round(AluminumCladSteel, 1, inch(0.1486)),
)

STARLING = B549(
    code_words=("Starling",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 26, inch(0.1659)),
    core=Round(AluminumCladSteel, 7, inch(0.129)),
)

MACAW = B549(
    code_words=("Macaw",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 42, inch(0.1376)),
    core=Round(AluminumCladSteel, 7, inch(0.0764)),
)

TERN = B549(
    code_words=("Tern",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 45, inch(0.1329)),
    core=Round(AluminumCladSteel, 7, inch(0.0886)),
)

TURBIT = B549(
    code_words=("Turbit",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 20, inch(0.1994)),
    core=Round(AluminumCladSteel, 7, inch(0.0886)),
)

PUFFIN = B549(
    code_words=("Puffin",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 22, inch(0.1901)),
    core=Round(AluminumCladSteel, 7, inch(0.1056)),
)

REDWING = B549(
    code_words=("Redwing",),
    designation=Kcmil(715.5),
    outer=Round(Aluminum1350H19, 30, inch(0.1544)),
    core=Round(AluminumCladSteel, 19, inch(0.0926)),
)

CONDOR = B549(
    code_words=("Condor",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 54, inch(0.1213)),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

CUCKOO = B549(
    code_words=("Cuckoo",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 24, inch(0.182)),
    core=Round(AluminumCladSteel, 7, inch(0.1213)),
)

DRAKE = B549(
    code_words=("Drake",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 26, inch(0.1749)),
    core=Round(AluminumCladSteel, 7, inch(0.136)),
)

RUDDY = B549(
    code_words=("Ruddy",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 45, inch(0.1414)),
    core=Round(AluminumCladSteel, 7, inch(0.0943)),
)

MALLARD = B549(
    code_words=("Mallard",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 30, inch(0.1628)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

SKIMMER = B549(
    code_words=("Skimmer",),
    designation=Kcmil(795),
    outer=Round(Aluminum1350H19, 30, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1628)),
)

CATBIRD = B549(
    code_words=("Catbird",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 36, inch(0.1628)),
    core=Round(AluminumCladSteel, 1, inch(0.1628)),
)

PHOENIX = B549(
    code_words=("Phoenix",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 42, inch(0.1507)),
    core=Round(AluminumCladSteel, 7, inch(0.0837)),
)

CANARY = B549(
    code_words=("Canary",),
    designation=Kcmil(900),
    outer=Round(Aluminum1350H19, 54, inch(0.1291)),
    core=Round(AluminumCladSteel, 7, inch(0.1291)),
)

CORNCRAKE = B549(
    code_words=("Corncrake",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 20, inch(0.2184)),
    core=Round(AluminumCladSteel, 7, inch(0.0971)),
)

RAIL = B549(
    code_words=("Rail",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 45, inch(0.1456)),
    core=Round(AluminumCladSteel, 7, inch(0.0971)),
)

TOWHEE = B549(
    code_words=("Towhee",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 48, inch(0.141)),
    core=Round(AluminumCladSteel, 7, inch(0.1097)),
)

TANAGER = B549(
    code_words=("Tanager",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 36, inch(0.1694)),
    core=Round(AluminumCladSteel, 1, inch(0.1694)),
)

CARDINAL = B549(
    code_words=("Cardinal",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 54, inch(0.1329)),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

REDBIRD = B549(
    code_words=("Redbird",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 24, inch(0.1994)),
    core=Round(AluminumCladSteel, 7, inch(0.1329)),
)

SNOWBIRD = B549(
    code_words=("Snowbird",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1569)),
    core=Round(AluminumCladSteel, 7, inch(0.0872)),
)

ORTOLAN = B549(
    code_words=("Ortolan",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1515)),
    core=Round(AluminumCladSteel, 7, inch(0.101)),
)

WHOOPER = B549(
    code_words=("Whooper",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1467)),
    core=Round(AluminumCladSteel, 7, inch(0.1141)),
)

CURLEW = B549(
    code_words=("Curlew",),
    designation=Kcmil(1033.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1383)),
    core=Round(AluminumCladSteel, 7, inch(0.1383)),
)

AVOCET = B549(
    code_words=("Avocet",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 42, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.0904)),
)

CANVASBACK = B549(
    code_words=("Canvasback",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 30, inch(0.1783)),
    core=Round(AluminumCladSteel, 19, inch(0.107)),
)

MERGANSER = B549(
    code_words=("Merganser",),
    designation=Kcmil(954),
    outer=Round(Aluminum1350H19, 30, inch(0.1783)),
    core=Round(AluminumCladSteel, 7, inch(0.1783)),
)

BLUEJAY = B549(
    code_words=("Bluejay",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 45, inch(0.1573)),
    core=Round(AluminumCladSteel, 7, inch(0.1049)),
)

BULLFINCH = B549(
    code_words=("Bullfinch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 48, inch(0.1523)),
    core=Round(AluminumCladSteel, 7, inch(0.1185)),
)

OXBIRD = B549(
    code_words=("Oxbird",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1685)),
    core=Round(AluminumCladSteel, 7, inch(0.0936)),
)

FINCH = B549(
    code_words=("Finch",),
    designation=Kcmil(1113),
    outer=Round(Aluminum1350H19, 54, inch(0.1436)),
    core=Round(AluminumCladSteel, 19, inch(0.0862)),
)

BUNTING = B549(
    code_words=("Bunting",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1085)),
)

CORMORANT = B549(
    code_words=("Cormorant",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1576)),
    core=Round(AluminumCladSteel, 7, inch(0.1226)),
)

SKYLARK = B549(
    code_words=("Skylark",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 36, inch(0.188)),
    core=Round(AluminumCladSteel, 1, inch(0.188)),
)

SCISSORTAIL = B549(
    code_words=("Scissortail",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 42, inch(0.174)),
    core=Round(AluminumCladSteel, 7, inch(0.0967)),
)

GRACKLE = B549(
    code_words=("Grackle",),
    designation=Kcmil(1192.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1486)),
    core=Round(AluminumCladSteel, 19, inch(0.0892)),
)

BITTERN = B549(
    code_words=("Bittern",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 45, inch(0.1681)),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

DIVER = B549(
    code_words=("Diver",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 48, inch(0.1628)),
    core=Round(AluminumCladSteel, 7, inch(0.1266)),
)

RINGDOVE = B549(
    code_words=("Ringdove",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 42, inch(0.1794)),
    core=Round(AluminumCladSteel, 7, inch(0.0997)),
)

PHEASANT = B549(
    code_words=("Pheasant",),
    designation=Kcmil(1272),
    outer=Round(Aluminum1350H19, 54, inch(0.1535)),
    core=Round(AluminumCladSteel, 19, inch(0.0921)),
)

DIPPER = B549(
    code_words=("Dipper",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1733)),
    core=Round(AluminumCladSteel, 7, inch(0.1155)),
)

KCMIL_1351_5_48_7 = B549(
    code_words=(),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 48, inch(0.1678)),
    core=Round(AluminumCladSteel, 7, inch(0.1305)),
)

POPINJAY = B549(
    code_words=("Popinjay",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 42, inch(0.1846)),
    core=Round(AluminumCladSteel, 7, inch(0.1026)),
)

MARTIN = B549(
    code_words=("Martin",),
    designation=Kcmil(1351.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1582)),
    core=Round(AluminumCladSteel, 19, inch(0.0949)),
)

BOBOLINK = B549(
    code_words=("Bobolink",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 45, inch(0.1783)),
    core=Round(AluminumCladSteel, 7, inch(0.1189)),
)

WAGTAIL = B549(
    code_words=("Wagtail",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 48, inch(0.1727)),
    core=Round(AluminumCladSteel, 7, inch(0.1343)),
)

PLOVER = B549(
    code_words=("Plover",),
    designation=Kcmil(1431),
    outer=Round(Aluminum1350H19, 54, inch(0.1628)),
    core=Round(AluminumCladSteel, 19, inch(0.0977)),
)

NUTHATCH = B549(
    code_words=("Nuthatch",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350H19, 45, inch(0.1832)),
    core=Round(AluminumCladSteel, 7, inch(0.1221)),
)

RATITE = B549(
    code_words=("Ratite",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 42, inch(0.1946)),
    core=Round(AluminumCladSteel, 7, inch(0.1081)),
)

LAPWING = B549(
    code_words=("Lapwing",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 45, inch(0.188)),
    core=Round(AluminumCladSteel, 7, inch(0.1253)),
)

PARROT = B549(
    code_words=("Parrot",),
    designation=Kcmil(1510.5),
    outer=Round(Aluminum1350H19, 54, inch(0.1672)),
    core=Round(AluminumCladSteel, 19, inch(0.1003)),
)

HORNBILL = B549(
    code_words=("Hornbill",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 48, inch(0.182)),
    core=Round(AluminumCladSteel, 7, inch(0.1416)),
)

FALCON = B549(
    code_words=("Falcon",),
    designation=Kcmil(1590),
    outer=Round(Aluminum1350H19, 54, inch(0.1716)),
    core=Round(AluminumCladSteel, 19, inch(0.103)),
)

WOODPECKER = B549(
    code_words=("Woodpecker",),
    designation=Kcmil(1843),
    outer=Round(Aluminum1350H19, 72, inch(0.16)),
    core=Round(AluminumCladSteel, 7, inch(0.1067)),
)

CHUKAR = B549(
    code_words=("Chukar",),
    designation=Kcmil(1780),
    outer=Round(Aluminum1350H19, 84, inch(0.1456)),
    core=Round(AluminumCladSteel, 19, inch(0.0874)),
)

SEAHAWK = B549(
    code_words=("Seahawk",),
    designation=Kcmil(1869),
    outer=Round(Aluminum1350H19, 68, inch(0.1658)),
    core=Round(AluminumCladSteel, 7, inch(0.0921)),
)

MOCKINGBIRD = B549(
    code_words=("Mockingbird",),
    designation=Kcmil(2034.5),
    outer=Round(Aluminum1350H19, 72, inch(0.1681)),
    core=Round(AluminumCladSteel, 7, inch(0.1121)),
)

ROADRUNNER = B549(
    code_words=("Roadrunner",),
    designation=Kcmil(2057.5),
    outer=Round(Aluminum1350H19, 76, inch(0.1645)),
    core=Round(AluminumCladSteel, 19, inch(0.0768)),
)

KIWI = B549(
    code_words=("Kiwi",),
    designation=Kcmil(2167),
    outer=Round(Aluminum1350H19, 72, inch(0.1735)),
    core=Round(AluminumCladSteel, 7, inch(0.1157)),
)

BLUEBIRD = B549(
    code_words=("Bluebird",),
    designation=Kcmil(2156),
    outer=Round(Aluminum1350H19, 84, inch(0.1602)),
    core=Round(AluminumCladSteel, 19, inch(0.0961)),
)

THRASHER = B549(
    code_words=("Thrasher",),
    designation=Kcmil(2312),
    outer=Round(Aluminum1350H19, 76, inch(0.1744)),
    core=Round(AluminumCladSteel, 19, inch(0.0814)),
)

JOREE = B549(
    code_words=("Joree",),
    designation=Kcmil(2515),
    outer=Round(Aluminum1350H19, 76, inch(0.1819)),
    core=Round(AluminumCladSteel, 19, inch(0.0849)),
)
