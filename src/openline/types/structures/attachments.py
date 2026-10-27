"""Wire attachment points, support arrangements, and insulator strings."""

from abc import ABC
from dataclasses import replace
from enum import Enum, auto
from typing import Self

from .. import Record
from ..units import Length
from .geometry import Point

__all__ = [
    "Attachment",
    "DiscString",
    "Hold",
    "InsulatorString",
    "Mount",
    "Wire",
    "WirePosition",
]


class Wire(Enum):
    """Wire role: phase conductor or shield wire."""

    PHASE = auto()
    """A phase conductor."""
    SHIELD = auto()
    """A grounded shield wire, above the phases."""

    def __str__(self) -> str:
        return self.name.lower()


class Hold(Enum):
    """How a structure holds a wire at a point."""

    CLAMP = auto()
    """In a clamp at the point."""
    SUSPENSION = auto()
    """Hanging from an insulator string below the point."""
    V_STRING = auto()
    """Hanging where two insulator strings meet, below the point."""
    STRAIN = auto()
    """In line with the wire: an insulator string takes its pull."""
    POST = auto()
    """On a post insulator."""
    PIN = auto()
    """On a pin insulator."""

    def __str__(self) -> str:
        return self.name.lower().replace("_", "-")


class InsulatorString(Record):
    """An insulator string, from its mount on the structure to the wire."""

    mount: Point
    """Where it is mounted on the structure."""

    def raised(self, by: Length) -> Self:
        """The string, ``by`` higher."""
        return replace(self, mount=self.mount.raised(by))


class DiscString(InsulatorString):
    """A string of discs, as its drawing gives them."""

    discs: int
    """How many discs."""
    diameter: Length
    """The discs' diameter."""
    length: Length
    """The length the discs take up along the string."""

    def __post_init__(self) -> None:
        if self.discs < 1 or self.diameter.si <= 0 or self.length.si <= 0:
            raise ValueError("a disc string needs discs, of a size, over a length")


class Attachment(Record, ABC, kw_only=False):
    """A wire attachment point, role, and support arrangement."""

    wire: Wire
    """What the wire is for."""
    point: Point
    """Where its drawing gives it: on the structure for a mount, the wire itself for a wire
    position."""
    hold: Hold
    """How it is held."""

    def __str__(self) -> str:
        return f"{self.wire}, {self.hold}, {self.point}"

    def raised(self, by: Length) -> Self:
        """The attachment, ``by`` higher."""
        return replace(self, point=self.point.raised(by))


class Mount(Attachment):
    """Held at a point of the structure: where its clamp is, or where its insulators hang from
    or pull on."""


class WirePosition(Attachment):
    """Wire location and insulator strings connecting it to the structure."""

    strings: tuple[InsulatorString, ...]
    """Its insulator strings: one, or a V-string's two."""

    def __post_init__(self) -> None:
        """Its strings, as many as its hold takes, from mounts apart, each away from the wire and
        no shorter than its discs."""
        if self.hold is Hold.CLAMP:
            raise ValueError("a wire clamped at a point is held at a mount")
        count, needed = (2, "two strings") if self.hold is Hold.V_STRING else (1, "one string")
        if len(self.strings) != count or len({s.mount for s in self.strings}) != count:
            raise ValueError(f"a {self.hold} position needs {needed}, from mounts apart")
        for string in self.strings:
            span = string.mount.distance(self.point)
            if span <= 0 or (isinstance(string, DiscString) and string.length.si > span):
                raise ValueError("a string's discs must fit between its mount and the wire")

    def raised(self, by: Length) -> Self:
        return replace(
            self,
            point=self.point.raised(by),
            strings=tuple(string.raised(by) for string in self.strings),
        )
