"""A conductor's construction seen from the side, each layer cut back from the one within it:
every wire turns about the axis as openline lays it, at its layer's radius, lay and hand.

A wire at turn angle ψ, ψ = 0 facing the viewer, lies at depth cos ψ. Each of its passes is drawn
in pieces within which depth runs one way: its front, within half a pitch of ψ = 0; its rising
and falling sides, round to half a pitch past the outline, as far as the wire nearest the outline
ever is; and, where a layer has three wires, its back. Neighbors change places in front only
midway between them, where they just touch, so drawing the backs, then the sides by how far
round they are, then the fronts, puts every wire behind those in front of it.

A band of trapezoidal wires shows its outside alone, closed: each wire a ribbon between its seams
with its neighbors, at ψ ± π/n, held at the outline once past it. Ribbons meet seam to seam, so
none is drawn behind another.

A layer's pieces are drawn once, in its definitions, and placed at each pass. What a ``use``
copies takes no style from the page's selectors, so each stroke's color is a variable its part's
group sets: a figure grows with its passes, not its points, and keeps its metals and themes."""

import math
from collections.abc import Iterator

from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.conductors.strands import Band, Hand, HelicalBand, Helix, Layer, Ring, Strand
from openline.types.materials import Metal
from openline.types.units import mm, symbol

from . import metals, svg
from .section import wire
from .svg import XY, number

DIAMETER = 100.0  # the conductor's, in drawing units
OUTER, STEP = 1.6, 0.8  # how far its outer layer runs, and each within it further, in diameters
BODY, SHEEN, LIFT = 0.84, 0.3, 0.32  # a wire's body and its light, of its diameter; the light's
#                                      offset above its axis, of its radius
JOIN = 0.015  # radians a piece runs past a joint it is drawn over: its body once, its light twice
SEAM, GROOVE = 0.45, 0.7  # a band's seams, and the light along each beneath it, in drawing units
HALF = math.pi / 2
PIECES = ("back-rise", "back-fall", "rise", "fall", "front")  # in the order they are drawn

type Span = tuple[float, float]  # turn angles, radians
type Strokes = tuple[Span, Span, Span]  # of a piece's outline, body and light


def helical(record: Conductor) -> bool:
    """Whether openline lays every ring and band of it, its lay and its hand: what its cutback
    takes."""
    try:
        layers = record.layers
    except Missing:
        return False
    return all(
        isinstance(layer, Helix | HelicalBand) and layer.hand is not None
        for layer in layers
        if isinstance(layer, Ring | Band)
    )


def reach(wires: int) -> tuple[float, float, float]:
    """Of a layer of ``wires``: half its pitch, where neighbors change places in front; how far
    round a wire is drawn, half a pitch past the outline; and where its back begins, half a pitch
    short of ψ = π."""
    mid = math.pi / wires
    return mid, HALF + mid, math.pi - mid


def spans(wires: int) -> dict[str, Strokes]:
    """Each piece's turn angles for its outline, body and light. A piece drawn under a joint runs
    past it in full; the piece drawn over it ends its outline at the joint, its body ``JOIN``
    past and its light twice that, so each end lies on its own color and no seam shows."""
    mid, edge, back = reach(wires)

    def over(a: float, b: float, start: bool, end: bool) -> Strokes:
        return (
            (a, b),
            (a - JOIN * start, b + JOIN * end),
            (a - 2 * JOIN * start, b + 2 * JOIN * end),
        )

    def under(a: float, b: float) -> Strokes:
        return ((a, b),) * 3

    if edge <= back:
        found = {"rise": under(-edge, -mid + JOIN), "fall": under(mid - JOIN, edge)}
    else:  # three wires: the back shows at the outline
        found = {
            "back-rise": under(-edge, -back + JOIN),
            "back-fall": under(back - JOIN, edge),
            "rise": over(-back, -mid + JOIN, True, False),
            "fall": over(mid - JOIN, back, False, True),
        }
    return {**found, "front": over(-mid, mid, True, True)}


def curve(lay: float, radius: float, sign: int, span: Span, shift: float = 0.0) -> str:
    """A wire's axis over turn angles ``span``, either way, as cubic Béziers at most π/4 apart:
    at ψ it lies at x = λ(ψ + π/2)/2π along the conductor, and ``shift`` further, and y = ±a sin ψ
    across it, with λ its lay and a its layer's radius."""

    def at(psi: float) -> XY:
        return XY(lay * (psi + HALF) / (2 * math.pi) + shift, sign * radius * math.sin(psi))

    def slope(psi: float) -> XY:
        return XY(lay / (2 * math.pi), sign * radius * math.cos(psi))

    a, b = span
    steps = max(1, math.ceil(abs(b - a) / (math.pi / 4)))
    step = (b - a) / steps
    found = f"M{number(at(a).x)},{number(at(a).y)}"
    for k in range(steps):
        p, q = a + k * step, a + (k + 1) * step
        start, end, leave, enter = at(p), at(q), slope(p), slope(q)
        h = step / 3
        found += (
            f"C{number(start.x + h * leave.x)},{number(start.y + h * leave.y)}"
            f" {number(end.x - h * enter.x)},{number(end.y - h * enter.y)}"
            f" {number(end.x)},{number(end.y)}"
        )
    return found


def ribbon(lay: float, radius: float, sign: int, wires: int) -> str:
    """One pass of a band's wire, as the band's outside shows it: across the conductor from one
    side of the outline to the other, between its seams r sin(ψ ± π/n), each held at the outline
    once past it. Its seams lie half a pitch either side of its middle, so one pass's leading
    seam is the next's trailing one."""
    half = lay / (2 * wires)
    leading = curve(lay, radius, sign, (-HALF, HALF), -half)
    trailing = curve(lay, radius, sign, (HALF, -HALF), half)
    return f"{leading}H{number(lay / 2 + half)}{trailing[trailing.index('C') :]}Z"


def sleeve(identifier: str, lay: float, radius: float, sign: int, wires: int) -> str:
    """A band's ribbon, drawn once: filled with its body's gradient, its seams the outline's
    color, and the light along its upper seam, as a groove's lower wall catches it."""
    top = curve(lay, radius, sign, (-HALF, HALF), lay / (2 * wires) * sign)
    return (
        f'<g id="{identifier}"><path d="{ribbon(lay, radius, sign, wires)}"'
        f' stroke-width="{number(SEAM)}" stroke-linejoin="round"'
        ' style="fill:var(--ol-round);stroke:var(--ol-edge)"/>'
        f'<path d="{top}" fill="none" stroke-width="{number(GROOVE)}"'
        f' transform="translate(0,{number(GROOVE)})" style="stroke:var(--ol-shine)"/></g>'
    )


def cuts(count: int) -> list[Span]:
    """Where each of ``count`` layers shows, from the center out, along the conductor: the outer
    from its end, each within it from just under the end of the one outside it."""
    ends = [(OUTER + STEP * (count - 1 - depth)) * DIAMETER for depth in range(count)]
    return [
        (0.0 if depth == count - 1 else ends[depth + 1] - 1, ends[depth]) for depth in range(count)
    ]


def passes(lay: float, wires: int, cut: Span) -> list[float]:
    """Where each pass of a band's wires that shows within ``cut`` is at ψ = -π/2, a pitch apart:
    every one whose ribbon reaches into it, at the outline or anywhere across."""
    pitch, half = lay / wires, lay / (2 * wires)
    low = (cut[0] - lay / 2 - half + lay / 4) / pitch
    high = (cut[1] + half + lay / 4) / pitch
    return [-lay / 4 + k * pitch for k in range(math.floor(low) + 1, math.ceil(high))]


def ordered(layer: Helix, lay: float, cut: Span) -> list[tuple[str, float, Strand[Metal]]]:
    """Each piece a layer shows within ``cut``, back to front: its name, where its pass begins
    along the conductor, and its wire. At any point the backs and the fronts hold one wire each;
    along a side, a wire further round is deeper, and an earlier pass is further round."""
    start, end = cut
    wires = len(layer.wires)
    beyond = lay * (reach(wires)[1] - HALF) / (2 * math.pi)
    passes: list[tuple[float, Strand[Metal]]] = []
    for i, strand in enumerate(layer.wires):
        base = -lay * (0.25 + i / wires)  # where a pass of it is at ψ = -π/2
        first = math.ceil((start - lay / 2 - beyond - base) / lay)
        last = math.floor((end + beyond - base) / lay)
        passes.extend((base + j * lay, strand) for j in range(first, last + 1))
    ahead = sorted(passes, key=lambda given: given[0])
    pieces = spans(wires)

    def shown(piece: str, base: float) -> bool:
        low = min(a for a, _ in pieces[piece])
        high = max(b for _, b in pieces[piece])
        return base + lay * (high + HALF) / (2 * math.pi) > start and (
            base + lay * (low + HALF) / (2 * math.pi) < end
        )

    found: list[tuple[str, float, Strand[Metal]]] = []
    for piece in PIECES:
        if piece in pieces:
            given = ahead[::-1] if piece in ("back-rise", "rise") else ahead
            found.extend((piece, base, strand) for base, strand in given if shown(piece, base))
    return found


def strokes(identifier: str, width: float, paths: tuple[str, str, str]) -> str:
    """A piece's outline, body and light along its paths, drawn once; one path where all three
    share it. Each stroke's color is a variable of its part's group."""
    edge, body, sheen = paths
    shared = edge == body == sheen
    drawn = [f'<use href="#{identifier}-axis"'] * 3 if shared else [f'<path d="{p}"' for p in paths]
    return (
        (f'<path id="{identifier}-axis" d="{edge}"/>' if shared else "")
        + f'<g id="{identifier}" fill="none">'
        + f'{drawn[0]} stroke-width="{number(width)}" style="stroke:var(--ol-edge)"/>'
        + f'{drawn[1]} stroke-width="{number(width * BODY)}" style="stroke:var(--ol-round)"/>'
        + f'{drawn[2]} stroke-width="{number(width * SHEEN)}"'
        + f' transform="translate(0,{number(-width / 2 * LIFT)})" style="stroke:var(--ol-shine)"/>'
        + "</g>"
    )


def shades(occurrence: str, record: Conductor) -> Iterator[str]:
    """Each part's shading as a round conductor, its body's and its light's: lit above, darker
    below, darkest where its wires turn away at the outline. A layer's gradients take these
    stops at its own height."""
    for index, (name, strand) in enumerate(record.parts):
        for kind, extra in (("round", ""), ("shine", " ol-shine")):
            yield (
                f'<linearGradient id="{occurrence}cutback-{index}-{kind}" data-ol-key="{name}"'
                f' class="ol-round{extra} {metals.classes(strand.material)}"'
                ' gradientUnits="userSpaceOnUse" x1="0" x2="0"><stop class="ol-rim"/>'
                '<stop class="ol-lit" offset=".3"/><stop class="ol-tone" offset=".55"/>'
                '<stop class="ol-deep" offset=".85"/><stop class="ol-rim" offset="1"/>'
                "</linearGradient>"
            )


def cutback(record: Conductor, title: str, *, interactive: bool, occurrence: str) -> str:
    """Its layers from the side, each cut back from the one within it, its diameter beside."""
    if not helical(record):
        raise Missing(f"{record.title}: openline does not have the lay of each of its layers")
    layers: tuple[Layer[Strand[Metal]], ...] = record.layers
    scale = DIAMETER / record.diameter.to(mm)
    parts = {id(strand): (index, name) for index, (name, strand) in enumerate(record.parts)}
    defs = list(shades(occurrence, record))
    groups: list[str] = []
    named: set[str] = set()
    for depth, (layer, cut) in enumerate(zip(layers, cuts(len(layers)), strict=True)):
        prefix = f"{occurrence}c{depth}"
        start, end = cut
        outside = layer.outer_radius.to(mm) * scale
        defs.append(
            f'<clipPath id="{prefix}-clip"><rect x="{number(start)}" y="{number(-outside - 1)}"'
            f' width="{number(end - start)}" height="{number(2 * outside + 2)}"/></clipPath>'
        )
        for index, _ in {parts[id(strand)] for strand in layer.wires}:
            defs.extend(
                f'<linearGradient id="{prefix}-{index}-{kind}"'
                f' href="#{occurrence}cutback-{index}-{kind}"'
                f' y1="{number(-outside)}" y2="{number(outside)}"/>'
                for kind in ("round", "shine")
            )
        width = layer.wires[0].diameter.to(mm) * scale
        placed: list[tuple[str, float, Strand[Metal]]]  # each piece, where its pass is, its wire
        if isinstance(layer, HelicalBand):
            lay, wires = layer.lay.to(mm) * scale, len(layer.wires)
            sign = 1 if layer.hand is Hand.RIGHT else -1
            defs.append(sleeve(f"{prefix}r", lay, outside, sign, wires))
            placed = [(f"{prefix}r", base, layer.wires[0]) for base in passes(lay, wires, cut)]
        elif isinstance(layer, Helix):
            lay, radius = layer.lay.to(mm) * scale, layer.radius.to(mm) * scale
            sign = 1 if layer.hand is Hand.RIGHT else -1
            for piece, angles in spans(len(layer.wires)).items():
                outline, inner, light = (curve(lay, radius, sign, span) for span in angles)
                paths = (outline, inner, light)
                defs.append(strokes(f"{prefix}p{PIECES.index(piece)}", width, paths))
            placed = [
                (f"{prefix}p{PIECES.index(piece)}", base, strand)
                for piece, base, strand in ordered(layer, lay, cut)
            ]
        else:  # the wire on the axis, straight
            axis = f"M{number(start)},0H{number(end)}"
            defs.append(strokes(f"{prefix}p", width, (axis, axis, axis)))
            placed = [(f"{prefix}p", 0.0, layer.wires[0])]
        shown: set[str] = set()
        runs: list[tuple[Strand[Metal], list[str]]] = []  # one part's consecutive pieces
        for identifier, base, strand in placed:
            if not runs or runs[-1][0] is not strand:
                runs.append((strand, []))
            runs[-1][1].append(f'<use href="#{identifier}" x="{number(base)}"/>')
        for strand, uses in runs:
            index, name = parts[id(strand)]
            label = f"{name.capitalize()}: {wire(strand)}"
            control = "" if name in named else svg.controls(interactive, label)
            heading = "" if name in shown else f"<title>{label}</title>"
            named.add(name)
            shown.add(name)
            groups.append(
                f'<g class="ol-part {metals.classes(strand.material)}" data-ol-key="{name}"'
                f' clip-path="url(#{prefix}-clip)" style="--ol-round:url(#{prefix}-{index}-round);'
                f'--ol-shine:url(#{prefix}-{index}-shine)"{control}>{heading}{"".join(uses)}</g>'
            )
    half = DIAMETER / 2
    diameter = f"Ø {record.diameter.to(mm):.4g} {symbol(mm)}"
    body = f"<defs>{''.join(defs)}</defs>{''.join(groups)}" + svg.dimension(
        XY(0, -half), XY(0, half), diameter, -14
    )
    return svg.svg(
        "cutback",
        (-34.0, -62.0, cuts(len(layers))[0][1] + 44, 124.0),
        f"{title} construction",
        "Each layer cut back from the one within it, seen from the side: every wire at its "
        "layer's radius, lay and hand, as openline lays them, behind those in front of it.",
        body,
        interactive=interactive,
    )
