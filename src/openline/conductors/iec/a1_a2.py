"""IEC 61089, A1/A2: Aluminium A1 around a core of aluminium alloy A2."""

from openline.types.conductors.designations import Code
from openline.types.conductors.iec import A1_A2
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumA1, AluminumA2
from openline.types.units import mm

CODE_16_4_3 = A1_A2(
    code_words=(),
    designation=Code(16),
    outer=Round(AluminumA1, 4, mm(1.76)),
    core=Round(AluminumA2, 3, mm(1.76)),
)

CODE_25_4_3 = A1_A2(
    code_words=(),
    designation=Code(25),
    outer=Round(AluminumA1, 4, mm(2.2)),
    core=Round(AluminumA2, 3, mm(2.2)),
)

CODE_40_4_3 = A1_A2(
    code_words=(),
    designation=Code(40),
    outer=Round(AluminumA1, 4, mm(2.78)),
    core=Round(AluminumA2, 3, mm(2.78)),
)

CODE_63_4_3 = A1_A2(
    code_words=(),
    designation=Code(63),
    outer=Round(AluminumA1, 4, mm(3.49)),
    core=Round(AluminumA2, 3, mm(3.49)),
)

CODE_100_4_3 = A1_A2(
    code_words=(),
    designation=Code(100),
    outer=Round(AluminumA1, 4, mm(4.4)),
    core=Round(AluminumA2, 3, mm(4.4)),
)

CODE_125_12_7 = A1_A2(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA1, 12, mm(2.97)),
    core=Round(AluminumA2, 7, mm(2.97)),
)

CODE_160_12_7 = A1_A2(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA1, 12, mm(3.36)),
    core=Round(AluminumA2, 7, mm(3.36)),
)

CODE_200_12_7 = A1_A2(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA1, 12, mm(3.76)),
    core=Round(AluminumA2, 7, mm(3.76)),
)

CODE_250_12_7 = A1_A2(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 12, mm(4.21)),
    core=Round(AluminumA2, 7, mm(4.21)),
)

CODE_250_18_19 = A1_A2(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 18, mm(3.04)),
    core=Round(AluminumA2, 19, mm(3.04)),
)

CODE_315_30_7 = A1_A2(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 30, mm(3.34)),
    core=Round(AluminumA2, 7, mm(3.34)),
)

CODE_315_18_19 = A1_A2(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 18, mm(3.42)),
    core=Round(AluminumA2, 19, mm(3.42)),
)

CODE_400_30_7 = A1_A2(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 30, mm(3.76)),
    core=Round(AluminumA2, 7, mm(3.76)),
)

CODE_400_18_19 = A1_A2(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 18, mm(3.85)),
    core=Round(AluminumA2, 19, mm(3.85)),
)

CODE_450_30_7 = A1_A2(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 30, mm(3.99)),
    core=Round(AluminumA2, 7, mm(3.99)),
)

CODE_450_18_19 = A1_A2(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 18, mm(4.08)),
    core=Round(AluminumA2, 19, mm(4.08)),
)

CODE_500_30_7 = A1_A2(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 30, mm(4.21)),
    core=Round(AluminumA2, 7, mm(4.21)),
)

CODE_500_18_19 = A1_A2(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 18, mm(4.31)),
    core=Round(AluminumA2, 19, mm(4.31)),
)

CODE_560_54_7 = A1_A2(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 54, mm(3.45)),
    core=Round(AluminumA2, 7, mm(3.45)),
)

CODE_560_30_7 = A1_A2(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 30, mm(4.45)),
    core=Round(AluminumA2, 7, mm(4.45)),
)

CODE_630_42_19 = A1_A2(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 42, mm(3.71)),
    core=Round(AluminumA2, 19, mm(3.71)),
)

CODE_630_24_37 = A1_A2(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 24, mm(3.79)),
    core=Round(AluminumA2, 37, mm(3.79)),
)

CODE_710_42_19 = A1_A2(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 42, mm(3.94)),
    core=Round(AluminumA2, 19, mm(3.94)),
)

CODE_710_24_37 = A1_A2(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 24, mm(4.02)),
    core=Round(AluminumA2, 37, mm(4.02)),
)

CODE_800_42_19 = A1_A2(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 42, mm(4.18)),
    core=Round(AluminumA2, 19, mm(4.18)),
)

CODE_800_24_37 = A1_A2(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 24, mm(4.27)),
    core=Round(AluminumA2, 37, mm(4.27)),
)

CODE_900_42_19 = A1_A2(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 42, mm(4.43)),
    core=Round(AluminumA2, 19, mm(4.43)),
)

CODE_900_54_37 = A1_A2(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 54, mm(3.66)),
    core=Round(AluminumA2, 37, mm(3.66)),
)

CODE_1000_72_19 = A1_A2(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA1, 72, mm(3.8)),
    core=Round(AluminumA2, 19, mm(3.8)),
)

CODE_1000_54_37 = A1_A2(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA1, 54, mm(3.85)),
    core=Round(AluminumA2, 37, mm(3.85)),
)

CODE_1120_72_19 = A1_A2(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 72, mm(4.02)),
    core=Round(AluminumA2, 19, mm(4.02)),
)

CODE_1120_54_37 = A1_A2(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 54, mm(4.08)),
    core=Round(AluminumA2, 37, mm(4.08)),
)

CODE_1250_72_19 = A1_A2(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 72, mm(4.25)),
    core=Round(AluminumA2, 19, mm(4.25)),
)

CODE_1250_54_37 = A1_A2(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 54, mm(4.31)),
    core=Round(AluminumA2, 37, mm(4.31)),
)

CODE_1400_72_19 = A1_A2(
    code_words=(),
    designation=Code(1400),
    outer=Round(AluminumA1, 72, mm(4.5)),
    core=Round(AluminumA2, 19, mm(4.5)),
)
