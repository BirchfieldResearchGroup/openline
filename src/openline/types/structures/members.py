"""A structure's members: the bars of a truss, and beams."""

from abc import ABC
from enum import Enum, auto

from .. import Record
from ..materials import Material, Steel, Wood
from ..units import Length
from .geometry import Point

__all__ = ["Bar", "Beam", "Member", "Rectangle", "Role", "Truss"]


class Member(Record, ABC, kw_only=False):
    """A straight member, from ``start`` to ``end``."""

    start: Point
    """One end."""
    end: Point
    """The other end."""

    def __post_init__(self) -> None:
        if self.start.distance(self.end) == 0:
            raise ValueError(f"a member needs two ends apart: {self.start}")


class Role(Enum):
    """What a bar of a truss does."""

    CHORD = auto()
    """A main member, along an edge of the part."""
    DIAGONAL_BRACE = auto()
    """A brace across a panel, between the chords."""
    TRANSVERSE_BRACE = auto()
    """A brace straight across the part, from chord to chord."""


class Bar(Member):
    """A bar of a truss, by its role: ``Bar(Point(...), Point(...), role=Role.CHORD)``."""

    role: Role
    """What it does."""


class Rectangle(Record, kw_only=False):
    """A rectangular section: ``Rectangle(inch(5.625), inch(7.375))``."""

    width: Length
    """Its width, across the member."""
    depth: Length
    """Its depth, upright."""

    def __post_init__(self) -> None:
        if min(self.width.si, self.depth.si) <= 0:
            raise ValueError("a section's sides must be positive")


class Beam[M: Wood | Steel](Member):
    """Beams of a rectangular section side by side, upright in their depth: a crossarm."""

    material: type[M]
    """What they are made of."""
    section: Rectangle
    """Each one's section."""
    count: int
    """How many side by side: 2 for a double crossarm."""

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.count < 1:
            raise ValueError("a crossarm needs a beam")


class Truss[M: Material](Record):
    """Bars of one material, joined where their ends meet."""

    material: type[M]
    """What its bars are made of."""
    bars: tuple[Bar, ...]
    """Its bars."""

    def __post_init__(self) -> None:
        if not self.bars:
            raise ValueError("a truss needs bars")

    @property
    def joints(self) -> tuple[Point, ...]:
        """Where its bars' ends are, each once."""
        return tuple(dict.fromkeys(end for bar in self.bars for end in (bar.start, bar.end)))
