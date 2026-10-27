"""Upright poles joined by crossarms: two make an H-frame."""

from dataclasses import replace

from openline.types.materials import Wood
from openline.types.structures import Frame, PoleTop
from openline.types.structures.attachments import Hold, Mount, Wire
from openline.types.structures.geometry import Point
from openline.types.structures.members import Beam, Rectangle
from openline.types.units import ft, ft_in, inch, kv

TH_1 = Frame(
    name="TH-1",
    datum=PoleTop(()),
    voltages=(kv(69),),
    line_angles=(),
    attachments=(
        Mount(Wire.PHASE, Point(-ft_in(10, 6), ft(0), -ft_in(1, 0)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(0, 0), ft(0), -ft_in(1, 0)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(10, 6), ft(0), -ft_in(1, 0)), Hold.SUSPENSION),
    ),
    material=Wood,
    poles=(
        Point(-ft_in(5, 3), ft(0), ft_in(0, 0)),
        Point(ft_in(5, 3), ft(0), ft_in(0, 0)),
    ),
    crossarms=(
        Beam(
            Point(-ft_in(11, 0), ft(0), -ft_in(1, 0)),
            Point(ft_in(11, 0), ft(0), -ft_in(1, 0)),
            material=Wood,
            section=Rectangle(inch(5.625), inch(7.375)),
            count=1,
        ),
    ),
)

TH_10_SERIES = Frame(
    name="TH-10 Series",
    datum=PoleTop(()),
    voltages=(kv(161),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(-ft_in(7, 9), ft(0), -ft_in(0, 9)), Hold.CLAMP),
        Mount(Wire.SHIELD, Point(ft_in(7, 9), ft(0), -ft_in(0, 9)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(-ft_in(15, 6), ft(0), -ft_in(7, 9)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(0, 0), ft(0), -ft_in(7, 9)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(15, 6), ft(0), -ft_in(7, 9)), Hold.SUSPENSION),
    ),
    material=Wood,
    poles=(),
    crossarms=(),
)

TH_1A = Frame(
    name="TH-1A",
    datum=PoleTop(()),
    voltages=(kv(115),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(-ft_in(6, 3), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.SHIELD, Point(ft_in(6, 3), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(-ft_in(12, 6), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(0, 0), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(12, 6), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
    ),
    material=Wood,
    poles=(
        Point(-ft_in(6, 3), ft(0), ft_in(0, 0)),
        Point(ft_in(6, 3), ft(0), ft_in(0, 0)),
    ),
    crossarms=(
        Beam(
            Point(-ft_in(13, 0), ft(0), -ft_in(6, 6)),
            Point(ft_in(13, 0), ft(0), -ft_in(6, 6)),
            material=Wood,
            section=Rectangle(inch(5.625), inch(7.375)),
            count=1,
        ),
    ),
)

TH_1G = Frame(
    name="TH-1G",
    datum=PoleTop(()),
    voltages=(kv(69),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(-ft_in(5, 3), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.SHIELD, Point(ft_in(5, 3), ft(0), -ft_in(0, 5)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(-ft_in(10, 6), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(0, 0), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(10, 6), ft(0), -ft_in(6, 6)), Hold.SUSPENSION),
    ),
    material=Wood,
    poles=(
        Point(-ft_in(5, 3), ft(0), ft_in(0, 0)),
        Point(ft_in(5, 3), ft(0), ft_in(0, 0)),
    ),
    crossarms=(
        Beam(
            Point(-ft_in(11, 0), ft(0), -ft_in(6, 6)),
            Point(ft_in(11, 0), ft(0), -ft_in(6, 6)),
            material=Wood,
            section=Rectangle(inch(5.625), inch(7.375)),
            count=1,
        ),
    ),
)

TH_230 = Frame(
    name="TH-230",
    datum=PoleTop(()),
    voltages=(kv(230),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(-ft_in(9, 9), ft(0), -ft_in(0, 9)), Hold.CLAMP),
        Mount(Wire.SHIELD, Point(ft_in(9, 9), ft(0), -ft_in(0, 9)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(-ft_in(19, 6), ft(0), -ft_in(9, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(0, 0), ft(0), -ft_in(9, 6)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(ft_in(19, 6), ft(0), -ft_in(9, 6)), Hold.SUSPENSION),
    ),
    material=Wood,
    poles=(
        Point(-ft_in(9, 9), ft(0), ft_in(0, 0)),
        Point(ft_in(9, 9), ft(0), ft_in(0, 0)),
    ),
    crossarms=(
        Beam(
            Point(-ft_in(20, 0), ft(0), -ft_in(9, 6)),
            Point(ft_in(20, 0), ft(0), -ft_in(9, 6)),
            material=Wood,
            section=Rectangle(inch(3.625), inch(9.375)),
            count=2,
        ),
    ),
)

# RUS 1728F-811, note 5: TH-230 "with one additional X-Brace"; X-braces are not entered.
TH_230X = replace(TH_230, name="TH-230X")
