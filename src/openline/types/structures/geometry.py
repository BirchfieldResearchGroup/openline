"""Structure coordinates: across the line, along it, and up."""

import math
from dataclasses import replace
from enum import Enum, auto
from typing import Self

from .. import Record
from ..units import Length

__all__ = ["Face", "Point"]


class Face(Enum):
    """The plane of an outline of panels within the structure."""

    TRANSVERSE = auto()
    """Across the line, seen from behind the structure."""
    LONGITUDINAL = auto()
    """Along the line, seen from the side of the structure."""


class Point(Record, kw_only=False):
    """A point: ``Point(m(-12.7), m(0), m(10))``, across, along and up."""

    across: Length
    """Right of the centerline."""
    along: Length
    """Ahead along the line."""
    height: Length
    """Above the structure's datum."""

    def __post_init__(self) -> None:
        if not all(math.isfinite(value.si) for value in (self.across, self.along, self.height)):
            raise ValueError(f"a point's coordinates must be finite: {self!r}")

    def distance(self, other: "Point") -> float:
        """How far it is from ``other``, in meters."""
        return math.dist(
            (self.across.si, self.along.si, self.height.si),
            (other.across.si, other.along.si, other.height.si),
        )

    def raised(self, by: Length) -> Self:
        """The point, ``by`` higher."""
        return replace(self, height=self.height + by)

    def __str__(self) -> str:
        along = f", {self.along} along" if self.along.si else ""
        return f"{self.across} across{along}, {self.height} up"
