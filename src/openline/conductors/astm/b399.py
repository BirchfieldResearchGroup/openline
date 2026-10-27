"""ASTM B399: Aluminum alloy 6201-T81, round wires, of class AA, A or both."""

from openline.types.conductors.astm import B399
from openline.types.conductors.designations import Kcmil
from openline.types.conductors.strands import Round
from openline.types.materials import Aluminum6201T81
from openline.types.units import inch

KCMIL_26_24_7 = B399(
    code_words=(),
    designation=Kcmil(26.24),
    wires=Round(Aluminum6201T81, 7, inch(0.0612)),
    classes=("A",),
)

AKRON = B399(
    code_words=("Akron",),
    designation=Kcmil(30.58),
    wires=Round(Aluminum6201T81, 7, inch(0.0661)),
    classes=("A",),
)

KCMIL_41_74_7 = B399(
    code_words=(),
    designation=Kcmil(41.74),
    wires=Round(Aluminum6201T81, 7, inch(0.0772)),
    classes=("A",),
)

ALTON = B399(
    code_words=("Alton",),
    designation=Kcmil(48.69),
    wires=Round(Aluminum6201T81, 7, inch(0.0834)),
    classes=("A",),
)

KCMIL_66_36_7 = B399(
    code_words=(),
    designation=Kcmil(66.36),
    wires=Round(Aluminum6201T81, 7, inch(0.0974)),
    classes=("A", "AA"),
)

AMES = B399(
    code_words=("Ames",),
    designation=Kcmil(77.47),
    wires=Round(Aluminum6201T81, 7, inch(0.1052)),
    classes=("A", "AA"),
)

KCMIL_105_6_7 = B399(
    code_words=(),
    designation=Kcmil(105.6),
    wires=Round(Aluminum6201T81, 7, inch(0.1228)),
    classes=("A", "AA"),
)

AZUSA = B399(
    code_words=("Azusa",),
    designation=Kcmil(123.3),
    wires=Round(Aluminum6201T81, 7, inch(0.1327)),
    classes=("A", "AA"),
)

KCMIL_133_1_7 = B399(
    code_words=(),
    designation=Kcmil(133.1),
    wires=Round(Aluminum6201T81, 7, inch(0.1379)),
    classes=("A", "AA"),
)

ANAHEIM = B399(
    code_words=("Anaheim",),
    designation=Kcmil(155.4),
    wires=Round(Aluminum6201T81, 7, inch(0.149)),
    classes=("A", "AA"),
)

KCMIL_167_8_7 = B399(
    code_words=(),
    designation=Kcmil(167.8),
    wires=Round(Aluminum6201T81, 7, inch(0.1548)),
    classes=("A", "AA"),
)

AMHERST = B399(
    code_words=("Amherst",),
    designation=Kcmil(195.7),
    wires=Round(Aluminum6201T81, 7, inch(0.1672)),
    classes=("A", "AA"),
)

KCMIL_211_6_7 = B399(
    code_words=(),
    designation=Kcmil(211.6),
    wires=Round(Aluminum6201T81, 7, inch(0.1739)),
    classes=("A", "AA"),
)

ALLIANCE = B399(
    code_words=("Alliance",),
    designation=Kcmil(246.9),
    wires=Round(Aluminum6201T81, 7, inch(0.1878)),
    classes=("AA",),
)

KCMIL_250_19 = B399(
    code_words=(),
    designation=Kcmil(250),
    wires=Round(Aluminum6201T81, 19, inch(0.1147)),
    classes=("A",),
)

KCMIL_300_19 = B399(
    code_words=(),
    designation=Kcmil(300),
    wires=Round(Aluminum6201T81, 19, inch(0.1257)),
    classes=("A",),
)

BUTTE = B399(
    code_words=("Butte",),
    designation=Kcmil(312.8),
    wires=Round(Aluminum6201T81, 19, inch(0.1283)),
    classes=("A",),
)

KCMIL_350_19 = B399(
    code_words=(),
    designation=Kcmil(350),
    wires=Round(Aluminum6201T81, 19, inch(0.1357)),
    classes=("A",),
)

CANTON = B399(
    code_words=("Canton",),
    designation=Kcmil(394.5),
    wires=Round(Aluminum6201T81, 19, inch(0.1441)),
    classes=("A", "AA"),
)

KCMIL_400_19 = B399(
    code_words=(),
    designation=Kcmil(400),
    wires=Round(Aluminum6201T81, 19, inch(0.1451)),
    classes=("A", "AA"),
)

KCMIL_450_19 = B399(
    code_words=(),
    designation=Kcmil(450),
    wires=Round(Aluminum6201T81, 19, inch(0.1539)),
    classes=("AA",),
)

CAIRO = B399(
    code_words=("Cairo",),
    designation=Kcmil(465.4),
    wires=Round(Aluminum6201T81, 19, inch(0.1565)),
    classes=("AA",),
)

KCMIL_500_19 = B399(
    code_words=(),
    designation=Kcmil(500),
    wires=Round(Aluminum6201T81, 19, inch(0.1622)),
    classes=("AA",),
)

KCMIL_550_37 = B399(
    code_words=(),
    designation=Kcmil(550),
    wires=Round(Aluminum6201T81, 37, inch(0.1219)),
    classes=("A", "AA"),
)

DARIEN = B399(
    code_words=("Darien",),
    designation=Kcmil(559.5),
    wires=Round(Aluminum6201T81, 19, inch(0.1716)),
    classes=("AA",),
)

KCMIL_600_37 = B399(
    code_words=(),
    designation=Kcmil(600),
    wires=Round(Aluminum6201T81, 37, inch(0.1273)),
    classes=("A", "AA"),
)

KCMIL_650_37 = B399(
    code_words=(),
    designation=Kcmil(650),
    wires=Round(Aluminum6201T81, 37, inch(0.1325)),
    classes=("AA",),
)

ELGIN = B399(
    code_words=("Elgin",),
    designation=Kcmil(652.4),
    wires=Round(Aluminum6201T81, 19, inch(0.1853)),
    classes=("AA",),
)

KCMIL_700_37 = B399(
    code_words=(),
    designation=Kcmil(700),
    wires=Round(Aluminum6201T81, 37, inch(0.1375)),
    classes=("AA",),
)

FLINT = B399(
    code_words=("Flint",),
    designation=Kcmil(740.8),
    wires=Round(Aluminum6201T81, 37, inch(0.1415)),
    classes=("AA",),
)

KCMIL_750_37 = B399(
    code_words=(),
    designation=Kcmil(750),
    wires=Round(Aluminum6201T81, 37, inch(0.1424)),
    classes=("AA",),
)

KCMIL_800_37 = B399(
    code_words=(),
    designation=Kcmil(800),
    wires=Round(Aluminum6201T81, 37, inch(0.147)),
    classes=("AA",),
)

KCMIL_900_37 = B399(
    code_words=(),
    designation=Kcmil(900),
    wires=Round(Aluminum6201T81, 37, inch(0.156)),
    classes=("AA",),
)

GREELEY = B399(
    code_words=("Greeley",),
    designation=Kcmil(927.2),
    wires=Round(Aluminum6201T81, 37, inch(0.1583)),
    classes=("AA",),
)

KCMIL_1000_37 = B399(
    code_words=(),
    designation=Kcmil(1000),
    wires=Round(Aluminum6201T81, 37, inch(0.1644)),
    classes=("AA",),
)

KCMIL_1077_4_61 = B399(
    code_words=(),
    designation=Kcmil(1077.4),
    wires=Round(Aluminum6201T81, 61, inch(0.1329)),
    classes=("AA",),
)

KCMIL_1165_1_61 = B399(
    code_words=(),
    designation=Kcmil(1165.1),
    wires=Round(Aluminum6201T81, 61, inch(0.1382)),
    classes=("AA",),
)

KCMIL_1250_61 = B399(
    code_words=(),
    designation=Kcmil(1250),
    wires=Round(Aluminum6201T81, 61, inch(0.1431)),
    classes=("AA",),
)

KCMIL_1259_6_61 = B399(
    code_words=(),
    designation=Kcmil(1259.6),
    wires=Round(Aluminum6201T81, 61, inch(0.1437)),
    classes=("AA",),
)

KCMIL_1348_8_61 = B399(
    code_words=(),
    designation=Kcmil(1348.8),
    wires=Round(Aluminum6201T81, 61, inch(0.1487)),
    classes=("AA",),
)

KCMIL_1439_2_61 = B399(
    code_words=(),
    designation=Kcmil(1439.2),
    wires=Round(Aluminum6201T81, 61, inch(0.1536)),
    classes=("AA",),
)

KCMIL_1500_61 = B399(
    code_words=(),
    designation=Kcmil(1500),
    wires=Round(Aluminum6201T81, 61, inch(0.1568)),
    classes=("AA",),
)

KCMIL_1750_61 = B399(
    code_words=(),
    designation=Kcmil(1750),
    wires=Round(Aluminum6201T81, 61, inch(0.1694)),
    classes=("AA",),
)
