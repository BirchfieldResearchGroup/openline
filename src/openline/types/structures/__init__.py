"""Towers, frames, poles, and their wire attachments.

Coordinates run across the line, along it, and up from the structure datum.
``at(height)`` places attachments with the datum at ``height`` above ground."""

import math
import re
from abc import ABC

from .. import Design, Record
from ..materials import Concrete, Steel, Wood
from ..units import Angle, Length, Voltage
from .attachments import Attachment, Hold, Wire
from .geometry import Point
from .members import Beam
from .panels import Base, Body, Crossarm, Head, Leg, Part, Peak

__all__ = [
    "Datum",
    "Frame",
    "Ground",
    "LineAngle",
    "LowestCrossarm",
    "Pole",
    "PoleTop",
    "Structure",
    "Tower",
]


class Datum(Record, ABC, kw_only=False):
    """Coordinate reference and installation heights; an empty tuple leaves heights to the line."""

    heights: tuple[Length, ...]
    """The heights above the ground it is built at."""

    def __str__(self) -> str:
        what = re.sub(r"(?<!^)(?=[A-Z])", " ", type(self).__name__).lower()
        return f"{what} at {'; '.join(map(str, self.heights))}" if self.heights else what


class Ground(Datum):
    """The nominal ground level, raised by each body extension it is built with: 0 m nominal, 3 m
    for a 3 m extension."""


class LowestCrossarm(Datum):
    """The underside of its lowest crossarm."""


class PoleTop(Datum):
    """The tops of its poles."""


class LineAngle(Record, kw_only=False):
    """The smallest and largest line angle a structure takes."""

    low: Angle
    """The smallest."""
    high: Angle
    """The largest."""

    def __post_init__(self) -> None:
        if not 0 <= self.low.si <= self.high.si <= math.pi:
            raise ValueError("line angles must be ordered between 0 and 180 degrees")

    def __str__(self) -> str:
        return f"{self.low} to {self.high}"


class Structure[D: Datum](Design):
    """A structure that holds wires."""

    name: str
    """Its name as printed: D-2-D-2018.3 T1."""
    datum: D
    """What its heights are measured from, and the heights it is built at."""
    voltages: tuple[Voltage, ...]
    """The voltages it takes, between phases: 34.5, 46 and 69 kV; none where none is given."""
    line_angles: tuple[LineAngle, ...]
    """The line angles it takes; none where none is given."""
    attachments: tuple[Attachment, ...]
    """Where it holds wires, from the top down, then left to right."""

    def __post_init__(self) -> None:
        order = [(-a.point.height.si, a.point.across.si) for a in self.attachments]
        if order != sorted(order):
            raise ValueError(f"{self.name}: attachments run from the top down, then left to right")

    @property
    def names(self) -> tuple[str, ...]:
        return (self.name,)

    @property
    def title(self) -> str:
        return self.name

    @property
    def order(self) -> str:
        """Structure name, used for catalog sorting."""
        return self.name

    @property
    def parts(self) -> tuple[Part, ...]:
        """Its parts drawn as panels or bars, from its legs up; a tower's alone."""
        return ()

    @property
    def phases(self) -> tuple[Attachment, ...]:
        """Phase conductor attachments."""
        return tuple(a for a in self.attachments if a.wire is Wire.PHASE)

    @property
    def shields(self) -> tuple[Attachment, ...]:
        """Shield wire attachments."""
        return tuple(a for a in self.attachments if a.wire is Wire.SHIELD)

    @property
    def tension(self) -> bool:
        """Whether any phase attachment uses a strain string."""
        return any(a.hold is Hold.STRAIN for a in self.phases)

    def at(self, height: Length) -> tuple[Attachment, ...]:
        """Return attachments with the structure datum at ``height`` above ground."""
        return tuple(a.raised(height) for a in self.attachments)


class Tower[D: Datum](Structure[D]):
    """A lattice tower, by its parts."""

    bases: tuple[Base, ...]
    """How wide it stands on the ground, at each height it gives."""
    body: tuple[Body, ...]
    """Its body."""
    legs: tuple[Leg, ...]
    """Its legs."""
    head: tuple[Head, ...]
    """Its head, joining its body, crossarms and peaks."""
    crossarms: tuple[Crossarm, ...]
    """Its crossarms."""
    peaks: tuple[Peak, ...]
    """Its peaks, holding its shield wires."""

    @property
    def parts(self) -> tuple[Part, ...]:
        return (*self.legs, *self.body, *self.head, *self.crossarms, *self.peaks)


class Pole[M: Wood | Steel | Concrete, D: Datum](Structure[D]):
    """One pole, upright on the centerline, its crossarms holding the wires."""

    material: type[M]
    """What the pole is made of."""
    crossarms: tuple[Beam[Wood | Steel], ...]
    """Its crossarms."""


class Frame[M: Wood | Steel | Concrete, D: Datum](Structure[D]):
    """Upright poles joined by crossarms: two make an H-frame."""

    material: type[M]
    """What its poles are made of."""
    poles: tuple[Point, ...]
    """The top of each pole."""
    crossarms: tuple[Beam[Wood | Steel], ...]
    """Its crossarms."""
