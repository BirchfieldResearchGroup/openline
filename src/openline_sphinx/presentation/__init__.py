"""What a design shows in the documentation, as plain values: a module per collection,
``conductors`` and ``structures``, gives its catalog table, a design's specification and its
figures."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any, NamedTuple, Protocol

from openline.types import Design
from openline.types.units import Quantity, symbol

type Header = tuple[str, str]  # a column's title, and its unit or none


@dataclass(frozen=True, slots=True)
class Column[T, Q: Quantity[Any]]:
    """A fixed unit throughout a column, using the quantity's own conversion and symbol, and the
    condition its values hold at, where they hold at one."""

    title: str
    value: Callable[[T], Q | None]
    unit: Callable[[float], Q]
    precision: int = 4
    at: str = ""
    reported: str = ""
    """The field of a listing's report it is compared with, where one is."""

    @property
    def symbol(self) -> str:
        """Its unit's symbol: ``Ω/km``."""
        return symbol(self.unit)

    @property
    def header(self) -> Header:
        """Its title, and beneath it its unit and condition: ``Ω/km at 20 °C``."""
        return (self.title, f"{self.symbol} at {self.at}" if self.at else self.symbol)

    @property
    def label(self) -> str:
        """Its title and condition, as a fact names it: ``DC resistance at 20 °C``."""
        return f"{self.title} at {self.at}" if self.at else self.title

    def number(self, record: T) -> str:
        value = self.value(record)
        return format(value.to(self.unit), f".{self.precision}g") if value is not None else "—"

    def text(self, record: T) -> str:
        number = self.number(record)
        return f"{number}\u202f{self.symbol}" if number != "—" else number


class Grid(NamedTuple):
    """A catalog table: its headers; its rows, each the constant it lists and its cells, the
    first its name, which links it to its specification; the columns of numbers; and its caption,
    where a module's designs take more than one table."""

    headers: list[Header]
    rows: list[tuple[str, list[str]]]
    numeric: frozenset[int]
    title: str = ""


class Block(NamedTuple):
    """A table of a specification: its caption, its headers, its rows, and the columns of
    numbers."""

    title: str
    headers: list[Header]
    rows: list[list[str]]
    numeric: frozenset[int]
    keys: tuple[str, ...]


class Sheet(NamedTuple):
    """A specification: its facts, a title and a value each, the first naming what lists it;
    then its tables, in order."""

    facts: list[tuple[str, str]]
    blocks: list[Block]


class Presenter[T: Design](Protocol):
    """A collection's presentation: a module, ``conductors`` or ``structures``."""

    def grids(self, listed: Sequence[tuple[str, T]]) -> list[Grid]:
        """The catalog tables of a module's designs, each with its constant's name."""
        ...

    def sheet(self, design: T) -> Sheet:
        """A design's specification."""
        ...

    def figures(self, design: T) -> tuple[Figure, ...]:
        """The design's figures, those openline has what they take for."""
        ...


class Figure(Protocol):
    """A design's figure, drawn as one inline SVG that fits its container."""

    @property
    def heading(self) -> str: ...

    @property
    def dimensioned(self) -> bool:
        """Whether a reader may hide its dimensions."""
        ...

    def svg(self, *, interactive: bool, occurrence: str) -> str: ...


def presenter(design: Design) -> Presenter[Any]:
    """The presentation of a design's collection."""
    from openline.types.conductors import Conductor
    from openline.types.structures import Structure

    from . import conductors, structures

    if isinstance(design, Conductor):
        return conductors
    if isinstance(design, Structure):
        return structures
    raise TypeError(f"{type(design).__name__} has no presentation")
