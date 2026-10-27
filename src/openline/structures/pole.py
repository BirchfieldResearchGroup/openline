"""One pole, upright on the centerline, its crossarms holding the wires."""

from dataclasses import replace

from openline.types.materials import Wood
from openline.types.structures import Pole, PoleTop
from openline.types.structures.attachments import Hold, Mount, Wire
from openline.types.structures.geometry import Point
from openline.types.units import ft, ft_in, kv

TS_1 = Pole(
    name="TS-1",
    datum=PoleTop(()),
    voltages=(kv(69),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(ft_in(0, 0), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(ft_in(3, 6), ft(0), -ft_in(3, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(-ft_in(4, 6), ft(0), -ft_in(9, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(4, 6), ft(0), -ft_in(9, 6)), Hold.SUSPENSION),
    ),
    material=Wood,
    crossarms=(),
)

TS_1X = Pole(
    name="TS-1X",
    datum=PoleTop(()),
    voltages=(kv(69),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(ft_in(0, 0), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(ft_in(3, 6), ft(0), -ft_in(4, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(-ft_in(4, 6), ft(0), -ft_in(11, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(4, 6), ft(0), -ft_in(11, 6)), Hold.SUSPENSION),
    ),
    material=Wood,
    crossarms=(),
)

# RUS 1728F-810: "TS-1, TS-2" are drawn alike.
TS_2 = replace(TS_1, name="TS-2")

# RUS 1728F-810: "TS-1X, TS-2X" are drawn alike.
TS_2X = replace(TS_1X, name="TS-2X")
