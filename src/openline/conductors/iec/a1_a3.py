"""IEC 61089, A1/A3: Aluminium A1 around a core of aluminium alloy A3."""

from openline.types.conductors.designations import Code
from openline.types.conductors.iec import A1_A3
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumA1, AluminumA3
from openline.types.units import mm

CODE_16_4_3 = A1_A3(
    code_words=(),
    designation=Code(16),
    outer=Round(AluminumA1, 4, mm(1.76)),
    core=Round(AluminumA3, 3, mm(1.76)),
)

CODE_25_4_3 = A1_A3(
    code_words=(),
    designation=Code(25),
    outer=Round(AluminumA1, 4, mm(2.21)),
    core=Round(AluminumA3, 3, mm(2.21)),
)

CODE_40_4_3 = A1_A3(
    code_words=(),
    designation=Code(40),
    outer=Round(AluminumA1, 4, mm(2.79)),
    core=Round(AluminumA3, 3, mm(2.79)),
)

CODE_63_4_3 = A1_A3(
    code_words=(),
    designation=Code(63),
    outer=Round(AluminumA1, 4, mm(3.5)),
    core=Round(AluminumA3, 3, mm(3.5)),
)

CODE_100_4_3 = A1_A3(
    code_words=(),
    designation=Code(100),
    outer=Round(AluminumA1, 4, mm(4.41)),
    core=Round(AluminumA3, 3, mm(4.41)),
)

CODE_125_12_7 = A1_A3(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA1, 12, mm(2.98)),
    core=Round(AluminumA3, 7, mm(2.98)),
)

CODE_160_12_7 = A1_A3(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA1, 12, mm(3.37)),
    core=Round(AluminumA3, 7, mm(3.37)),
)

CODE_200_12_7 = A1_A3(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA1, 12, mm(3.77)),
    core=Round(AluminumA3, 7, mm(3.77)),
)

CODE_250_12_7 = A1_A3(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 12, mm(4.21)),
    core=Round(AluminumA3, 7, mm(4.21)),
)

CODE_250_18_19 = A1_A3(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 18, mm(3.05)),
    core=Round(AluminumA3, 19, mm(3.05)),
)

CODE_315_30_7 = A1_A3(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 30, mm(3.34)),
    core=Round(AluminumA3, 7, mm(3.34)),
)

CODE_315_18_19 = A1_A3(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 18, mm(3.43)),
    core=Round(AluminumA3, 19, mm(3.43)),
)

CODE_400_30_7 = A1_A3(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 30, mm(3.77)),
    core=Round(AluminumA3, 7, mm(3.77)),
)

CODE_400_18_19 = A1_A3(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 18, mm(3.86)),
    core=Round(AluminumA3, 19, mm(3.86)),
)

CODE_450_30_7 = A1_A3(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 30, mm(3.99)),
    core=Round(AluminumA3, 7, mm(3.99)),
)

CODE_450_18_19 = A1_A3(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 18, mm(4.1)),
    core=Round(AluminumA3, 19, mm(4.1)),
)

CODE_500_30_7 = A1_A3(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 30, mm(4.21)),
    core=Round(AluminumA3, 7, mm(4.21)),
)

CODE_500_18_19 = A1_A3(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 18, mm(4.32)),
    core=Round(AluminumA3, 19, mm(4.32)),
)

CODE_560_54_7 = A1_A3(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 54, mm(3.45)),
    core=Round(AluminumA3, 7, mm(3.45)),
)

CODE_560_30_7 = A1_A3(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 30, mm(4.46)),
    core=Round(AluminumA3, 7, mm(4.46)),
)

CODE_630_42_19 = A1_A3(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 42, mm(3.72)),
    core=Round(AluminumA3, 19, mm(3.72)),
)

CODE_630_24_37 = A1_A3(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 24, mm(3.8)),
    core=Round(AluminumA3, 37, mm(3.8)),
)

CODE_710_42_19 = A1_A3(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 42, mm(3.95)),
    core=Round(AluminumA3, 19, mm(3.95)),
)

CODE_710_24_37 = A1_A3(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 24, mm(4.03)),
    core=Round(AluminumA3, 37, mm(4.03)),
)

CODE_800_42_19 = A1_A3(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 42, mm(4.19)),
    core=Round(AluminumA3, 19, mm(4.19)),
)

CODE_800_24_37 = A1_A3(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 24, mm(4.28)),
    core=Round(AluminumA3, 37, mm(4.28)),
)

CODE_900_42_19 = A1_A3(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 42, mm(4.44)),
    core=Round(AluminumA3, 19, mm(4.44)),
)

CODE_900_54_37 = A1_A3(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 54, mm(3.66)),
    core=Round(AluminumA3, 37, mm(3.66)),
)

CODE_1000_72_19 = A1_A3(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA1, 72, mm(3.8)),
    core=Round(AluminumA3, 19, mm(3.8)),
)

CODE_1000_54_37 = A1_A3(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA1, 54, mm(3.86)),
    core=Round(AluminumA3, 37, mm(3.86)),
)

CODE_1120_72_19 = A1_A3(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 72, mm(4.02)),
    core=Round(AluminumA3, 19, mm(4.02)),
)

CODE_1120_54_37 = A1_A3(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 54, mm(4.09)),
    core=Round(AluminumA3, 37, mm(4.09)),
)

CODE_1250_72_19 = A1_A3(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 72, mm(4.25)),
    core=Round(AluminumA3, 19, mm(4.25)),
)

CODE_1250_54_37 = A1_A3(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 54, mm(4.32)),
    core=Round(AluminumA3, 37, mm(4.32)),
)

CODE_1400_72_19 = A1_A3(
    code_words=(),
    designation=Code(1400),
    outer=Round(AluminumA1, 72, mm(4.5)),
    core=Round(AluminumA3, 19, mm(4.5)),
)
