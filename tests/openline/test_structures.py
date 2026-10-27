"""openline.types.structures and the structures openline.structures lists: records that refuse
what no structure is; how every listed structure holds its wires and stands at its heights; and
each source's structures as its drawings give them: TenneT's masts, RUS's wood frames, and
LCRA's 765 kV tower."""

import math
from dataclasses import replace
from typing import Any

import pytest

from openline import structures
from openline.structures.frame import TH_230
from openline.structures.tower import (
    A_2_D_2004_4_WE_WADIFF_100,
    A_2_E_01_2019_42_WE_WADIFF_140,
    D_2_D_2018_3_T1,
    D_2_D_2018_3_WA160,
    D_2_T_2019_1_T1,
    DA_4_DE_2018_1_T1,
)
from openline.structures.tower import TYPICAL_765KV_TANGENT_TOWER as LCRA
from openline.types.materials import Steel, Wood
from openline.types.structures import (
    Frame,
    LineAngle,
    LowestCrossarm,
    Pole,
    PoleTop,
    Structure,
    Tower,
)
from openline.types.structures.attachments import (
    DiscString,
    Hold,
    InsulatorString,
    Wire,
    WirePosition,
)
from openline.types.structures.geometry import Face, Point
from openline.types.structures.members import Bar, Beam, Rectangle, Role, Truss
from openline.types.structures.panels import Bracing, Edge, Panel, PanelRun
from openline.types.units import degrees, ft, ft_in, inch, m, mm

ORIGIN = Point(m(0), m(0), m(0))
UP = Point(m(0), m(0), m(1))
WIRE = Point(m(0), m(0), m(-2))


def joints(tower: Tower[Any]) -> set[Point]:
    """Where a tower's bars meet, over all its parts."""
    trusses = (part.construction for part in tower.parts if isinstance(part.construction, Truss))
    return {joint for truss in trusses for joint in truss.joints}


TRUSSED = [tower for tower in structures.of(Tower) if joints(tower)]  # drawn as bars


def test_a_point_is_finite() -> None:
    with pytest.raises(ValueError, match="finite"):
        Point(m(math.nan), m(0), m(0))


def test_a_member_s_ends_are_apart() -> None:
    with pytest.raises(ValueError, match="two ends apart"):
        Bar(ORIGIN, ORIGIN, role=Role.CHORD)


def test_a_section_s_sides_are_positive() -> None:
    with pytest.raises(ValueError, match="positive"):
        Rectangle(inch(3.625), inch(0))


def test_a_crossarm_has_a_beam() -> None:
    with pytest.raises(ValueError, match="needs a beam"):
        Beam(ORIGIN, UP, material=Wood, section=Rectangle(inch(3.625), inch(9.375)), count=0)


def test_a_truss_has_bars() -> None:
    with pytest.raises(ValueError, match="needs bars"):
        Truss(material=Steel, bars=())


def test_a_panel_has_a_bay() -> None:
    with pytest.raises(ValueError, match="a bay"):
        Panel(Edge(ORIGIN, UP), Bracing.CROSS, 0)


def test_an_outline_has_panels() -> None:
    with pytest.raises(ValueError, match="needs panels"):
        PanelRun(face=Face.TRANSVERSE, start=Edge(ORIGIN, UP), panels=())


@pytest.mark.parametrize(("low", "high"), [(30, 10), (-10, 10), (10, 190)])
def test_line_angles_run_from_the_smaller_within_a_half_turn(low: float, high: float) -> None:
    with pytest.raises(ValueError, match="ordered"):
        LineAngle(degrees(low), degrees(high))


@pytest.mark.parametrize(
    ("discs", "diameter", "length"), [(0, 254, 2000), (12, 0, 2000), (12, 254, 0)]
)
def test_a_disc_string_has_discs_of_a_size_over_a_length(
    discs: int, diameter: float, length: float
) -> None:
    with pytest.raises(ValueError, match="needs discs"):
        DiscString(mount=UP, discs=discs, diameter=mm(diameter), length=mm(length))


@pytest.mark.parametrize(
    ("hold", "given", "needed"),
    [(Hold.V_STRING, 1, "two strings"), (Hold.SUSPENSION, 2, "one string")],
)
def test_a_wire_position_has_the_strings_its_hold_takes(
    hold: Hold, given: int, needed: str
) -> None:
    strings = tuple(InsulatorString(mount=Point(m(i), m(0), m(1))) for i in range(given))
    with pytest.raises(ValueError, match=f"needs {needed}"):
        WirePosition(Wire.PHASE, WIRE, hold, strings=strings)


def test_a_wire_position_s_strings_hang_from_mounts_apart() -> None:
    with pytest.raises(ValueError, match="mounts apart"):
        WirePosition(Wire.PHASE, WIRE, Hold.V_STRING, strings=(InsulatorString(mount=UP),) * 2)


def test_a_wire_clamped_at_a_point_is_held_at_a_mount() -> None:
    with pytest.raises(ValueError, match="held at a mount"):
        WirePosition(Wire.SHIELD, WIRE, Hold.CLAMP, strings=())


def test_a_string_s_discs_fit_between_its_mount_and_its_wire() -> None:  # 3 m apart
    discs = DiscString(mount=UP, discs=24, diameter=mm(254), length=mm(3500))
    with pytest.raises(ValueError, match="must fit"):
        WirePosition(Wire.PHASE, WIRE, Hold.SUSPENSION, strings=(discs,))


def test_a_structure_lists_its_attachments_from_the_top_down_then_left_to_right() -> None:
    with pytest.raises(ValueError, match="from the top down"):
        replace(LCRA, attachments=LCRA.attachments[::-1])


def test_every_listed_structure_clamps_its_shields_and_insulates_its_phases() -> None:
    astray = [
        (structure.name, str(a))
        for structure in structures.of(Structure)
        for a in structure.attachments
        if (a.hold is Hold.CLAMP) != (a.wire is Wire.SHIELD)
    ]
    assert astray == []


@pytest.mark.parametrize("tower", TRUSSED, ids=[tower.name for tower in TRUSSED])
def test_a_trussed_tower_is_steel_bars_all_joined(tower: Tower[Any]) -> None:
    graph: dict[Point, set[Point]] = {}
    for part in tower.parts:
        assert isinstance(part.construction, Truss)
        assert part.construction.material is Steel
        for bar in part.construction.bars:
            graph.setdefault(bar.start, set()).add(bar.end)
            graph.setdefault(bar.end, set()).add(bar.start)
    first = next(iter(graph))
    seen, pending = {first}, [first]
    while pending:
        for other in graph[pending.pop()] - seen:
            seen.add(other)
            pending.append(other)
    assert seen == joints(tower)


def test_a_structure_built_higher_raises_its_wires_and_strings_alike() -> None:
    for before, after in zip(LCRA.attachments, LCRA.at(m(50)), strict=True):
        assert after.point == before.point.raised(m(50))
        if isinstance(before, WirePosition) and isinstance(after, WirePosition):
            assert after.strings == tuple(string.raised(m(50)) for string in before.strings)


def test_rus_frames_and_poles_are_wood_hung_below_their_pole_tops() -> None:
    poled: list[Frame[Any, Any] | Pole[Any, Any]] = [*structures.of(Frame), *structures.of(Pole)]
    astray = [
        structure.name
        for structure in poled
        if structure.material is not Wood
        or structure.datum != PoleTop(())
        or any(a.point.height > ft(0) for a in structure.attachments)
    ]
    assert astray == []


@pytest.mark.parametrize(
    ("tower", "reaches", "height"),
    [
        (D_2_D_2018_3_T1, (-9.95, 9.95, -12.7, -7.2, 7.2, 12.7), 43.5),
        (D_2_T_2019_1_T1, (-7, 7, -9.5, 9.5, -7.5, 7.5), 58.5),
        (
            DA_4_DE_2018_1_T1,
            (-9.95, 9.95, -12.7, -7.2, 7.2, 12.7, -14.3, -10, -5.7, 5.7, 10, 14.3),
            55.5,
        ),
        (A_2_D_2004_4_WE_WADIFF_100, (-7.15, 7.15, -10.1, -4.2, 4.2, 10.1), 31.5),
        (A_2_E_01_2019_42_WE_WADIFF_140, (-14.2, -9.3, -4.4, 4.4, 9.3, 14.2), 28.55),
    ],
    ids=lambda value: getattr(value, "name", None),
)
def test_tennet_masts_reach_and_rise_as_drawn(
    tower: Tower[Any], reaches: tuple[float, ...], height: float
) -> None:
    assert tuple(p.point.across.si for p in tower.phases) == reaches
    bottom = min(joint.height.si for joint in joints(tower))
    top = max(joint.height.si for joint in joints(tower))
    assert bottom == -min(value.si for value in tower.datum.heights)
    assert top - bottom == pytest.approx(height)


def test_a_tennet_mast_stands_26_to_50_m_to_its_lowest_crossarm() -> None:
    datum = D_2_D_2018_3_T1.datum
    assert isinstance(datum, LowestCrossarm)
    assert (datum.heights[0], datum.heights[-1]) == (m(26), m(50))


def test_a_tennet_angle_mast_takes_its_wires_pull_and_a_tangent_mast_not() -> None:
    assert (D_2_D_2018_3_WA160.tension, D_2_D_2018_3_T1.tension) == (True, False)


def test_a_tennet_mast_hangs_its_phases_at_their_drawn_heights() -> None:
    heights = [p.point.height.si for p in D_2_D_2018_3_T1.phases]
    assert heights == [6.55, 6.55, -3.91, -3.91, -3.91, -3.91]


def test_a_tennet_mast_hangs_v_strings_from_its_joints_above_its_wires() -> None:
    at = joints(D_2_D_2018_3_T1)
    hung = [
        (phase.hold, type(string), string.mount in at, string.mount.height > phase.point.height)
        for phase in D_2_D_2018_3_T1.phases
        if isinstance(phase, WirePosition)
        for string in phase.strings
    ]  # the drawings give no discs
    assert hung == [(Hold.V_STRING, InsulatorString, True, True)] * 12


def test_a_tennet_mast_hangs_its_lowest_phases_on_one_string_each() -> None:
    lowest = DA_4_DE_2018_1_T1.phases[-6:]
    hung = [
        (phase.hold, len(phase.strings), phase.strings[0].mount.height, phase.point.height)
        for phase in lowest
        if isinstance(phase, WirePosition)
    ]
    assert hung == [(Hold.SUSPENSION, 1, m(0), m(-2.15))] * 6


def test_rus_th_230_stands_on_two_poles_19_ft_6_in_apart() -> None:
    assert TH_230.poles == (Point(-ft_in(9, 9), ft(0), ft(0)), Point(ft_in(9, 9), ft(0), ft(0)))


def test_rus_th_230_holds_its_phases_on_a_double_wood_crossarm_40_ft_long() -> None:
    (arm,) = TH_230.crossarms
    assert (arm.material, arm.count, arm.end.across - arm.start.across) == (Wood, 2, ft(40))
    assert (arm.section.width, arm.section.depth) == (inch(3.625), inch(9.375))


def test_lcra_crossarms_end_70_ft_10_in_out() -> None:
    tips = {
        arm.construction.panels[-1].edge.start.across
        for arm in LCRA.crossarms
        if isinstance(arm.construction, PanelRun)
    }
    assert tips == {-ft_in(70, 10), ft_in(70, 10)}


def test_lcra_peaks_end_at_its_shield_wires() -> None:
    peaks = {
        peak.construction.panels[-1].edge.start
        for peak in LCRA.peaks
        if isinstance(peak.construction, PanelRun)
    }
    assert peaks == {a.point for a in LCRA.shields}


def test_lcra_hangs_its_phases_19_ft_6_in_below_its_datum() -> None:
    assert {a.point.height for a in LCRA.phases} == {-ft_in(19, 6)}


def test_lcra_hangs_each_phase_on_two_disc_strings() -> None:
    strings = [
        tuple(type(string) for string in phase.strings)
        for phase in LCRA.phases
        if isinstance(phase, WirePosition)
    ]
    assert strings == [(DiscString, DiscString)] * len(LCRA.phases)
