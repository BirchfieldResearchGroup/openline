"""BS EN 50182, AL3: Aluminum alloy AL3, designated by code number."""

from openline.types.conductors.bs import BS_EN50182_AL3
from openline.types.conductors.designations import Code
from openline.types.conductors.strands import Round
from openline.types.materials import AluminumAL3
from openline.types.units import mm

BOX = BS_EN50182_AL3(
    code_words=("Box",), designation=Code(19), wires=Round(AluminumAL3, 7, mm(1.85))
)

ACACIA = BS_EN50182_AL3(
    code_words=("Acacia",), designation=Code(24), wires=Round(AluminumAL3, 7, mm(2.08))
)

ALMOND = BS_EN50182_AL3(
    code_words=("Almond",), designation=Code(30), wires=Round(AluminumAL3, 7, mm(2.34))
)

CEDAR = BS_EN50182_AL3(
    code_words=("Cedar",), designation=Code(35), wires=Round(AluminumAL3, 7, mm(2.54))
)

DEODAR = BS_EN50182_AL3(
    code_words=("Deodar",), designation=Code(42), wires=Round(AluminumAL3, 7, mm(2.77))
)

FIR = BS_EN50182_AL3(
    code_words=("Fir",), designation=Code(48), wires=Round(AluminumAL3, 7, mm(2.95))
)

HAZEL = BS_EN50182_AL3(
    code_words=("Hazel",), designation=Code(60), wires=Round(AluminumAL3, 7, mm(3.3))
)

PINE = BS_EN50182_AL3(
    code_words=("Pine",), designation=Code(72), wires=Round(AluminumAL3, 7, mm(3.61))
)

HOLLY = BS_EN50182_AL3(
    code_words=("Holly",), designation=Code(84), wires=Round(AluminumAL3, 7, mm(3.91))
)

WILLOW = BS_EN50182_AL3(
    code_words=("Willow",), designation=Code(90), wires=Round(AluminumAL3, 7, mm(4.04))
)

OAK = BS_EN50182_AL3(
    code_words=("Oak",), designation=Code(119), wires=Round(AluminumAL3, 7, mm(4.65))
)

MULBERRY = BS_EN50182_AL3(
    code_words=("Mulberry",), designation=Code(151), wires=Round(AluminumAL3, 19, mm(3.18))
)

ASH = BS_EN50182_AL3(
    code_words=("Ash",), designation=Code(181), wires=Round(AluminumAL3, 19, mm(3.48))
)

ELM = BS_EN50182_AL3(
    code_words=("Elm",), designation=Code(211), wires=Round(AluminumAL3, 19, mm(3.76))
)

POPLAR = BS_EN50182_AL3(
    code_words=("Poplar",), designation=Code(239), wires=Round(AluminumAL3, 37, mm(2.87))
)

SYCAMORE = BS_EN50182_AL3(
    code_words=("Sycamore",), designation=Code(303), wires=Round(AluminumAL3, 37, mm(3.23))
)

UPAS = BS_EN50182_AL3(
    code_words=("Upas",), designation=Code(362), wires=Round(AluminumAL3, 37, mm(3.53))
)

YEW = BS_EN50182_AL3(
    code_words=("Yew",), designation=Code(479), wires=Round(AluminumAL3, 37, mm(4.06))
)

TOTARA = BS_EN50182_AL3(
    code_words=("Totara",), designation=Code(498), wires=Round(AluminumAL3, 37, mm(4.14))
)

RUBUS = BS_EN50182_AL3(
    code_words=("Rubus",), designation=Code(587), wires=Round(AluminumAL3, 61, mm(3.5))
)

SORBUS = BS_EN50182_AL3(
    code_words=("Sorbus",), designation=Code(659), wires=Round(AluminumAL3, 61, mm(3.71))
)

ARAUCARIA = BS_EN50182_AL3(
    code_words=("Araucaria",), designation=Code(821), wires=Round(AluminumAL3, 61, mm(4.14))
)

REDWOOD = BS_EN50182_AL3(
    code_words=("Redwood",), designation=Code(996), wires=Round(AluminumAL3, 61, mm(4.56))
)
