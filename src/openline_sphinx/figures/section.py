"""A conductor's cross section: each wire where openline lays it, a round one a disc and a
trapezoidal one its sector of a band, in its part's group, shaded in its material. A strand
openline cannot lay, as trapezoidal wires whose layers no document gives, fills a ring of its
area around those it lays; no layers are guessed."""

import math

from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.conductors.strands import Band, Layer, Ring, Round, Strand, layout
from openline.types.materials import Metal
from openline.types.units import mm, mm2, symbol

from . import metals, svg
from .svg import XY, number

RADIUS = 100.0  # the conductor's, in drawing units
GAP = 0.8  # drawing units between trapezoidal wires, and between their layers


def laid(record: Conductor) -> tuple[tuple[Layer[Strand[Metal]], ...], tuple[Strand[Metal], ...]]:
    """Its layers of wires as openline lays them, and the strands it cannot lay: its
    trapezoidal ones, or every one where its round wires make no rings."""
    try:
        return record.layers, ()
    except Missing:
        rounds = [strand for strand in record.strands if isinstance(strand, Round)]
        others = tuple(strand for strand in record.strands if not isinstance(strand, Round))
        try:
            return layout(rounds), others
        except Missing:
            return (), record.strands


def wire(strand: Strand[Metal]) -> str:
    """A strand as a reader names it: ``26 round wires of 4.442 mm, Aluminum 1350-H19``."""
    shape = type(strand).__name__.lower()
    size = f"{strand.diameter.to(mm):.4g} {symbol(mm)}"
    return f"{strand.count} {shape} wires of {size}, {strand.material.name}"


def sector(inner: float, outer: float, start: float, end: float) -> str:
    """A trapezoidal wire as drawn: the annulus between two radii, between two angles."""

    def at(radius: float, angle: float) -> str:
        return f"{number(radius * math.cos(angle))},{number(radius * math.sin(angle))}"

    o, i = number(outer), number(inner)
    return (
        f"M{at(outer, start)}A{o},{o} 0 0,1 {at(outer, end)}"
        f"L{at(inner, end)}A{i},{i} 0 0,0 {at(inner, start)}Z"
    )


def circle(radius: float) -> str:
    """A circle about the axis, as a path: two half arcs."""
    r = number(radius)
    return f"M-{r},0A{r},{r} 0 1,0 {r},0A{r},{r} 0 1,0 -{r},0Z"


def section(record: Conductor, title: str, *, interactive: bool, occurrence: str) -> str:
    """Its cross section; its overall diameter above it where openline lays every wire."""
    layers, filled = laid(record)
    outside = layers[-1].outer_radius.to(mm) if layers else 0.0
    rings: dict[int, tuple[float, float]] = {}  # a filled strand's inner and outer radius, mm
    for strand in reversed(filled):  # from the inside out
        inner, outside = outside, math.sqrt(outside**2 + strand.area.to(mm2) / math.pi)
        rings[id(strand)] = (inner, outside)
    scale = RADIUS / outside
    discs: dict[int, list[str]] = {id(strand): [] for strand in record.strands}
    for depth, layer in enumerate(layers):
        if isinstance(layer, Band):
            inner, outer = layer.inner.to(mm) * scale + GAP, layer.outer.to(mm) * scale
            step = 2 * math.pi / len(layer.wires)
            for i, strand in enumerate(layer.wires):
                start = step * (i + depth % 2 / 2) - math.pi / 2
                path = sector(inner, outer, start + GAP / outer, start + step - GAP / outer)
                discs[id(strand)].append(f'<path d="{path}"/>')
            continue
        r = layer.radius.to(mm) * scale if isinstance(layer, Ring) else 0.0
        for i, strand in enumerate(layer.wires):
            angle = 2 * math.pi * (i + depth % 2 / 2) / len(layer.wires) - math.pi / 2
            discs[id(strand)].append(
                f'<circle cx="{number(r * math.cos(angle))}" cy="{number(r * math.sin(angle))}"'
                f' r="{number(strand.diameter.to(mm) / 2 * scale)}"/>'
            )
    defs, parts = [], []
    for index, (name, strand) in enumerate(reversed(record.parts)):  # the core first
        identifier = f"{occurrence}section-{index}"
        defs.append(metals.shade(identifier, name, strand.material))
        shapes = "".join(discs[id(strand)])
        if id(strand) in rings:
            inner, outer = rings[id(strand)]
            shapes += f'<path d="{circle(outer * scale)}{circle(inner * scale) if inner else ""}"/>'
        label = f"{name.capitalize()}: {wire(strand)}"
        parts.append(
            f'<g class="ol-part {metals.classes(strand.material)}" data-ol-key="{name}"'
            f' fill="url(#{identifier})"{svg.controls(interactive, label)}>'
            f"<title>{label}</title>{shapes}</g>"
        )
    body = f"<defs>{''.join(defs)}</defs>{''.join(parts)}"
    notes = ["Each wire where openline lays it, about the conductor's axis."]
    if any(isinstance(layer, Band) for layer in layers):
        notes.append(
            "Trapezoidal wires lie in as many layers as their standard counts, of equal "
            "thickness: no document gives the wires of each."
        )
    if filled:
        notes.append(
            "Wires openline cannot lay, as trapezoidal ones, fill a ring of their area: their "
            "layers are not known."
        )
        box = (-110.0, -110.0, 220.0, 220.0)
    else:
        diameter = f"Ø {record.diameter.to(mm):.4g} {symbol(mm)}"
        body += svg.dimension(XY(-RADIUS, 0), XY(RADIUS, 0), diameter, RADIUS + 14)
        box = (-110.0, -140.0, 220.0, 250.0)
    return svg.svg(
        "section",
        box,
        f"{title} cross section",
        " ".join(notes),
        body,
        interactive=interactive,
    )
