"""ASTM B231: Aluminum 1350, round wires, of class AA, A or both."""

from openline.types.conductors.astm import B231
from openline.types.conductors.designations import Gauge, Kcmil, Mm2
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum1350H19
from openline.types.units import inch, mm

PEACHBELL = B231(
    code_words=("Peachbell",),
    designation=Gauge(6),
    wires=Round(Aluminum1350H19, 7, inch(0.0612)),
    classes=("A",),
)

ROSE = B231(
    code_words=("Rose",),
    designation=Gauge(4),
    wires=Round(Aluminum1350H19, 7, inch(0.0772)),
    classes=("A",),
)

IRIS = B231(
    code_words=("Iris",),
    designation=Gauge(2),
    wires=Round(Aluminum1350H19, 7, inch(0.0974)),
    classes=("A", "AA"),
)

PANSY = B231(
    code_words=("Pansy",),
    designation=Gauge(1),
    wires=Round(Aluminum1350H19, 7, inch(0.1093)),
    classes=("A", "AA"),
)

POPPY = B231(
    code_words=("Poppy",),
    designation=Gauge(0),
    wires=Round(Aluminum1350H19, 7, inch(0.1228)),
    classes=("A", "AA"),
)

ASTER = B231(
    code_words=("Aster",),
    designation=Gauge(-1),
    wires=Round(Aluminum1350H19, 7, inch(0.1379)),
    classes=("A", "AA"),
)

PHLOX = B231(
    code_words=("Phlox",),
    designation=Gauge(-2),
    wires=Round(Aluminum1350H19, 7, inch(0.1548)),
    classes=("A", "AA"),
)

OXLIP = B231(
    code_words=("Oxlip",),
    designation=Gauge(-3),
    wires=Round(Aluminum1350H19, 7, inch(0.1739)),
    classes=("A", "AA"),
)

MM2_125_7 = B231(
    code_words=(), designation=Mm2(125), wires=Round(Aluminum1350H19, 7, mm(4.77)), classes=("AA",)
)

VALERIAN = B231(
    code_words=("Valerian",),
    designation=Kcmil(250),
    wires=Round(Aluminum1350H19, 19, inch(0.1147)),
    classes=("A",),
)

SNEEZEWORT = B231(
    code_words=("Sneezewort",),
    designation=Kcmil(250),
    wires=Round(Aluminum1350H19, 7, inch(0.189)),
    classes=("AA",),
)

LAUREL = B231(
    code_words=("Laurel",),
    designation=Kcmil(266.8),
    wires=Round(Aluminum1350H19, 19, inch(0.1185)),
    classes=("A",),
)

DAISY = B231(
    code_words=("Daisy",),
    designation=Kcmil(266.8),
    wires=Round(Aluminum1350H19, 7, inch(0.1953)),
    classes=("AA",),
)

MM2_140_19 = B231(
    code_words=(), designation=Mm2(140), wires=Round(Aluminum1350H19, 19, mm(3.06)), classes=("A",)
)

MM2_140_7 = B231(
    code_words=(), designation=Mm2(140), wires=Round(Aluminum1350H19, 7, mm(5.05)), classes=("AA",)
)

PEONY = B231(
    code_words=("Peony",),
    designation=Kcmil(300),
    wires=Round(Aluminum1350H19, 19, inch(0.1257)),
    classes=("A",),
)

MM2_160_19 = B231(
    code_words=(), designation=Mm2(160), wires=Round(Aluminum1350H19, 19, mm(3.27)), classes=("A",)
)

TULIP = B231(
    code_words=("Tulip",),
    designation=Kcmil(336.4),
    wires=Round(Aluminum1350H19, 19, inch(0.1331)),
    classes=("A",),
)

DAFFODIL = B231(
    code_words=("Daffodil",),
    designation=Kcmil(350),
    wires=Round(Aluminum1350H19, 19, inch(0.1357)),
    classes=("A",),
)

MM2_180_19 = B231(
    code_words=(), designation=Mm2(180), wires=Round(Aluminum1350H19, 19, mm(3.47)), classes=("A",)
)

MM2_200_19 = B231(
    code_words=(),
    designation=Mm2(200),
    wires=Round(Aluminum1350H19, 19, mm(3.66)),
    classes=("A", "AA"),
)

CANNA = B231(
    code_words=("Canna",),
    designation=Kcmil(397.5),
    wires=Round(Aluminum1350H19, 19, inch(0.1447)),
    classes=("A", "AA"),
)

MM2_224_19 = B231(
    code_words=(), designation=Mm2(224), wires=Round(Aluminum1350H19, 19, mm(3.87)), classes=("AA",)
)

GOLDENTUFT = B231(
    code_words=("Goldentuft",),
    designation=Kcmil(450),
    wires=Round(Aluminum1350H19, 19, inch(0.1539)),
    classes=("AA",),
)

SYRINGA = B231(
    code_words=("Syringa",),
    designation=Kcmil(477),
    wires=Round(Aluminum1350H19, 37, inch(0.1135)),
    classes=("A",),
)

COSMOS = B231(
    code_words=("Cosmos",),
    designation=Kcmil(477),
    wires=Round(Aluminum1350H19, 19, inch(0.1584)),
    classes=("AA",),
)

MM2_250_37 = B231(
    code_words=(), designation=Mm2(250), wires=Round(Aluminum1350H19, 37, mm(2.93)), classes=("A",)
)

MM2_250_19 = B231(
    code_words=(), designation=Mm2(250), wires=Round(Aluminum1350H19, 19, mm(4.09)), classes=("AA",)
)

HYACINTH = B231(
    code_words=("Hyacinth",),
    designation=Kcmil(500),
    wires=Round(Aluminum1350H19, 37, inch(0.1162)),
    classes=("A",),
)

ZINNIA = B231(
    code_words=("Zinnia",),
    designation=Kcmil(500),
    wires=Round(Aluminum1350H19, 19, inch(0.1622)),
    classes=("AA",),
)

MM2_280_37 = B231(
    code_words=(), designation=Mm2(280), wires=Round(Aluminum1350H19, 37, mm(3.1)), classes=("A",)
)

MM2_280_19 = B231(
    code_words=(), designation=Mm2(280), wires=Round(Aluminum1350H19, 19, mm(4.33)), classes=("AA",)
)

MISTLETOE = B231(
    code_words=("Mistletoe",),
    designation=Kcmil(556.5),
    wires=Round(Aluminum1350H19, 37, inch(0.1226)),
    classes=("A",),
)

DAHLIA = B231(
    code_words=("Dahlia",),
    designation=Kcmil(556.5),
    wires=Round(Aluminum1350H19, 19, inch(0.1711)),
    classes=("AA",),
)

MEADOWSWEET = B231(
    code_words=("Meadowsweet",),
    designation=Kcmil(600),
    wires=Round(Aluminum1350H19, 37, inch(0.1273)),
    classes=("A", "AA"),
)

MM2_315_37 = B231(
    code_words=(),
    designation=Mm2(315),
    wires=Round(Aluminum1350H19, 37, mm(3.29)),
    classes=("A", "AA"),
)

ORCHID = B231(
    code_words=("Orchid",),
    designation=Kcmil(636),
    wires=Round(Aluminum1350H19, 37, inch(0.1311)),
    classes=("A", "AA"),
)

HEUCHERA = B231(
    code_words=("Heuchera",),
    designation=Kcmil(650),
    wires=Round(Aluminum1350H19, 37, inch(0.1326)),
    classes=("AA",),
)

VERBENA = B231(
    code_words=("Verbena",),
    designation=Kcmil(700),
    wires=Round(Aluminum1350H19, 37, inch(0.1375)),
    classes=("AA",),
)

FLAG = B231(
    code_words=("Flag",),
    designation=Kcmil(700),
    wires=Round(Aluminum1350H19, 61, inch(0.1071)),
    classes=("A",),
)

MM2_355_37 = B231(
    code_words=(), designation=Mm2(355), wires=Round(Aluminum1350H19, 37, mm(3.5)), classes=("AA",)
)

NASTURTIUM = B231(
    code_words=("Nasturtium",),
    designation=Kcmil(715.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1083)),
    classes=("A",),
)

VIOLET = B231(
    code_words=("Violet",),
    designation=Kcmil(715.5),
    wires=Round(Aluminum1350H19, 37, inch(0.1391)),
    classes=("AA",),
)

CATTAIL = B231(
    code_words=("Cattail",),
    designation=Kcmil(750),
    wires=Round(Aluminum1350H19, 61, inch(0.1109)),
    classes=("A",),
)

PETUNIA = B231(
    code_words=("Petunia",),
    designation=Kcmil(750),
    wires=Round(Aluminum1350H19, 37, inch(0.1424)),
    classes=("AA",),
)

MM2_400_37 = B231(
    code_words=(), designation=Mm2(400), wires=Round(Aluminum1350H19, 37, mm(3.71)), classes=("AA",)
)

MM2_400_61 = B231(
    code_words=(), designation=Mm2(400), wires=Round(Aluminum1350H19, 61, mm(2.89)), classes=("A",)
)

ARBUTUS = B231(
    code_words=("Arbutus",),
    designation=Kcmil(795),
    wires=Round(Aluminum1350H19, 37, inch(0.1466)),
    classes=("AA",),
)

LILAC = B231(
    code_words=("Lilac",),
    designation=Kcmil(795),
    wires=Round(Aluminum1350H19, 61, inch(0.1142)),
    classes=("A",),
)

FUCHSIA = B231(
    code_words=("Fuchsia",),
    designation=Kcmil(800),
    wires=Round(Aluminum1350H19, 37, inch(0.147)),
    classes=("AA",),
)

HELIOTROPE = B231(
    code_words=("Heliotrope",),
    designation=Kcmil(800),
    wires=Round(Aluminum1350H19, 61, inch(0.1145)),
    classes=("A",),
)

CROCUS = B231(
    code_words=("Crocus",),
    designation=Kcmil(874.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1197)),
    classes=("A",),
)

ANEMONE = B231(
    code_words=("Anemone",),
    designation=Kcmil(874.5),
    wires=Round(Aluminum1350H19, 37, inch(0.1537)),
    classes=("AA",),
)

MM2_450_61 = B231(
    code_words=(), designation=Mm2(450), wires=Round(Aluminum1350H19, 61, mm(3.06)), classes=("A",)
)

MM2_450_37 = B231(
    code_words=(), designation=Mm2(450), wires=Round(Aluminum1350H19, 37, mm(3.94)), classes=("AA",)
)

COCKSCOMB = B231(
    code_words=("Cockscomb",),
    designation=Kcmil(900),
    wires=Round(Aluminum1350H19, 37, inch(0.156)),
    classes=("AA",),
)

SNAPDRAGON = B231(
    code_words=("Snapdragon",),
    designation=Kcmil(900),
    wires=Round(Aluminum1350H19, 61, inch(0.1215)),
    classes=("A",),
)

MAGNOLIA = B231(
    code_words=("Magnolia",),
    designation=Kcmil(954),
    wires=Round(Aluminum1350H19, 37, inch(0.1606)),
    classes=("AA",),
)

GOLDENROD = B231(
    code_words=("Goldenrod",),
    designation=Kcmil(954),
    wires=Round(Aluminum1350H19, 61, inch(0.1251)),
    classes=("A",),
)

MM2_500_61 = B231(
    code_words=(), designation=Mm2(500), wires=Round(Aluminum1350H19, 61, mm(3.23)), classes=("A",)
)

MM2_500_37 = B231(
    code_words=(), designation=Mm2(500), wires=Round(Aluminum1350H19, 37, mm(4.15)), classes=("AA",)
)

CAMELLIA = B231(
    code_words=("Camellia",),
    designation=Kcmil(1000),
    wires=Round(Aluminum1350H19, 61, inch(0.128)),
    classes=("A",),
)

HAWKWEED = B231(
    code_words=("Hawkweed",),
    designation=Kcmil(1000),
    wires=Round(Aluminum1350H19, 37, inch(0.1644)),
    classes=("AA",),
)

BLUEBELL = B231(
    code_words=("Bluebell",),
    designation=Kcmil(1033.5),
    wires=Round(Aluminum1350H19, 37, inch(0.1671)),
    classes=("AA",),
)

LARKSPUR = B231(
    code_words=("Larkspur",),
    designation=Kcmil(1033.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1302)),
    classes=("A",),
)

MM2_560_61 = B231(
    code_words=(),
    designation=Mm2(560),
    wires=Round(Aluminum1350H19, 61, mm(3.42)),
    classes=("A", "AA"),
)

MARIGOLD = B231(
    code_words=("Marigold",),
    designation=Kcmil(1113),
    wires=Round(Aluminum1350H19, 61, inch(0.1351)),
    classes=("A", "AA"),
)

HAWTHORN = B231(
    code_words=("Hawthorn",),
    designation=Kcmil(1192.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1398)),
    classes=("A", "AA"),
)

MM2_630_61 = B231(
    code_words=(),
    designation=Mm2(630),
    wires=Round(Aluminum1350H19, 61, mm(3.63)),
    classes=("A", "AA"),
)

NARCISSUS = B231(
    code_words=("Narcissus",),
    designation=Kcmil(1272),
    wires=Round(Aluminum1350H19, 61, inch(0.1444)),
    classes=("A", "AA"),
)

COLUMBINE = B231(
    code_words=("Columbine",),
    designation=Kcmil(1351.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1488)),
    classes=("A", "AA"),
)

MM2_710_61 = B231(
    code_words=(),
    designation=Mm2(710),
    wires=Round(Aluminum1350H19, 61, mm(3.85)),
    classes=("A", "AA"),
)

CARNATION = B231(
    code_words=("Carnation",),
    designation=Kcmil(1431),
    wires=Round(Aluminum1350H19, 61, inch(0.1532)),
    classes=("A", "AA"),
)

GLADIOLUS = B231(
    code_words=("Gladiolus",),
    designation=Kcmil(1510.5),
    wires=Round(Aluminum1350H19, 61, inch(0.1574)),
    classes=("A", "AA"),
)

MM2_800_61 = B231(
    code_words=(),
    designation=Mm2(800),
    wires=Round(Aluminum1350H19, 61, mm(4.09)),
    classes=("A", "AA"),
)

COREOPSIS = B231(
    code_words=("Coreopsis",),
    designation=Kcmil(1590),
    wires=Round(Aluminum1350H19, 61, inch(0.1614)),
    classes=("AA",),
)

JESSAMINE = B231(
    code_words=("Jessamine",),
    designation=Kcmil(1750),
    wires=Round(Aluminum1350H19, 61, inch(0.1694)),
    classes=("AA",),
)

MM2_900_61 = B231(
    code_words=(), designation=Mm2(900), wires=Round(Aluminum1350H19, 61, mm(4.33)), classes=("AA",)
)

MM2_1000_91 = B231(
    code_words=(), designation=Mm2(1000), wires=Round(Aluminum1350H19, 91, mm(3.74)), classes=("A",)
)

COWSLIP = B231(
    code_words=("Cowslip",),
    designation=Kcmil(2000),
    wires=Round(Aluminum1350H19, 91, inch(0.1482)),
    classes=("A",),
)

MM2_1120_91 = B231(
    code_words=(), designation=Mm2(1120), wires=Round(Aluminum1350H19, 91, mm(3.96)), classes=("A",)
)

SAGEBRUSH = B231(
    code_words=("Sagebrush",),
    designation=Kcmil(2250),
    wires=Round(Aluminum1350H19, 91, inch(0.1572)),
    classes=("A",),
)

PIGWEED = B231(
    code_words=("Pigweed",),
    designation=Kcmil(2300),
    wires=Round(Aluminum1350H19, 61, inch(0.1942)),
    classes=("A",),
)

MM2_1250_91 = B231(
    code_words=(), designation=Mm2(1250), wires=Round(Aluminum1350H19, 91, mm(4.18)), classes=("A",)
)

LUPINE = B231(
    code_words=("Lupine",),
    designation=Kcmil(2500),
    wires=Round(Aluminum1350H19, 91, inch(0.1657)),
    classes=("A",),
)

BITTEROOT = B231(
    code_words=("Bitteroot", "Bitterroot"),
    designation=Kcmil(2750),
    wires=Round(Aluminum1350H19, 91, inch(0.1738)),
    classes=("A",),
)

TRILLIUM = B231(
    code_words=("Trillium",),
    designation=Kcmil(3000),
    wires=Round(Aluminum1350H19, 127, inch(0.1537)),
    classes=("A",),
)

MM2_1600_127 = B231(
    code_words=(),
    designation=Mm2(1600),
    wires=Round(Aluminum1350H19, 127, mm(4.01)),
    classes=("A",),
)

BLUEBONNET = B231(
    code_words=("Bluebonnet",),
    designation=Kcmil(3500),
    wires=Round(Aluminum1350H19, 127, inch(0.166)),
    classes=("A",),
)

MM2_2000_127 = B231(
    code_words=(),
    designation=Mm2(2000),
    wires=Round(Aluminum1350H19, 127, mm(4.48)),
    classes=("A",),
)

BITTERROOT = BITTEROOT
