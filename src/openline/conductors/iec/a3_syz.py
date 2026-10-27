"""IEC 61089, A3/Syz: Aluminium alloy A3 around a core of zinc-coated steel."""

from openline.types.conductors.designations import Code
from openline.types.conductors.iec import A3_Syz
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumA3, ZincCoatedSteel
from openline.types.units import mm

CODE_16_6_1 = A3_Syz(
    code_words=(),
    designation=Code(16),
    outer=Round(AluminumA3, 6, mm(1.99)),
    core=Round(ZincCoatedSteel, 1, mm(1.99)),
)

CODE_25_6_1 = A3_Syz(
    code_words=(),
    designation=Code(25),
    outer=Round(AluminumA3, 6, mm(2.48)),
    core=Round(ZincCoatedSteel, 1, mm(2.48)),
)

CODE_40_6_1 = A3_Syz(
    code_words=(),
    designation=Code(40),
    outer=Round(AluminumA3, 6, mm(3.14)),
    core=Round(ZincCoatedSteel, 1, mm(3.14)),
)

CODE_63_6_1 = A3_Syz(
    code_words=(),
    designation=Code(63),
    outer=Round(AluminumA3, 6, mm(3.94)),
    core=Round(ZincCoatedSteel, 1, mm(3.94)),
)

CODE_100_18_1 = A3_Syz(
    code_words=(),
    designation=Code(100),
    outer=Round(AluminumA3, 18, mm(2.87)),
    core=Round(ZincCoatedSteel, 1, mm(2.87)),
)

CODE_125_18_1 = A3_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA3, 18, mm(3.21)),
    core=Round(ZincCoatedSteel, 1, mm(3.21)),
)

CODE_125_26_7 = A3_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA3, 26, mm(2.67)),
    core=Round(ZincCoatedSteel, 7, mm(2.07)),
)

CODE_160_18_1 = A3_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA3, 18, mm(3.63)),
    core=Round(ZincCoatedSteel, 1, mm(3.63)),
)

CODE_160_26_7 = A3_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA3, 26, mm(3.02)),
    core=Round(ZincCoatedSteel, 7, mm(2.35)),
)

CODE_200_18_1 = A3_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA3, 18, mm(4.05)),
    core=Round(ZincCoatedSteel, 1, mm(4.05)),
)

CODE_200_26_7 = A3_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA3, 26, mm(3.37)),
    core=Round(ZincCoatedSteel, 7, mm(2.62)),
)

CODE_250_22_7 = A3_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA3, 22, mm(4.1)),
    core=Round(ZincCoatedSteel, 7, mm(2.28)),
)

CODE_250_26_7 = A3_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA3, 26, mm(3.77)),
    core=Round(ZincCoatedSteel, 7, mm(2.93)),
)

CODE_315_45_7 = A3_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA3, 45, mm(3.22)),
    core=Round(ZincCoatedSteel, 7, mm(2.15)),
)

CODE_315_26_7 = A3_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA3, 26, mm(4.23)),
    core=Round(ZincCoatedSteel, 7, mm(3.29)),
)

CODE_400_45_7 = A3_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA3, 45, mm(3.63)),
    core=Round(ZincCoatedSteel, 7, mm(2.42)),
)

CODE_400_54_7 = A3_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA3, 54, mm(3.31)),
    core=Round(ZincCoatedSteel, 7, mm(3.31)),
)

CODE_450_45_7 = A3_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA3, 45, mm(3.85)),
    core=Round(ZincCoatedSteel, 7, mm(2.56)),
)

CODE_450_54_7 = A3_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA3, 54, mm(3.51)),
    core=Round(ZincCoatedSteel, 7, mm(3.51)),
)

CODE_500_45_7 = A3_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA3, 45, mm(4.05)),
    core=Round(ZincCoatedSteel, 7, mm(2.7)),
)

CODE_500_54_7 = A3_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA3, 54, mm(3.7)),
    core=Round(ZincCoatedSteel, 7, mm(3.7)),
)

CODE_560_45_7 = A3_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA3, 45, mm(4.29)),
    core=Round(ZincCoatedSteel, 7, mm(2.86)),
)

CODE_560_54_19 = A3_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA3, 54, mm(3.92)),
    core=Round(ZincCoatedSteel, 19, mm(2.35)),
)

CODE_630_72_7 = A3_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA3, 72, mm(3.6)),
    core=Round(ZincCoatedSteel, 7, mm(2.4)),
)

CODE_630_54_19 = A3_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA3, 54, mm(4.15)),
    core=Round(ZincCoatedSteel, 19, mm(2.49)),
)

CODE_710_72_7 = A3_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA3, 72, mm(3.82)),
    core=Round(ZincCoatedSteel, 7, mm(2.55)),
)

CODE_710_54_19 = A3_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA3, 54, mm(4.41)),
    core=Round(ZincCoatedSteel, 19, mm(2.65)),
)

CODE_800_72_7 = A3_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA3, 72, mm(4.05)),
    core=Round(ZincCoatedSteel, 7, mm(2.7)),
)

CODE_800_84_7 = A3_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA3, 84, mm(3.75)),
    core=Round(ZincCoatedSteel, 7, mm(3.75)),
)

CODE_900_72_7 = A3_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA3, 72, mm(4.3)),
    core=Round(ZincCoatedSteel, 7, mm(2.87)),
)

CODE_900_84_7 = A3_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA3, 84, mm(3.98)),
    core=Round(ZincCoatedSteel, 7, mm(3.98)),
)

CODE_1000_84_19 = A3_Syz(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA3, 84, mm(4.2)),
    core=Round(ZincCoatedSteel, 19, mm(2.52)),
)

CODE_1120_84_19 = A3_Syz(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA3, 84, mm(4.44)),
    core=Round(ZincCoatedSteel, 19, mm(2.66)),
)
