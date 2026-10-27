"""IEC 61089, A1/Syz: Aluminium A1 around a core of zinc-coated steel."""

from openline.types.conductors.designations import Code
from openline.types.conductors.iec import A1_Syz
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumA1, ZincCoatedSteel
from openline.types.units import mm

CODE_16_6_1 = A1_Syz(
    code_words=(),
    designation=Code(16),
    outer=Round(AluminumA1, 6, mm(1.84)),
    core=Round(ZincCoatedSteel, 1, mm(1.84)),
)

CODE_25_6_1 = A1_Syz(
    code_words=(),
    designation=Code(25),
    outer=Round(AluminumA1, 6, mm(2.3)),
    core=Round(ZincCoatedSteel, 1, mm(2.3)),
)

CODE_40_6_1 = A1_Syz(
    code_words=(),
    designation=Code(40),
    outer=Round(AluminumA1, 6, mm(2.91)),
    core=Round(ZincCoatedSteel, 1, mm(2.91)),
)

CODE_63_6_1 = A1_Syz(
    code_words=(),
    designation=Code(63),
    outer=Round(AluminumA1, 6, mm(3.66)),
    core=Round(ZincCoatedSteel, 1, mm(3.66)),
)

CODE_100_6_1 = A1_Syz(
    code_words=(),
    designation=Code(100),
    outer=Round(AluminumA1, 6, mm(4.61)),
    core=Round(ZincCoatedSteel, 1, mm(4.61)),
)

CODE_125_18_1 = A1_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA1, 18, mm(2.97)),
    core=Round(ZincCoatedSteel, 1, mm(2.97)),
)

CODE_125_26_7 = A1_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA1, 26, mm(2.47)),
    core=Round(ZincCoatedSteel, 7, mm(1.92)),
)

CODE_160_18_1 = A1_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA1, 18, mm(3.36)),
    core=Round(ZincCoatedSteel, 1, mm(3.36)),
)

CODE_160_26_7 = A1_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA1, 26, mm(2.8)),
    core=Round(ZincCoatedSteel, 7, mm(2.18)),
)

CODE_200_18_1 = A1_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA1, 18, mm(3.76)),
    core=Round(ZincCoatedSteel, 1, mm(3.76)),
)

CODE_200_26_7 = A1_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA1, 26, mm(3.13)),
    core=Round(ZincCoatedSteel, 7, mm(2.43)),
)

CODE_250_22_7 = A1_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 22, mm(3.8)),
    core=Round(ZincCoatedSteel, 7, mm(2.11)),
)

CODE_250_26_7 = A1_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA1, 26, mm(3.5)),
    core=Round(ZincCoatedSteel, 7, mm(2.72)),
)

CODE_315_45_7 = A1_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 45, mm(2.99)),
    core=Round(ZincCoatedSteel, 7, mm(1.99)),
)

CODE_315_26_7 = A1_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA1, 26, mm(3.93)),
    core=Round(ZincCoatedSteel, 7, mm(3.05)),
)

CODE_400_45_7 = A1_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 45, mm(3.36)),
    core=Round(ZincCoatedSteel, 7, mm(2.24)),
)

CODE_400_54_7 = A1_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA1, 54, mm(3.07)),
    core=Round(ZincCoatedSteel, 7, mm(3.07)),
)

CODE_450_45_7 = A1_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 45, mm(3.57)),
    core=Round(ZincCoatedSteel, 7, mm(2.38)),
)

CODE_450_54_7 = A1_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA1, 54, mm(3.26)),
    core=Round(ZincCoatedSteel, 7, mm(3.26)),
)

CODE_500_45_7 = A1_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 45, mm(3.76)),
    core=Round(ZincCoatedSteel, 7, mm(2.51)),
)

CODE_500_54_7 = A1_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA1, 54, mm(3.43)),
    core=Round(ZincCoatedSteel, 7, mm(3.43)),
)

CODE_560_45_7 = A1_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 45, mm(3.98)),
    core=Round(ZincCoatedSteel, 7, mm(2.65)),
)

CODE_560_54_19 = A1_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA1, 54, mm(3.63)),
    core=Round(ZincCoatedSteel, 19, mm(2.18)),
)

CODE_630_45_7 = A1_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 45, mm(4.22)),
    core=Round(ZincCoatedSteel, 7, mm(2.81)),
)

CODE_630_54_19 = A1_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA1, 54, mm(3.85)),
    core=Round(ZincCoatedSteel, 19, mm(2.31)),
)

CODE_710_45_7 = A1_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 45, mm(4.48)),
    core=Round(ZincCoatedSteel, 7, mm(2.99)),
)

CODE_710_54_19 = A1_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA1, 54, mm(4.09)),
    core=Round(ZincCoatedSteel, 19, mm(2.45)),
)

CODE_800_72_7 = A1_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 72, mm(3.76)),
    core=Round(ZincCoatedSteel, 7, mm(2.51)),
)

CODE_800_84_7 = A1_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 84, mm(3.48)),
    core=Round(ZincCoatedSteel, 7, mm(3.48)),
)

CODE_800_54_19 = A1_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA1, 54, mm(4.34)),
    core=Round(ZincCoatedSteel, 19, mm(2.61)),
)

CODE_900_72_7 = A1_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 72, mm(3.99)),
    core=Round(ZincCoatedSteel, 7, mm(2.66)),
)

CODE_900_84_7 = A1_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA1, 84, mm(3.69)),
    core=Round(ZincCoatedSteel, 7, mm(3.69)),
)

CODE_1000_72_7 = A1_Syz(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA1, 72, mm(4.21)),
    core=Round(ZincCoatedSteel, 7, mm(2.8)),
)

CODE_1120_72_19 = A1_Syz(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 72, mm(4.45)),
    core=Round(ZincCoatedSteel, 19, mm(1.78)),
)

CODE_1120_84_19 = A1_Syz(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA1, 84, mm(4.12)),
    core=Round(ZincCoatedSteel, 19, mm(2.47)),
)

CODE_1250_72_19 = A1_Syz(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 72, mm(4.7)),
    core=Round(ZincCoatedSteel, 19, mm(1.88)),
)

CODE_1250_84_19 = A1_Syz(
    code_words=(),
    designation=Code(1250),
    outer=Round(AluminumA1, 84, mm(4.35)),
    core=Round(ZincCoatedSteel, 19, mm(2.61)),
)
