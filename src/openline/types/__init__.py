"""Data types for catalog designs and calculation inputs and results."""

from collections.abc import Iterator
from dataclasses import Field, dataclass, fields
from typing import Any, ClassVar, dataclass_transform

__all__ = ["Design", "Missing", "Record"]


class Missing(ValueError):
    """What a calculation takes and no document at hand gives: a standard's lay, direction of
    lay or rating factors, or a metal's constant."""


@dataclass_transform(kw_only_default=True, frozen_default=True)
class Record:
    """Base class for immutable records.

    Subclasses become frozen dataclasses with keyword-only fields unless declared with
    ``kw_only=False``. Their repr uses constructor syntax.
    """

    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]

    def __init_subclass__(cls, kw_only: bool = True, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        dataclass(frozen=True, kw_only=kw_only, repr=False)(cls)

    def __repr__(self) -> str:
        """Format fields as constructor arguments."""
        given = (
            f"{f.name}={getattr(self, f.name)!r}" if f.kw_only else repr(getattr(self, f.name))
            for f in fields(self)
        )
        return f"{type(self).__name__}({', '.join(given)})"


class Design(Record):
    """Base class for conductor and structure designs."""

    @property
    def names(self) -> tuple[str, ...]:
        """Names recognized by ``conductors.named`` and ``structures.named``."""
        raise NotImplementedError

    @property
    def title(self) -> str:
        """Single-line display name."""
        raise NotImplementedError

    @property
    def order(self) -> float | str:
        """Catalog sort key: conductor area or structure name."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Format a data sheet with a title and labeled values."""
        sheet = list(_values(self, ()))
        width = max(len(name) for name, _ in sheet)
        rows = [self.title]
        for name, value in sheet:
            for n, each in enumerate(value if isinstance(value, tuple) else (value,)):
                rows.append(f"  {name if n == 0 else '':<{width}} {each}")
        return "\n".join(rows)


def _values(record: Record, within: tuple[str, ...]) -> Iterator[tuple[str, Any]]:
    """Yield named fields, flatten records without custom formatting, and skip empty tuples and
    values none is given for."""
    for field in fields(record):
        value = getattr(record, field.name)
        place = (*within, field.name)
        if isinstance(value, Record) and type(value).__str__ is object.__str__:
            yield from _values(value, place)
        elif value != () and value is not None:
            yield ".".join(place), value
