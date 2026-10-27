"""CAN/CSA C61089: ACSR, A1 aluminum around a core of zinc-coated steel, designated by code
number."""

from openline.types.conductors.csa import C61089
from openline.types.conductors.designations import Code
from openline.types.conductors.strands import Round
from openline.types.materials import HardDrawnAluminum, ZincCoatedSteel
from openline.types.units import mm

TURKEY = C61089(
    code_words=("Turkey",),
    designation=Code(13),
    outer=Round(HardDrawnAluminum, 6, mm(1.68)),
    core=Round(ZincCoatedSteel, 1, mm(1.68)),
)

SWAN = C61089(
    code_words=("Swan",),
    designation=Code(21),
    outer=Round(HardDrawnAluminum, 6, mm(2.12)),
    core=Round(ZincCoatedSteel, 1, mm(2.12)),
)

SWANATE = C61089(
    code_words=("Swanate",),
    designation=Code(21),
    outer=Round(HardDrawnAluminum, 7, mm(1.96)),
    core=Round(ZincCoatedSteel, 1, mm(2.61)),
)

SPARROW = C61089(
    code_words=("Sparrow",),
    designation=Code(34),
    outer=Round(HardDrawnAluminum, 6, mm(2.67)),
    core=Round(ZincCoatedSteel, 1, mm(2.67)),
)

SPARATE = C61089(
    code_words=("Sparate",),
    designation=Code(34),
    outer=Round(HardDrawnAluminum, 7, mm(2.47)),
    core=Round(ZincCoatedSteel, 1, mm(3.3)),
)

ROBIN = C61089(
    code_words=("Robin",),
    designation=Code(42),
    outer=Round(HardDrawnAluminum, 6, mm(3)),
    core=Round(ZincCoatedSteel, 1, mm(3)),
)

GROUSE = C61089(
    code_words=("Grouse",),
    designation=Code(41),
    outer=Round(HardDrawnAluminum, 8, mm(2.54)),
    core=Round(ZincCoatedSteel, 1, mm(4.24)),
)

RAVEN = C61089(
    code_words=("Raven",),
    designation=Code(54),
    outer=Round(HardDrawnAluminum, 6, mm(3.37)),
    core=Round(ZincCoatedSteel, 1, mm(3.37)),
)

QUAIL = C61089(
    code_words=("Quail",),
    designation=Code(67),
    outer=Round(HardDrawnAluminum, 6, mm(3.78)),
    core=Round(ZincCoatedSteel, 1, mm(3.78)),
)

PETREL = C61089(
    code_words=("Petrel",),
    designation=Code(52),
    outer=Round(HardDrawnAluminum, 12, mm(2.34)),
    core=Round(ZincCoatedSteel, 7, mm(2.34)),
)

MINORCA = C61089(
    code_words=("Minorca",),
    designation=Code(56),
    outer=Round(HardDrawnAluminum, 12, mm(2.44)),
    core=Round(ZincCoatedSteel, 7, mm(2.44)),
)

PIGEON = C61089(
    code_words=("Pigeon",),
    designation=Code(85),
    outer=Round(HardDrawnAluminum, 6, mm(4.25)),
    core=Round(ZincCoatedSteel, 1, mm(4.25)),
)

LEGHORN = C61089(
    code_words=("Leghorn",),
    designation=Code(68),
    outer=Round(HardDrawnAluminum, 12, mm(2.69)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

PENGUIN = C61089(
    code_words=("Penguin",),
    designation=Code(107),
    outer=Round(HardDrawnAluminum, 6, mm(4.77)),
    core=Round(ZincCoatedSteel, 1, mm(4.77)),
)

GUINEA = C61089(
    code_words=("Guinea",),
    designation=Code(81),
    outer=Round(HardDrawnAluminum, 12, mm(2.92)),
    core=Round(ZincCoatedSteel, 7, mm(2.92)),
)

AUK = C61089(
    code_words=("Auk",),
    designation=Code(103),
    outer=Round(HardDrawnAluminum, 8, mm(4.05)),
    core=Round(ZincCoatedSteel, 7, mm(2.25)),
)

DOTTEREL = C61089(
    code_words=("Dotterel",),
    designation=Code(90),
    outer=Round(HardDrawnAluminum, 12, mm(3.08)),
    core=Round(ZincCoatedSteel, 7, mm(3.08)),
)

WAXWING = C61089(
    code_words=("Waxwing",),
    designation=Code(135),
    outer=Round(HardDrawnAluminum, 18, mm(3.09)),
    core=Round(ZincCoatedSteel, 1, mm(3.09)),
)

SPOONBILL = C61089(
    code_words=("Spoonbill",),
    designation=Code(135),
    outer=Round(HardDrawnAluminum, 22, mm(2.8)),
    core=Round(ZincCoatedSteel, 7, mm(1.55)),
)

DORKING = C61089(
    code_words=("Dorking",),
    designation=Code(97),
    outer=Round(HardDrawnAluminum, 12, mm(3.2)),
    core=Round(ZincCoatedSteel, 7, mm(3.2)),
)

OWL = C61089(
    code_words=("Owl",),
    designation=Code(135),
    outer=Round(HardDrawnAluminum, 6, mm(5.36)),
    core=Round(ZincCoatedSteel, 7, mm(1.79)),
)

SCAUP = C61089(
    code_words=("Scaup",),
    designation=Code(135),
    outer=Round(HardDrawnAluminum, 24, mm(2.68)),
    core=Round(ZincCoatedSteel, 7, mm(1.79)),
)

PARTRIDGE = C61089(
    code_words=("Partridge",),
    designation=Code(135),
    outer=Round(HardDrawnAluminum, 26, mm(2.57)),
    core=Round(ZincCoatedSteel, 7, mm(2)),
)

PHOEBE = C61089(
    code_words=("Phoebe",),
    designation=Code(152),
    outer=Round(HardDrawnAluminum, 18, mm(3.28)),
    core=Round(ZincCoatedSteel, 1, mm(3.28)),
)

JUNCO = C61089(
    code_words=("Junco",),
    designation=Code(136),
    outer=Round(HardDrawnAluminum, 30, mm(2.4)),
    core=Round(ZincCoatedSteel, 7, mm(2.4)),
)

COCHIN = C61089(
    code_words=("Cochin",),
    designation=Code(107),
    outer=Round(HardDrawnAluminum, 12, mm(3.37)),
    core=Round(ZincCoatedSteel, 7, mm(3.37)),
)

OSTRICH = C61089(
    code_words=("Ostrich",),
    designation=Code(152),
    outer=Round(HardDrawnAluminum, 26, mm(2.73)),
    core=Round(ZincCoatedSteel, 7, mm(2.12)),
)

MERLIN = C61089(
    code_words=("Merlin",),
    designation=Code(171),
    outer=Round(HardDrawnAluminum, 18, mm(3.47)),
    core=Round(ZincCoatedSteel, 1, mm(3.47)),
)

WOODCOCK = C61089(
    code_words=("Woodcock",),
    designation=Code(171),
    outer=Round(HardDrawnAluminum, 22, mm(3.14)),
    core=Round(ZincCoatedSteel, 7, mm(1.74)),
)

PIPER = C61089(
    code_words=("Piper",),
    designation=Code(152),
    outer=Round(HardDrawnAluminum, 30, mm(2.54)),
    core=Round(ZincCoatedSteel, 7, mm(2.54)),
)

WIDGEON = C61089(
    code_words=("Widgeon",),
    designation=Code(171),
    outer=Round(HardDrawnAluminum, 24, mm(3.01)),
    core=Round(ZincCoatedSteel, 7, mm(2)),
)

BRAHMA = C61089(
    code_words=("Brahma",),
    designation=Code(103),
    outer=Round(HardDrawnAluminum, 16, mm(2.86)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)

LINNET = C61089(
    code_words=("Linnet",),
    designation=Code(170),
    outer=Round(HardDrawnAluminum, 26, mm(2.89)),
    core=Round(ZincCoatedSteel, 7, mm(2.25)),
)

ORIOLE = C61089(
    code_words=("Oriole",),
    designation=Code(171),
    outer=Round(HardDrawnAluminum, 30, mm(2.69)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

CHICKADEE = C61089(
    code_words=("Chickadee",),
    designation=Code(201),
    outer=Round(HardDrawnAluminum, 18, mm(3.77)),
    core=Round(ZincCoatedSteel, 1, mm(3.77)),
)

STORK = C61089(
    code_words=("Stork",),
    designation=Code(201),
    outer=Round(HardDrawnAluminum, 22, mm(3.41)),
    core=Round(ZincCoatedSteel, 7, mm(1.9)),
)

BRANT = C61089(
    code_words=("Brant",),
    designation=Code(202),
    outer=Round(HardDrawnAluminum, 24, mm(3.27)),
    core=Round(ZincCoatedSteel, 7, mm(2.18)),
)

IBIS = C61089(
    code_words=("Ibis",),
    designation=Code(201),
    outer=Round(HardDrawnAluminum, 26, mm(3.14)),
    core=Round(ZincCoatedSteel, 7, mm(2.44)),
)

LARK = C61089(
    code_words=("Lark",),
    designation=Code(201),
    outer=Round(HardDrawnAluminum, 30, mm(2.92)),
    core=Round(ZincCoatedSteel, 7, mm(2.92)),
)

PELICAN = C61089(
    code_words=("Pelican",),
    designation=Code(242),
    outer=Round(HardDrawnAluminum, 18, mm(4.13)),
    core=Round(ZincCoatedSteel, 1, mm(4.13)),
)

TOUCAN = C61089(
    code_words=("Toucan",),
    designation=Code(242),
    outer=Round(HardDrawnAluminum, 22, mm(3.74)),
    core=Round(ZincCoatedSteel, 7, mm(2.08)),
)

FLICKER = C61089(
    code_words=("Flicker",),
    designation=Code(242),
    outer=Round(HardDrawnAluminum, 24, mm(3.58)),
    core=Round(ZincCoatedSteel, 7, mm(2.39)),
)

HAWK = C61089(
    code_words=("Hawk",),
    designation=Code(242),
    outer=Round(HardDrawnAluminum, 26, mm(3.44)),
    core=Round(ZincCoatedSteel, 7, mm(2.67)),
)

SHELTER_BAY = C61089(
    code_words=("Shelter Bay",),
    designation=Code(255),
    outer=Round(HardDrawnAluminum, 22, mm(3.85)),
    core=Round(ZincCoatedSteel, 7, mm(2.14)),
)

HEN = C61089(
    code_words=("Hen",),
    designation=Code(242),
    outer=Round(HardDrawnAluminum, 30, mm(3.2)),
    core=Round(ZincCoatedSteel, 7, mm(3.2)),
)

OSPREY = C61089(
    code_words=("Osprey",),
    designation=Code(282),
    outer=Round(HardDrawnAluminum, 18, mm(4.47)),
    core=Round(ZincCoatedSteel, 1, mm(4.47)),
)

SAPSUCKER = C61089(
    code_words=("Sapsucker",),
    designation=Code(282),
    outer=Round(HardDrawnAluminum, 22, mm(4.04)),
    core=Round(ZincCoatedSteel, 7, mm(2.24)),
)

HERON = C61089(
    code_words=("Heron",),
    designation=Code(253),
    outer=Round(HardDrawnAluminum, 30, mm(3.28)),
    core=Round(ZincCoatedSteel, 7, mm(3.28)),
)

PARAKEET = C61089(
    code_words=("Parakeet",),
    designation=Code(282),
    outer=Round(HardDrawnAluminum, 24, mm(3.87)),
    core=Round(ZincCoatedSteel, 7, mm(2.58)),
)

CHIGNECTO = C61089(
    code_words=("Chignecto",),
    designation=Code(298),
    outer=Round(HardDrawnAluminum, 22, mm(4.16)),
    core=Round(ZincCoatedSteel, 7, mm(2.31)),
)

DOVE = C61089(
    code_words=("Dove",),
    designation=Code(282),
    outer=Round(HardDrawnAluminum, 26, mm(3.72)),
    core=Round(ZincCoatedSteel, 7, mm(2.89)),
)

TEAL = C61089(
    code_words=("Teal",),
    designation=Code(307),
    outer=Round(HardDrawnAluminum, 22, mm(4.21)),
    core=Round(ZincCoatedSteel, 7, mm(2.34)),
)

KINGBIRD = C61089(
    code_words=("Kingbird",),
    designation=Code(323),
    outer=Round(HardDrawnAluminum, 18, mm(4.78)),
    core=Round(ZincCoatedSteel, 1, mm(4.78)),
)

PEACE_RIVER = C61089(
    code_words=("Peace River",),
    designation=Code(317),
    outer=Round(HardDrawnAluminum, 48, mm(2.9)),
    core=Round(ZincCoatedSteel, 7, mm(2.25)),
)

PEACOCK = C61089(
    code_words=("Peacock",),
    designation=Code(306),
    outer=Round(HardDrawnAluminum, 24, mm(4.03)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

DUCK = C61089(
    code_words=("Duck",),
    designation=Code(307),
    outer=Round(HardDrawnAluminum, 54, mm(2.69)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

EAGLE = C61089(
    code_words=("Eagle",),
    designation=Code(282),
    outer=Round(HardDrawnAluminum, 30, mm(3.46)),
    core=Round(ZincCoatedSteel, 7, mm(3.46)),
)

GOLDFINCH = C61089(
    code_words=("Goldfinch",),
    designation=Code(322),
    outer=Round(HardDrawnAluminum, 22, mm(4.32)),
    core=Round(ZincCoatedSteel, 7, mm(2.4)),
)

CODE_338_42_7 = C61089(
    code_words=(),
    designation=Code(338),
    outer=Round(HardDrawnAluminum, 42, mm(3.2)),
    core=Round(ZincCoatedSteel, 7, mm(1.78)),
)

SQUAB = C61089(
    code_words=("Squab",),
    designation=Code(306),
    outer=Round(HardDrawnAluminum, 26, mm(3.87)),
    core=Round(ZincCoatedSteel, 7, mm(3.01)),
)

ROOK = C61089(
    code_words=("Rook",),
    designation=Code(323),
    outer=Round(HardDrawnAluminum, 24, mm(4.14)),
    core=Round(ZincCoatedSteel, 7, mm(2.76)),
)

GOOSE = C61089(
    code_words=("Goose",),
    designation=Code(322),
    outer=Round(HardDrawnAluminum, 54, mm(2.76)),
    core=Round(ZincCoatedSteel, 7, mm(2.76)),
)

GROSBEAK = C61089(
    code_words=("Grosbeak",),
    designation=Code(322),
    outer=Round(HardDrawnAluminum, 26, mm(3.97)),
    core=Round(ZincCoatedSteel, 7, mm(3.09)),
)

WOOD_DUCK = C61089(
    code_words=("Wood Duck",),
    designation=Code(307),
    outer=Round(HardDrawnAluminum, 30, mm(3.61)),
    core=Round(ZincCoatedSteel, 7, mm(3.61)),
)

GRAND_RAPID = C61089(
    code_words=("Grand Rapid",),
    designation=Code(347),
    outer=Round(HardDrawnAluminum, 22, mm(4.48)),
    core=Round(ZincCoatedSteel, 7, mm(2.49)),
)

GULL = C61089(
    code_words=("Gull",),
    designation=Code(338),
    outer=Round(HardDrawnAluminum, 54, mm(2.82)),
    core=Round(ZincCoatedSteel, 7, mm(2.82)),
)

FLAMINGO = C61089(
    code_words=("Flamingo", "Mica"),
    designation=Code(337),
    outer=Round(HardDrawnAluminum, 24, mm(4.23)),
    core=Round(ZincCoatedSteel, 7, mm(2.82)),
)

CODE_363_42_7 = C61089(
    code_words=(),
    designation=Code(363),
    outer=Round(HardDrawnAluminum, 42, mm(3.32)),
    core=Round(ZincCoatedSteel, 7, mm(1.84)),
)

GANNET = C61089(
    code_words=("Gannet",),
    designation=Code(338),
    outer=Round(HardDrawnAluminum, 26, mm(4.07)),
    core=Round(ZincCoatedSteel, 7, mm(3.16)),
)

EGRET = C61089(
    code_words=("Egret",),
    designation=Code(322),
    outer=Round(HardDrawnAluminum, 30, mm(3.7)),
    core=Round(ZincCoatedSteel, 19, mm(2.22)),
)

SCOTER = C61089(
    code_words=("Scoter",),
    designation=Code(323),
    outer=Round(HardDrawnAluminum, 30, mm(3.7)),
    core=Round(ZincCoatedSteel, 7, mm(3.7)),
)

CROW = C61089(
    code_words=("Crow",),
    designation=Code(363),
    outer=Round(HardDrawnAluminum, 54, mm(2.92)),
    core=Round(ZincCoatedSteel, 7, mm(2.92)),
)

STILT = C61089(
    code_words=("Stilt",),
    designation=Code(363),
    outer=Round(HardDrawnAluminum, 24, mm(4.39)),
    core=Round(ZincCoatedSteel, 7, mm(2.92)),
)

STARLING = C61089(
    code_words=("Starling",),
    designation=Code(363),
    outer=Round(HardDrawnAluminum, 26, mm(4.21)),
    core=Round(ZincCoatedSteel, 7, mm(3.28)),
)

MACAW = C61089(
    code_words=("Macaw",),
    designation=Code(403),
    outer=Round(HardDrawnAluminum, 42, mm(3.49)),
    core=Round(ZincCoatedSteel, 7, mm(1.94)),
)

TERN = C61089(
    code_words=("Tern",),
    designation=Code(404),
    outer=Round(HardDrawnAluminum, 45, mm(3.38)),
    core=Round(ZincCoatedSteel, 7, mm(2.25)),
)

PUFFIN = C61089(
    code_words=("Puffin",),
    designation=Code(403),
    outer=Round(HardDrawnAluminum, 22, mm(4.83)),
    core=Round(ZincCoatedSteel, 7, mm(2.68)),
)

REDWING = C61089(
    code_words=("Redwing",),
    designation=Code(363),
    outer=Round(HardDrawnAluminum, 30, mm(3.92)),
    core=Round(ZincCoatedSteel, 19, mm(2.35)),
)

CUCKOO = C61089(
    code_words=("Cuckoo",),
    designation=Code(402),
    outer=Round(HardDrawnAluminum, 24, mm(4.62)),
    core=Round(ZincCoatedSteel, 7, mm(3.08)),
)

CONDOR = C61089(
    code_words=("Condor",),
    designation=Code(403),
    outer=Round(HardDrawnAluminum, 54, mm(3.08)),
    core=Round(ZincCoatedSteel, 7, mm(3.08)),
)

CHUTE_DES_PASSES = C61089(
    code_words=("Chute Des Passes",),
    designation=Code(430),
    outer=Round(HardDrawnAluminum, 45, mm(3.49)),
    core=Round(ZincCoatedSteel, 7, mm(2.33)),
)

LES_BOULES = C61089(
    code_words=("Les Boules",),
    designation=Code(440),
    outer=Round(HardDrawnAluminum, 42, mm(3.65)),
    core=Round(ZincCoatedSteel, 7, mm(2.02)),
)

CODE_443_42_7 = C61089(
    code_words=(),
    designation=Code(443),
    outer=Round(HardDrawnAluminum, 42, mm(3.67)),
    core=Round(ZincCoatedSteel, 7, mm(2.04)),
)

DRAKE = C61089(
    code_words=("Drake",),
    designation=Code(403),
    outer=Round(HardDrawnAluminum, 26, mm(4.44)),
    core=Round(ZincCoatedSteel, 7, mm(3.45)),
)

CODE_456_42_7 = C61089(
    code_words=(),
    designation=Code(456),
    outer=Round(HardDrawnAluminum, 42, mm(3.72)),
    core=Round(ZincCoatedSteel, 7, mm(2.07)),
)

RUDDY = C61089(
    code_words=("Ruddy",),
    designation=Code(456),
    outer=Round(HardDrawnAluminum, 45, mm(3.59)),
    core=Round(ZincCoatedSteel, 7, mm(2.4)),
)

MALLARD = C61089(
    code_words=("Mallard",),
    designation=Code(403),
    outer=Round(HardDrawnAluminum, 30, mm(4.13)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)

CRANE = C61089(
    code_words=("Crane",),
    designation=Code(443),
    outer=Round(HardDrawnAluminum, 54, mm(3.23)),
    core=Round(ZincCoatedSteel, 7, mm(3.23)),
)

PHOENIX = C61089(
    code_words=("Phoenix",),
    designation=Code(483),
    outer=Round(HardDrawnAluminum, 42, mm(3.83)),
    core=Round(ZincCoatedSteel, 7, mm(2.13)),
)

CANARY = C61089(
    code_words=("Canary",),
    designation=Code(456),
    outer=Round(HardDrawnAluminum, 54, mm(3.28)),
    core=Round(ZincCoatedSteel, 7, mm(3.28)),
)

RAIL = C61089(
    code_words=("Rail",),
    designation=Code(484),
    outer=Round(HardDrawnAluminum, 45, mm(3.7)),
    core=Round(ZincCoatedSteel, 7, mm(2.47)),
)

TOWHEE = C61089(
    code_words=("Towhee",),
    designation=Code(483),
    outer=Round(HardDrawnAluminum, 48, mm(3.58)),
    core=Round(ZincCoatedSteel, 7, mm(2.79)),
)

REDBIRD = C61089(
    code_words=("Redbird",),
    designation=Code(483),
    outer=Round(HardDrawnAluminum, 24, mm(5.06)),
    core=Round(ZincCoatedSteel, 7, mm(3.38)),
)

CARDINAL = C61089(
    code_words=("Cardinal",),
    designation=Code(483),
    outer=Round(HardDrawnAluminum, 54, mm(3.38)),
    core=Round(ZincCoatedSteel, 7, mm(3.38)),
)

SNOWBIRD = C61089(
    code_words=("Snowbird", "Carillon"),
    designation=Code(524),
    outer=Round(HardDrawnAluminum, 42, mm(3.98)),
    core=Round(ZincCoatedSteel, 7, mm(2.21)),
)

ORTOLAN = C61089(
    code_words=("Ortolan",),
    designation=Code(524),
    outer=Round(HardDrawnAluminum, 45, mm(3.85)),
    core=Round(ZincCoatedSteel, 7, mm(2.57)),
)

WHOOPER = C61089(
    code_words=("Whooper",),
    designation=Code(525),
    outer=Round(HardDrawnAluminum, 48, mm(3.73)),
    core=Round(ZincCoatedSteel, 7, mm(2.9)),
)

CURLEW = C61089(
    code_words=("Curlew",),
    designation=Code(524),
    outer=Round(HardDrawnAluminum, 54, mm(3.51)),
    core=Round(ZincCoatedSteel, 7, mm(3.51)),
)

BEAUMONT = C61089(
    code_words=("Beaumont",),
    designation=Code(564),
    outer=Round(HardDrawnAluminum, 42, mm(4.13)),
    core=Round(ZincCoatedSteel, 7, mm(2.3)),
)

BULLFINCH = C61089(
    code_words=("Bullfinch",),
    designation=Code(564),
    outer=Round(HardDrawnAluminum, 48, mm(3.87)),
    core=Round(ZincCoatedSteel, 7, mm(3.01)),
)

OXBIRD = C61089(
    code_words=("Oxbird",),
    designation=Code(604),
    outer=Round(HardDrawnAluminum, 42, mm(4.28)),
    core=Round(ZincCoatedSteel, 7, mm(2.38)),
)

FINCH = C61089(
    code_words=("Finch",),
    designation=Code(564),
    outer=Round(HardDrawnAluminum, 54, mm(3.65)),
    core=Round(ZincCoatedSteel, 19, mm(2.19)),
)

GATINEAU = C61089(
    code_words=("Gatineau",),
    designation=Code(591),
    outer=Round(HardDrawnAluminum, 48, mm(3.96)),
    core=Round(ZincCoatedSteel, 7, mm(3.08)),
)

BUNTING = C61089(
    code_words=("Bunting",),
    designation=Code(606),
    outer=Round(HardDrawnAluminum, 45, mm(4.14)),
    core=Round(ZincCoatedSteel, 7, mm(2.76)),
)

CORMORANT = C61089(
    code_words=("Cormorant",),
    designation=Code(603),
    outer=Round(HardDrawnAluminum, 48, mm(4)),
    core=Round(ZincCoatedSteel, 7, mm(3.11)),
)

SCISSORTAIL = C61089(
    code_words=("Scissortail",),
    designation=Code(645),
    outer=Round(HardDrawnAluminum, 42, mm(4.42)),
    core=Round(ZincCoatedSteel, 7, mm(2.46)),
)

GRACKLE = C61089(
    code_words=("Grackle",),
    designation=Code(604),
    outer=Round(HardDrawnAluminum, 54, mm(3.77)),
    core=Round(ZincCoatedSteel, 19, mm(2.27)),
)

SEAWAY = C61089(
    code_words=("Seaway",),
    designation=Code(647),
    outer=Round(HardDrawnAluminum, 42, mm(4.43)),
    core=Round(ZincCoatedSteel, 7, mm(2.46)),
)

BITTERN = C61089(
    code_words=("Bittern",),
    designation=Code(644),
    outer=Round(HardDrawnAluminum, 45, mm(4.27)),
    core=Round(ZincCoatedSteel, 7, mm(2.85)),
)

DIVER = C61089(
    code_words=("Diver",),
    designation=Code(646),
    outer=Round(HardDrawnAluminum, 48, mm(4.14)),
    core=Round(ZincCoatedSteel, 7, mm(3.22)),
)

RINGDOVE = C61089(
    code_words=("Ringdove",),
    designation=Code(685),
    outer=Round(HardDrawnAluminum, 42, mm(4.56)),
    core=Round(ZincCoatedSteel, 7, mm(2.53)),
)

BERSIMIS = C61089(
    code_words=("Bersimis",),
    designation=Code(689),
    outer=Round(HardDrawnAluminum, 42, mm(4.57)),
    core=Round(ZincCoatedSteel, 7, mm(2.54)),
)

PHEASANT = C61089(
    code_words=("Pheasant",),
    designation=Code(645),
    outer=Round(HardDrawnAluminum, 54, mm(3.9)),
    core=Round(ZincCoatedSteel, 19, mm(2.34)),
)

DIPPER = C61089(
    code_words=("Dipper",),
    designation=Code(685),
    outer=Round(HardDrawnAluminum, 45, mm(4.4)),
    core=Round(ZincCoatedSteel, 7, mm(2.93)),
)

CODE_685_48_7 = C61089(
    code_words=(),
    designation=Code(685),
    outer=Round(HardDrawnAluminum, 48, mm(4.26)),
    core=Round(ZincCoatedSteel, 7, mm(3.31)),
)

BERSFORT = C61089(
    code_words=("Bersfort",),
    designation=Code(687),
    outer=Round(HardDrawnAluminum, 48, mm(4.27)),
    core=Round(ZincCoatedSteel, 7, mm(3.32)),
)

POPINJAY = C61089(
    code_words=("Popinjay",),
    designation=Code(726),
    outer=Round(HardDrawnAluminum, 42, mm(4.69)),
    core=Round(ZincCoatedSteel, 7, mm(2.61)),
)

MARTIN = C61089(
    code_words=("Martin",),
    designation=Code(685),
    outer=Round(HardDrawnAluminum, 54, mm(4.02)),
    core=Round(ZincCoatedSteel, 19, mm(2.41)),
)

BOBOLINK = C61089(
    code_words=("Bobolink",),
    designation=Code(725),
    outer=Round(HardDrawnAluminum, 45, mm(4.53)),
    core=Round(ZincCoatedSteel, 7, mm(3.02)),
)

WAGTAIL = C61089(
    code_words=("Wagtail",),
    designation=Code(727),
    outer=Round(HardDrawnAluminum, 48, mm(4.39)),
    core=Round(ZincCoatedSteel, 7, mm(3.41)),
)

CODE_765_42_7 = C61089(
    code_words=(),
    designation=Code(765),
    outer=Round(HardDrawnAluminum, 42, mm(4.82)),
    core=Round(ZincCoatedSteel, 7, mm(2.67)),
)

PLOVER = C61089(
    code_words=("Plover",),
    designation=Code(725),
    outer=Round(HardDrawnAluminum, 54, mm(4.13)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)

NUTHATCH = C61089(
    code_words=("Nuthatch",),
    designation=Code(765),
    outer=Round(HardDrawnAluminum, 45, mm(4.65)),
    core=Round(ZincCoatedSteel, 7, mm(3.1)),
)

CODE_806_72_7 = C61089(
    code_words=(),
    designation=Code(806),
    outer=Round(HardDrawnAluminum, 72, mm(3.77)),
    core=Round(ZincCoatedSteel, 7, mm(2.52)),
)

RATITE = C61089(
    code_words=("Ratite",),
    designation=Code(806),
    outer=Round(HardDrawnAluminum, 42, mm(4.94)),
    core=Round(ZincCoatedSteel, 7, mm(2.75)),
)

LAPWING = C61089(
    code_words=("Lapwing",),
    designation=Code(806),
    outer=Round(HardDrawnAluminum, 45, mm(4.77)),
    core=Round(ZincCoatedSteel, 7, mm(3.18)),
)

PARROT = C61089(
    code_words=("Parrot",),
    designation=Code(765),
    outer=Round(HardDrawnAluminum, 54, mm(4.25)),
    core=Round(ZincCoatedSteel, 19, mm(2.55)),
)

HORNBILL = C61089(
    code_words=("Hornbill",),
    designation=Code(806),
    outer=Round(HardDrawnAluminum, 48, mm(4.62)),
    core=Round(ZincCoatedSteel, 7, mm(3.6)),
)

FALCON = C61089(
    code_words=("Falcon",),
    designation=Code(806),
    outer=Round(HardDrawnAluminum, 54, mm(4.36)),
    core=Round(ZincCoatedSteel, 19, mm(2.62)),
)

NELSON = C61089(
    code_words=("Nelson",),
    designation=Code(932),
    outer=Round(HardDrawnAluminum, 72, mm(4.06)),
    core=Round(ZincCoatedSteel, 7, mm(2.71)),
)

SEAHAWK = C61089(
    code_words=("Seahawk",),
    designation=Code(947),
    outer=Round(HardDrawnAluminum, 68, mm(4.21)),
    core=Round(ZincCoatedSteel, 7, mm(2.34)),
)

CHUKAR = C61089(
    code_words=("Chukar",),
    designation=Code(902),
    outer=Round(HardDrawnAluminum, 84, mm(3.7)),
    core=Round(ZincCoatedSteel, 19, mm(2.22)),
)

MOCKINGBIRD = C61089(
    code_words=("Mockingbird",),
    designation=Code(1031),
    outer=Round(HardDrawnAluminum, 72, mm(4.27)),
    core=Round(ZincCoatedSteel, 7, mm(2.85)),
)

ROADRUNNER = C61089(
    code_words=("Roadrunner",),
    designation=Code(1043),
    outer=Round(HardDrawnAluminum, 76, mm(4.18)),
    core=Round(ZincCoatedSteel, 19, mm(1.95)),
)

KIWI = C61089(
    code_words=("Kiwi",),
    designation=Code(1098),
    outer=Round(HardDrawnAluminum, 72, mm(4.41)),
    core=Round(ZincCoatedSteel, 7, mm(2.94)),
)

BLUEBIRD = C61089(
    code_words=("Bluebird",),
    designation=Code(1092),
    outer=Round(HardDrawnAluminum, 84, mm(4.07)),
    core=Round(ZincCoatedSteel, 19, mm(2.44)),
)

THRASHER = C61089(
    code_words=("Thrasher",),
    designation=Code(1172),
    outer=Round(HardDrawnAluminum, 76, mm(4.43)),
    core=Round(ZincCoatedSteel, 19, mm(2.07)),
)

JOREE = C61089(
    code_words=("Joree",),
    designation=Code(1274),
    outer=Round(HardDrawnAluminum, 76, mm(4.62)),
    core=Round(ZincCoatedSteel, 19, mm(2.16)),
)

MICA = FLAMINGO
CARILLON = SNOWBIRD
