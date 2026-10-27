"""Wire positions along a span, including bundle spacing, insulator drop, and sag."""

import math
from typing import NamedTuple

from ..mechanical import sag
from ..types.conductors import Conductor
from ..types.lines import Bundle, Line, Placed, Strung, Suspended
from ..types.structures.attachments import Attachment
from ..types.structures.geometry import Point
from ..types.units import Temperature, m
from . import _span

__all__ = ["Hanging", "groups", "hanging", "images", "mean_positions", "placed"]


class Hanging(NamedTuple):
    """A wire of a line."""

    conductor: Conductor
    """What it is strung with."""
    strung: Strung
    """How it is strung."""
    across: float
    """Where it is held, across the line, in meters."""
    height: float
    """How high above the earth it is held, in meters."""
    phase: int
    """The phase it is of, circuit by circuit from zero; a shield wire, none: -1."""


def hanging(line: Line, temperature: Temperature) -> list[Hanging]:
    """Return phase conductors followed by shield wires, with attachment and stringing data.

    Apply insulator drop for suspended phases. Raise ``ValueError`` if a wire reaches ground
    at the specified temperature."""
    found: list[Hanging] = []
    phase = 0
    for circuit in line.circuits:
        for each in circuit.phases:
            given = each.conductor
            conductor = given.conductor if isinstance(given, Bundle) else given
            across, height = _held(line, each.attachments)
            if isinstance(each, Suspended):
                height -= each.drop.si
            for x, y in _bundled(across, height, given):
                found.append(Hanging(conductor, each.strung, x, y, phase))
            phase += 1
    for shield in line.shields:
        across, height = _held(line, (shield.attachment,))
        found.append(Hanging(shield.conductor, shield.strung, across, height, -1))
    for wire in found:
        low = placed(line, wire, temperature, 0.5)
        if low.point.height <= low.radius:
            raise ValueError(f"a wire of {line.structure.name}'s line sags to the earth")
    return found


def groups(wires: list[Hanging]) -> list[list[int]]:
    """Return wire indices for each phase."""
    phases = max((wire.phase for wire in wires), default=-1) + 1
    return [[i for i, wire in enumerate(wires) if wire.phase == phase] for phase in range(phases)]


def placed(line: Line, wire: Hanging, temperature: Temperature, at: float) -> Placed:
    """Place a wire at fraction ``at`` along the span, accounting for sag at ``temperature``."""
    drop = sag(wire.conductor, span=line.span, strung=wire.strung, temperature=temperature, at=at)
    point = Point(m(wire.across), m(0), m(wire.height) - drop)
    return Placed(wire.conductor.diameter / 2, point)


def mean_positions(line: Line, wires: list[Hanging], temperature: Temperature) -> list[Placed]:
    r"""Place each wire at its mean height along the catenary, :math:`\bar h = \int_0^1 h(u)\,du`.

    Series impedance and shunt admittance use this same uniform geometry. Averaging their
    electrical matrices separately can disturb the balance of earth-return losses."""
    heights = _span.mean(
        lambda at: [placed(line, wire, temperature, at).point.height.si for wire in wires]
    )
    return [
        Placed(wire.conductor.diameter / 2, Point(m(wire.across), m(0), m(height.real)))
        for wire, height in zip(wires, heights, strict=True)
    ]


def images(a: Placed, b: Placed) -> tuple[float, float]:
    """Return wire-to-wire and wire-to-image distances in meters.

    For self-terms, use the wire radius and twice its height."""
    if a == b:
        return a.radius.si, 2 * a.point.height.si
    apart = abs(a.point.across.si - b.point.across.si)
    near = math.hypot(apart, a.point.height.si - b.point.height.si)
    return near, math.hypot(apart, a.point.height.si + b.point.height.si)


def _held(line: Line, attachments: tuple[Attachment, ...]) -> tuple[float, float]:
    """Return the attachment midpoint as horizontal position and height in meters."""
    points = [a.point for a in attachments]
    across = sum(p.across.si for p in points) / len(points)
    height = sum(p.height.si for p in points) / len(points)
    return across, line.height.si + height


def _bundled(across: float, height: float, given: Conductor | Bundle) -> list[tuple[float, float]]:
    """Place a single conductor at the support point or bundle conductors around it."""
    if not isinstance(given, Bundle) or given.count == 1:
        return [(across, height)]
    radius = given.spacing.si / (2 * math.sin(math.pi / given.count))
    turns = (2 * math.pi * k / given.count for k in range(given.count))
    return [(across + radius * math.cos(t), height + radius * math.sin(t)) for t in turns]
