"""Structure figures and tables: every catalog tower's elevations keep its mounts; bars in both
planes, insulator strings at any slant, a frame from its pole tops down, the ground line; and a
specification's tables."""

import math
import xml.etree.ElementTree as ET
from dataclasses import astuple, replace
from typing import Any

import pytest

from openline import structures
from openline.structures.frame import TH_230
from openline.structures.tower import AS4_AD90, MT_008_004
from openline.structures.tower import TYPICAL_765KV_TANGENT_TOWER as LCRA
from openline.types.materials import Steel
from openline.types.structures import Structure, Tower
from openline.types.structures.attachments import (
    DiscString,
    Hold,
    InsulatorString,
    Mount,
    Wire,
    WirePosition,
)
from openline.types.structures.geometry import Face, Point
from openline.types.structures.members import Bar, Role, Truss
from openline.types.structures.panels import Body, PanelRun
from openline.types.units import ft_in, m
from openline_sphinx.figures import elevation
from openline_sphinx.presentation import structures as pages

DRAWN = [tower for tower in structures.of(Tower) if tower.body]  # towers drawn by their parts


def barred() -> Tower[Any]:
    """LCRA's tower, its parts one steel chord, and no wires."""
    chord = Bar(Point(m(0), m(0), m(0)), Point(m(2), m(1), m(10)), role=Role.CHORD)
    return replace(
        LCRA,
        attachments=(),
        body=(Body(construction=Truss(material=Steel, bars=(chord,))),),
        legs=(),
        head=(),
        crossarms=(),
        peaks=(),
        bases=(),
    )


def test_bars_are_drawn_in_both_planes() -> None:
    drawing = elevation.plan(barred())
    assert [view.name for view in drawing.views] == ["Front", "Side"]
    assert drawing.views[0].path == "M0,0L2,-10"
    assert drawing.views[1].path == "M0,0L1,-10"
    for interactive in (False, True):
        ET.fromstring(elevation.draw(drawing, interactive=interactive, occurrence=""))


@pytest.mark.parametrize("height", [0, 1])
@pytest.mark.parametrize("discs", [False, True])
def test_strings_at_a_slant_are_drawn_over_their_length(height: int, discs: bool) -> None:
    mount = Point(m(0), m(10), m(height))
    string = (
        DiscString(mount=mount, discs=20, diameter=m(0.25), length=m(8))
        if discs
        else InsulatorString(mount=mount)
    )
    held = WirePosition(Wire.PHASE, Point(m(0), m(0), m(0)), Hold.STRAIN, strings=(string,))
    structure = replace(barred(), attachments=(held,))
    for face in Face:
        lines = elevation.strings(structure, face)
        assert lines
        assert all(math.isfinite(v) for line in lines for p in line for v in p)
    front = [p for line in elevation.strings(structure, Face.TRANSVERSE) for p in line]
    assert max(p.x for p in front) - min(p.x for p in front) == pytest.approx(0.25 if discs else 0)
    ET.fromstring(elevation.draw(elevation.plan(structure), interactive=False, occurrence=""))


def test_a_frame_is_drawn_from_its_pole_tops_down() -> None:
    (view,) = elevation.plan(TH_230).views
    assert view.bounds.left == pytest.approx(-ft_in(20, 0).si)
    assert view.bounds.right == pytest.approx(ft_in(20, 0).si)
    assert view.bounds.top == pytest.approx(0)
    assert pages.StructureFigure(TH_230).heading == "Upper structure"
    assert pages.StructureFigure(LCRA).heading == "Elevation"


def test_ground_follows_the_datum_or_tower_feet_without_inventing_pole_heights() -> None:
    assert elevation.ground(AS4_AD90) == 0
    assert elevation.ground(LCRA) == pytest.approx(ft_in(154, 9).si)
    assert elevation.ground(TH_230) is None
    assert elevation.ground(barred()) is None
    for structure in (LCRA, AS4_AD90, MT_008_004):
        drawing = elevation.plan(structure)
        assert all(view.ground == elevation.ground(structure) for view in drawing.views)
        for interactive in (False, True):
            root = ET.fromstring(elevation.draw(drawing, interactive=interactive, occurrence=""))
            ground = [node for node in root.iter() if node.get("class") == "ol-ground"]
            assert len(ground) == 1  # Both elevations share one grade line and label.
            assert all("Nominal ground" in "".join(node.itertext()) for node in ground)
            assert all(node.get("tabindex") is None for group in ground for node in group.iter())
    root = ET.fromstring(elevation.draw(elevation.plan(TH_230), interactive=False, occurrence=""))
    assert not any(node.get("class") == "ol-ground" for node in root.iter())


def test_the_sheet_tabulates_bars_poles_and_crossarms() -> None:
    blocks = {block.title: block for block in pages.sheet(barred()).blocks}
    assert blocks["Bars"].rows == [["Body 1", "Steel", "chord", "1"]]
    frame = {block.title: block for block in pages.sheet(TH_230).blocks}
    assert frame["Pole tops"].rows == [["1", "-2.972", "0", "0"], ["2", "2.972", "0", "0"]]
    assert frame["Crossarms"].rows == [
        ["Wood", "-6.096, 0, -2.896", "6.096, 0, -2.896", "92.07 \u00d7 238.1", "2"]
    ]
    assert all(block.rows for block in frame.values())
    (grid,) = pages.grids([("unwired", barred())])
    (_, cells), *_ = grid.rows
    assert cells[4:6] == ["\u2014", "\u2014"]  # no wires: no phase or shield points


@pytest.mark.parametrize("tower", DRAWN, ids=[tower.name for tower in DRAWN])
def test_a_tower_s_elevations_keep_every_mount_and_draw_as_svg(tower: Tower[Any]) -> None:
    corners = {
        point
        for part in tower.parts
        if isinstance(part.construction, PanelRun)
        for edge in (part.construction.start, *(bay.edge for bay in part.construction.panels))
        for point in (edge.start, edge.end)
    }
    corners |= {
        joint
        for part in tower.parts
        if isinstance(part.construction, Truss)
        for joint in part.construction.joints
    }
    assert all(a.point in corners for a in tower.attachments if isinstance(a, Mount))
    drawing = elevation.plan(tower)
    assert len(drawing.views[0].anchors) == len(tower.attachments)
    for view in drawing.views:
        assert view.path
        assert view.bounds.width > 0
        assert view.bounds.bottom > view.bounds.top
        assert all(math.isfinite(v) for v in astuple(view.bounds))
    for interactive in (False, True):
        root = ET.fromstring(elevation.draw(drawing, interactive=interactive, occurrence="one-"))
        assert root.get("role") == ("group" if interactive else "img")
        if not interactive:
            assert all(n.get("tabindex") is None for n in root.iter())


def test_side_view_uses_the_same_physical_scale() -> None:
    drawing = elevation.plan(MT_008_004)
    assert [view.name for view in drawing.views] == ["Front", "Side"]
    root = ET.fromstring(elevation.draw(drawing, interactive=False, occurrence=""))
    scales = [
        n.get("transform", "").split("scale(")[1]
        for n in root.iter()
        if "scale(" in n.get("transform", "")
    ]
    assert len(scales) == 2
    assert scales[0] == scales[1]
    assert not drawing.views[1].anchors


def test_changing_a_panel_changes_generated_members_without_source_files() -> None:
    part = AS4_AD90.body[0]
    run = part.construction
    assert isinstance(run, PanelRun)
    first, *rest = run.panels
    changed = replace(
        AS4_AD90,
        body=(
            replace(
                part, construction=replace(run, panels=(replace(first, bays=first.bays + 1), *rest))
            ),
            *AS4_AD90.body[1:],
        ),
    )
    assert elevation.plan(changed).views[0].path != elevation.plan(AS4_AD90).views[0].path


def test_every_structure_with_a_drawing_has_a_figure() -> None:
    for structure in structures.of(Structure):
        drawn = pages.figures(structure)
        for figure in drawn:
            root = ET.fromstring(figure.svg(interactive=False, occurrence="static-"))
            assert root.get("role") == "img"
            assert not any(n.get("role") == "button" or n.get("tabindex") for n in root.iter())
        if not drawn:
            assert not isinstance(structure, Tower) or not structure.body, structure.name
