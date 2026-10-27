"""IEC 61089, A2/Syz: Aluminium alloy A2 around a core of zinc-coated steel."""

from openline.types.conductors.designations import Code
from openline.types.conductors.iec import A2_Syz
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumA2, ZincCoatedSteel
from openline.types.units import mm

CODE_16_6_1 = A2_Syz(
    code_words=(),
    designation=Code(16),
    outer=Round(AluminumA2, 6, mm(1.98)),
    core=Round(ZincCoatedSteel, 1, mm(1.98)),
)

CODE_25_6_1 = A2_Syz(
    code_words=(),
    designation=Code(25),
    outer=Round(AluminumA2, 6, mm(2.47)),
    core=Round(ZincCoatedSteel, 1, mm(2.47)),
)

CODE_40_6_1 = A2_Syz(
    code_words=(),
    designation=Code(40),
    outer=Round(AluminumA2, 6, mm(3.13)),
    core=Round(ZincCoatedSteel, 1, mm(3.13)),
)

CODE_63_6_1 = A2_Syz(
    code_words=(),
    designation=Code(63),
    outer=Round(AluminumA2, 6, mm(3.92)),
    core=Round(ZincCoatedSteel, 1, mm(3.92)),
)

CODE_100_18_1 = A2_Syz(
    code_words=(),
    designation=Code(100),
    outer=Round(AluminumA2, 18, mm(2.85)),
    core=Round(ZincCoatedSteel, 1, mm(2.85)),
)

CODE_125_18_1 = A2_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA2, 18, mm(3.19)),
    core=Round(ZincCoatedSteel, 1, mm(3.19)),
)

CODE_125_26_7 = A2_Syz(
    code_words=(),
    designation=Code(125),
    outer=Round(AluminumA2, 26, mm(2.65)),
    core=Round(ZincCoatedSteel, 7, mm(2.06)),
)

CODE_160_18_1 = A2_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA2, 18, mm(3.61)),
    core=Round(ZincCoatedSteel, 1, mm(3.61)),
)

CODE_160_26_7 = A2_Syz(
    code_words=(),
    designation=Code(160),
    outer=Round(AluminumA2, 26, mm(3)),
    core=Round(ZincCoatedSteel, 7, mm(2.34)),
)

CODE_200_18_1 = A2_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA2, 18, mm(4.04)),
    core=Round(ZincCoatedSteel, 1, mm(4.04)),
)

CODE_200_26_7 = A2_Syz(
    code_words=(),
    designation=Code(200),
    outer=Round(AluminumA2, 26, mm(3.36)),
    core=Round(ZincCoatedSteel, 7, mm(2.61)),
)

CODE_250_22_7 = A2_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA2, 22, mm(4.08)),
    core=Round(ZincCoatedSteel, 7, mm(2.27)),
)

CODE_250_26_7 = A2_Syz(
    code_words=(),
    designation=Code(250),
    outer=Round(AluminumA2, 26, mm(3.75)),
    core=Round(ZincCoatedSteel, 7, mm(2.92)),
)

CODE_315_45_7 = A2_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA2, 45, mm(3.2)),
    core=Round(ZincCoatedSteel, 7, mm(2.14)),
)

CODE_315_26_7 = A2_Syz(
    code_words=(),
    designation=Code(315),
    outer=Round(AluminumA2, 26, mm(4.21)),
    core=Round(ZincCoatedSteel, 7, mm(3.28)),
)

CODE_400_45_7 = A2_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA2, 45, mm(3.61)),
    core=Round(ZincCoatedSteel, 7, mm(2.41)),
)

CODE_400_54_7 = A2_Syz(
    code_words=(),
    designation=Code(400),
    outer=Round(AluminumA2, 54, mm(3.29)),
    core=Round(ZincCoatedSteel, 7, mm(3.29)),
)

CODE_450_45_7 = A2_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA2, 45, mm(3.83)),
    core=Round(ZincCoatedSteel, 7, mm(2.55)),
)

CODE_450_54_7 = A2_Syz(
    code_words=(),
    designation=Code(450),
    outer=Round(AluminumA2, 54, mm(3.49)),
    core=Round(ZincCoatedSteel, 7, mm(3.49)),
)

CODE_500_45_7 = A2_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA2, 45, mm(4.04)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

CODE_500_54_7 = A2_Syz(
    code_words=(),
    designation=Code(500),
    outer=Round(AluminumA2, 54, mm(3.68)),
    core=Round(ZincCoatedSteel, 7, mm(3.68)),
)

CODE_560_45_7 = A2_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA2, 45, mm(4.27)),
    core=Round(ZincCoatedSteel, 7, mm(2.85)),
)

CODE_560_54_19 = A2_Syz(
    code_words=(),
    designation=Code(560),
    outer=Round(AluminumA2, 54, mm(3.9)),
    core=Round(ZincCoatedSteel, 19, mm(2.34)),
)

CODE_630_72_7 = A2_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA2, 72, mm(3.58)),
    core=Round(ZincCoatedSteel, 7, mm(2.39)),
)

CODE_630_54_19 = A2_Syz(
    code_words=(),
    designation=Code(630),
    outer=Round(AluminumA2, 54, mm(4.13)),
    core=Round(ZincCoatedSteel, 19, mm(2.48)),
)

CODE_710_72_7 = A2_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA2, 72, mm(3.8)),
    core=Round(ZincCoatedSteel, 7, mm(2.53)),
)

CODE_710_54_19 = A2_Syz(
    code_words=(),
    designation=Code(710),
    outer=Round(AluminumA2, 54, mm(4.39)),
    core=Round(ZincCoatedSteel, 19, mm(2.63)),
)

CODE_800_72_7 = A2_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA2, 72, mm(4.04)),
    core=Round(ZincCoatedSteel, 7, mm(2.69)),
)

CODE_800_84_7 = A2_Syz(
    code_words=(),
    designation=Code(800),
    outer=Round(AluminumA2, 84, mm(3.74)),
    core=Round(ZincCoatedSteel, 7, mm(3.74)),
)

CODE_900_72_7 = A2_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA2, 72, mm(4.28)),
    core=Round(ZincCoatedSteel, 7, mm(2.85)),
)

CODE_900_84_7 = A2_Syz(
    code_words=(),
    designation=Code(900),
    outer=Round(AluminumA2, 84, mm(3.96)),
    core=Round(ZincCoatedSteel, 7, mm(3.96)),
)

CODE_1000_84_19 = A2_Syz(
    code_words=(),
    designation=Code(1000),
    outer=Round(AluminumA2, 84, mm(4.18)),
    core=Round(ZincCoatedSteel, 19, mm(2.51)),
)

CODE_1120_84_19 = A2_Syz(
    code_words=(),
    designation=Code(1120),
    outer=Round(AluminumA2, 84, mm(4.42)),
    core=Round(ZincCoatedSteel, 19, mm(2.65)),
)
