"""Lattice tower parts represented as panel outlines or explicit bars."""

from abc import ABC
from enum import Enum, auto
from typing import Any

from .. import Record
from ..units import Length
from .geometry import Face, Point
from .members import Truss

__all__ = [
    "Base",
    "Body",
    "Bracing",
    "Crossarm",
    "Edge",
    "Head",
    "Leg",
    "Panel",
    "PanelRun",
    "Part",
    "Peak",
]


class Bracing(Enum):
    """The pattern between a panel's chords."""

    CROSS = auto()
    """Two diagonals crossing in each bay, and a strut at each end."""
    WARREN = auto()
    """One diagonal in each bay, turning the other way in the next."""
    PRATT = auto()
    """One diagonal in each bay, and a strut at each end."""
    DIAMOND = auto()
    """A diamond in each bay, its corners at the middles of the bay's sides."""
    OPEN = auto()
    """Nothing between the chords."""


class Edge(Record, kw_only=False):
    """The two ends of a panel's boundary: ``Edge(start, end)``."""

    start: Point
    """The first chord's end."""
    end: Point
    """The second chord's end."""


class Panel(Record, kw_only=False):
    """A panel up or out from the edge before it: ``Panel(edge, Bracing.CROSS, 3)``."""

    edge: Edge
    """The ends of its chords at its far boundary."""
    bracing: Bracing
    """The pattern between its chords."""
    bays: int
    """How many times the pattern repeats."""

    def __post_init__(self) -> None:
        if self.bays < 1:
            raise ValueError("a panel needs a bay or more")


class PanelRun(Record):
    """An outline of panels in one plane, each bay of a panel braced alike. A crossing of braces
    makes no joint."""

    face: Face
    """The plane it lies in."""
    start: Edge
    """The first panel's near boundary."""
    panels: tuple[Panel, ...]
    """Its panels, in order up or out from the first boundary."""

    def __post_init__(self) -> None:
        if not self.panels:
            raise ValueError("an outline needs panels")


class Part(Record, ABC):
    """A part of a tower, as its drawing gives it."""

    construction: PanelRun | Truss[Any]
    """Its outline of panels, or its bars."""


class Body(Part):
    """The tower's body, which carries its load to its legs."""


class Leg(Part):
    """A leg, from a footing up to the body."""


class Head(Part):
    """A part of the head, which joins the body, crossarms and peaks."""


class Crossarm(Part):
    """A crossarm, holding wires out from the body or between its sides."""


class Peak(Part):
    """A peak, holding a shield wire."""


class Base(Record, kw_only=False):
    """How wide a tower stands on the ground, square over its heels, built with its datum at
    ``height``."""

    height: Length
    """The datum's height above the ground."""
    width: Length
    """The width."""

    def __str__(self) -> str:
        return f"{self.width} at {self.height}"
