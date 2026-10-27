"""A structure's elevations, drawn orthographically from its catalog parts at one scale: across
the line, and along it where its points lie apart along it; where it holds its wires, each a
point its specification's rows select; its overall width and height; and its nominal ground,
where its datum or its legs give one."""

import math
from collections.abc import Iterable
from dataclasses import dataclass
from html import escape
from typing import Any

from openline.types.structures import Frame, Ground, Pole, PoleTop, Structure, Tower
from openline.types.structures.attachments import DiscString, Wire, WirePosition
from openline.types.structures.geometry import Face, Point
from openline.types.structures.members import Beam, Truss
from openline.types.structures.panels import Bracing, Edge, Panel, PanelRun
from openline.types.units import m, symbol

from . import svg
from .svg import XY, number

type Segment = tuple[XY, XY]

WIDTH, HEIGHT = 1200.0, 864.0  # drawing units; its container sets its size
MARGIN, GAP, FOOTER = 80.0, 90.0, 140.0


@dataclass(frozen=True, slots=True)
class Bounds:
    """An elevation's extent, in meters, its y downwards."""

    left: float
    top: float
    right: float
    bottom: float

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top


@dataclass(frozen=True, slots=True)
class Anchor:
    """Where it holds a wire: a point its specification's row of that key selects."""

    key: str
    point: XY
    shield: bool
    label: str


@dataclass(frozen=True, slots=True)
class Dimension:
    """A length of an elevation, drawn ``offset`` beyond its ends."""

    start: XY
    end: XY
    label: str
    offset: float


@dataclass(frozen=True, slots=True)
class Elevation:
    """One face of a structure: its linework, its anchors, its dimensions and its ground."""

    name: str
    bounds: Bounds
    path: str
    anchors: tuple[Anchor, ...]
    dimensions: tuple[Dimension, ...]
    ground: float | None = None
    """Nominal ground, its y, where its datum or its legs give one."""


@dataclass(frozen=True, slots=True)
class Elevations:
    """A structure's elevations, sharing a scale."""

    title: str
    description: str
    views: tuple[Elevation, ...]

    @property
    def dimensioned(self) -> bool:
        return any(view.dimensions for view in self.views)


def point(given: Point, face: Face) -> XY:
    """A point projected across or along the line, its height upwards."""
    return XY(given.across.si if face is Face.TRANSVERSE else given.along.si, -given.height.si)


def between(a: XY, b: XY, fraction: float) -> XY:
    return XY(a.x + (b.x - a.x) * fraction, a.y + (b.y - a.y) * fraction)


def closed(points: tuple[XY, ...]) -> tuple[Segment, ...]:
    return tuple(zip(points, (*points[1:], points[0]), strict=True)) if len(points) > 1 else ()


def panel(start: Edge, given: Panel, face: Face) -> tuple[Segment, ...]:
    """A panel's chords, its boundary ties and its repeated web members."""
    a, b, c, d = (
        point(p, face) for p in (start.start, start.end, given.edge.start, given.edge.end)
    )
    lines = [(a, b), (c, d), (a, c), (b, d)]
    for i in range(given.bays):
        lo, hi = i / given.bays, (i + 1) / given.bays
        p, q, r, s = between(a, c, lo), between(b, d, lo), between(a, c, hi), between(b, d, hi)
        match given.bracing:
            case Bracing.CROSS:
                lines.extend(((p, q), (r, s), (p, s), (q, r)))
            case Bracing.PRATT:
                lines.extend(((p, q), (r, s), (q, r)))
            case Bracing.WARREN:
                lines.append((p, s) if i % 2 == 0 else (q, r))
            case Bracing.DIAMOND:
                corners = (
                    between(p, q, 0.5),
                    between(q, s, 0.5),
                    between(r, s, 0.5),
                    between(p, r, 0.5),
                )
                lines.extend(zip(corners, (*corners[1:], corners[0]), strict=True))
            case Bracing.OPEN:
                pass
    return tuple(lines)


def paths(lines: Iterable[Segment]) -> str:
    """One stroke for members shared by neighbouring panels."""
    seen = set()
    result = []
    for a, b in lines:
        key = tuple(sorted((tuple(round(v, 6) for v in a), tuple(round(v, 6) for v in b))))
        if key in seen or math.dist(a, b) < 1e-6:
            continue
        seen.add(key)
        result.append(f"M{a.x:.6g},{a.y:.6g}L{b.x:.6g},{b.y:.6g}")
    return "".join(result)


def beam(member: Beam[Any], face: Face) -> tuple[Segment, ...]:
    """A crossarm's outline, its depth upright; seen end on, its line."""
    a, b = point(member.start, face), point(member.end, face)
    length = math.dist(a, b)
    if face is Face.LONGITUDINAL or not length:
        return ((a, b),)
    dx, dy = (b.x - a.x) / length, (b.y - a.y) / length
    half = member.section.depth.si / 2
    return closed(
        tuple(
            XY(p.x - dy * half * sign, p.y + dx * half * sign)
            for p, sign in ((a, 1), (b, 1), (b, -1), (a, -1))
        )
    )


def construction(given: PanelRun | Truss[Any], face: Face) -> tuple[Segment, ...]:
    """A part's lines: its outline's panels in their plane, or its bars."""
    if isinstance(given, PanelRun):
        if given.face is not face:
            return ()
        lines: list[Segment] = []
        edge = given.start
        for bay in given.panels:
            lines.extend(panel(edge, bay, face))
            edge = bay.edge
        return tuple(lines)
    return tuple((point(bar.start, face), point(bar.end, face)) for bar in given.bars)


def strings(structure: Structure[Any], face: Face) -> list[Segment]:
    """Each wire position's insulator strings, from their mounts to the wire, and the discs of
    a disc string."""
    lines = []
    for attachment in structure.attachments:
        if not isinstance(attachment, WirePosition):
            continue
        wire = attachment.point
        end = point(wire, face)
        for string in attachment.strings:
            start = point(string.mount, face)
            lines.append((start, end))
            if isinstance(string, DiscString):
                lines.extend(discs(string, wire, start, end))
    return lines


def discs(string: DiscString, wire: Point, start: XY, end: XY) -> list[Segment]:
    """A disc string's discs, each a rim about its place along the string, from the wire up."""
    mount = (string.mount.across.si, string.mount.along.si, string.mount.height.si)
    span = math.dist(mount, (wire.across.si, wire.along.si, wire.height.si))
    distance = math.dist(start, end)
    ratio = min(1, distance / span)
    dx, dy = ((end.x - start.x) / distance, (end.y - start.y) / distance) if distance else (1, 0)
    pitch = string.length.si / string.discs
    radius = string.diameter.si / 2
    axial = math.hypot(radius * math.sqrt(max(0, 1 - ratio**2)), pitch * 0.22 * ratio)
    lines: list[Segment] = []
    for i in range(string.discs):
        center = between(end, start, (i + 0.5) * pitch / span)
        rim = tuple(
            XY(
                center.x - dy * radius * math.cos(t) + dx * axial * math.sin(t),
                center.y + dx * radius * math.cos(t) + dy * axial * math.sin(t),
            )
            for t in (2 * math.pi * j / 12 for j in range(12))
        )
        lines.extend(closed(rim))
    return lines


def crossarms(structure: Structure[Any]) -> tuple[Beam[Any], ...]:
    """A frame's or pole's crossarms; a tower's are parts."""
    return structure.crossarms if isinstance(structure, Frame | Pole) else ()


def located(structure: Structure[Any]) -> list[Point]:
    """Every point a structure gives: its parts', its attachments' and strings', and its
    poles' tops."""
    found: list[Point] = [a.point for a in structure.attachments]
    for attachment in structure.attachments:
        if isinstance(attachment, WirePosition):
            found.extend(string.mount for string in attachment.strings)
    for part in structure.parts:
        if isinstance(part.construction, Truss):
            found.extend(part.construction.joints)
    for arm in crossarms(structure):
        found.extend((arm.start, arm.end))
    if isinstance(structure, Frame):
        found.extend(structure.poles)
    return found


def orientations(structure: Structure[Any]) -> tuple[Face, ...]:
    """The faces it is drawn in: each of its outlines' planes, across the line where it has
    bars, crossarms or poles, and along it where its points lie apart along it."""
    selected = {
        part.construction.face
        for part in structure.parts
        if isinstance(part.construction, PanelRun)
    }
    if not isinstance(structure, Tower) or any(
        isinstance(part.construction, Truss) for part in structure.parts
    ):
        selected.add(Face.TRANSVERSE)
    points = located(structure)
    if points and max(p.along.si for p in points) - min(p.along.si for p in points) > 1e-9:
        selected.add(Face.LONGITUDINAL)
    return tuple(face for face in Face if face in selected)


def poles(structure: Structure[Any], lowest: float) -> list[Segment]:
    """A frame's or pole's poles across the line, from their tops down past the lowest thing
    drawn: the line sets how long they are. A pole's top is its datum where its datum is the
    pole top, or else its highest attachment."""
    if isinstance(structure, Frame):
        tops = [point(top, Face.TRANSVERSE) for top in structure.poles]
    elif isinstance(structure, Pole):
        highest = (point(a.point, Face.TRANSVERSE).y for a in structure.attachments)
        tops = [XY(0, 0 if isinstance(structure.datum, PoleTop) else min(highest, default=0))]
    else:
        return []
    return [(top, XY(top.x, lowest)) for top in tops]


def ground(structure: Structure[Any]) -> float | None:
    """The nominal grade, not an inferred installation height for an upper-only drawing: a
    ground datum's, or a complete tower's lowest leg ends', its nominal base plane; neither
    describes foundations or site grading."""
    if isinstance(structure.datum, Ground):
        return 0.0
    if isinstance(structure, Tower):
        feet = [
            p.y
            for leg in structure.legs
            for face in Face
            for line in construction(leg.construction, face)
            for p in line
        ]
        if feet:
            return max(feet)
    return None


def plan(structure: Structure[Any]) -> Elevations:
    """Its elevations, in meters and at a common scale."""
    views = []
    ground_level = ground(structure)
    for face in orientations(structure):
        lines = [line for part in structure.parts for line in construction(part.construction, face)]
        lines.extend(line for arm in crossarms(structure) for line in beam(arm, face))
        lines.extend(strings(structure, face))
        if face is Face.TRANSVERSE:
            lowest = max((point(a.point, face).y for a in structure.attachments), default=0)
            lowest = max(lowest, *(p.y for line in lines for p in line), 0)
            lines.extend(poles(structure, lowest))
        path = paths(lines)
        if not path:
            continue
        anchors = (
            tuple(
                Anchor(
                    str(i),
                    point(a.point, face),
                    a.wire is Wire.SHIELD,
                    f"{a.wire}, {a.hold}, {a.point}",
                )
                for i, a in enumerate(structure.attachments)
            )
            if face is Face.TRANSVERSE
            else ()
        )
        ys = [p.y for line in lines for p in line] + [a.point.y for a in anchors]
        xs = [p.x for line in lines for p in line] + [a.point.x for a in anchors]
        if ground_level is not None:
            ys.append(ground_level)
        bounds = Bounds(min(xs), min(ys), max(xs), max(ys))
        dimensions: list[Dimension] = []
        if bounds.width > 1e-9:
            dimensions.append(
                Dimension(
                    XY(bounds.left, bounds.top),
                    XY(bounds.right, bounds.top),
                    f"{bounds.width:.4g}\u202f{symbol(m)}",
                    35,
                )
            )
        if bounds.height > 1e-9:
            dimensions.append(
                Dimension(
                    XY(bounds.right, bounds.top),
                    XY(bounds.right, bounds.bottom),
                    f"{bounds.height:.4g}\u202f{symbol(m)}",
                    35,
                )
            )
        views.append(
            Elevation(
                "Front" if face is Face.TRANSVERSE else "Side",
                bounds,
                path,
                anchors,
                tuple(dimensions),
                ground_level,
            )
        )
    description = "Structure elevations."
    if ground_level is not None:
        description += (
            " Nominal ground follows the ground datum or modeled tower base."
            " Foundations and site grading are not shown."
        )
    return Elevations(structure.title, description, tuple(views))


def draw(drawing: Elevations, *, interactive: bool, occurrence: str) -> str:
    """Its views side by side, at their common vertical scale."""
    views = drawing.views
    if not views:
        raise ValueError("A drawing needs at least one view")
    top = min(view.bounds.top for view in views)
    bottom = max(view.bounds.bottom for view in views)
    footer = FOOTER if any(view.ground is not None for view in views) else MARGIN
    span = sum(view.bounds.width for view in views)
    scale = min(
        (WIDTH - 2 * MARGIN - GAP * (len(views) - 1)) / max(span, 1e-9),
        (HEIGHT - MARGIN - footer) / max(bottom - top, 1e-9),
    )
    left = (WIDTH - span * scale - GAP * (len(views) - 1)) / 2
    body: list[str] = []
    grounds: dict[float, tuple[float, float]] = {}
    for view in views:
        tx = left - view.bounds.left * scale
        ty = MARGIN + (HEIGHT - MARGIN - footer - (bottom - top) * scale) / 2 - top * scale

        def at(given: XY, tx: float = tx, ty: float = ty) -> XY:
            return XY(tx + given.x * scale, ty + given.y * scale)

        if view.ground is not None:
            y = at(XY(0, view.ground)).y
            start, end = left - 24, left + view.bounds.width * scale + 24
            grounds[y] = (grounds[y][0] if y in grounds else start, end)
        body.append(
            f'<path class="ol-ink" d="{view.path}"'
            f' transform="translate({tx:g},{ty:g}) scale({scale:g})"/>'
        )
        body.extend(
            svg.dimension(at(d.start), at(d.end), d.label, d.offset) for d in view.dimensions
        )
        for anchor in view.anchors:
            p = at(anchor.point)
            glyph = (
                '<path class="ol-dot" d="M0,-6.5L6.5,0L0,6.5L-6.5,0Z"/>'
                if anchor.shield
                else '<circle class="ol-dot" r="5"/>'
            )
            control = ' role="button" tabindex="0" aria-pressed="false"' if interactive else ""
            body.append(
                f'<g class="ol-anchor" data-ol-key="{escape(anchor.key, quote=True)}"'
                f' data-ol-wire="{"shield" if anchor.shield else "phase"}"'
                f' transform="translate({number(p.x)},{number(p.y)})"{control}'
                f' aria-label="{escape(anchor.label, quote=True)}">'
                f"<title>{escape(anchor.label)}</title>"
                f'<circle class="ol-hit" r="20"/><circle class="ol-ring" r="11"/>{glyph}</g>'
            )
        if len(views) > 1:
            x = left + view.bounds.width * scale / 2
            body.append(
                f'<text class="ol-label ol-view" x="{number(x)}" y="{number(HEIGHT - 12)}">'
                f"{escape(view.name)}</text>"
            )
        left += view.bounds.width * scale + GAP
    for y, (start, end) in grounds.items():
        hatches = "".join(f"M{x:g},{y:g}l-8,10" for x in range(round(start) + 12, round(end), 24))
        body.insert(
            0,
            '<g class="ol-ground">'
            f'<path class="ol-hatch" d="{hatches}"/>'
            f'<path class="ol-rule" d="M{number(start)},{number(y)}H{number(end)}"/>'
            f'<text class="ol-label" x="{number((start + end) / 2)}" y="{number(y + 12)}"'
            ' dy="1.2em">Nominal ground</text></g>',
        )
    return svg.svg(
        "elevation",
        (0.0, 0.0, WIDTH, HEIGHT),
        drawing.title,
        drawing.description,
        "".join(body),
        interactive=interactive,
    )
