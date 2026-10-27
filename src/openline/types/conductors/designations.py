"""How standards name conductors: by a size in kcmil, AWG or mm², by the gauge of each wire, by a
code number, or by the sizes of aluminum and steel. A designation is given in order:
``Kcmil(795)``."""

import re
from abc import ABC, abstractmethod
from dataclasses import fields
from decimal import ROUND_HALF_UP, Decimal
from typing import ClassVar, Self

from .. import Record
from ..units import aught, gauge_number, kcmil, mm2, symbol

__all__ = ["Code", "Designation", "Gauge", "Kcmil", "Mm2", "WireGauge"]


class Designation(Record, ABC):
    """How a standard names a conductor."""

    metric: ClassVar[bool]
    """Whether it sizes the conductor in SI units, so that the metric tables of its wires'
    standards govern it."""

    @classmethod
    @abstractmethod
    def parse(cls, text: str) -> Self:
        """The designation written as ``text``."""

    @abstractmethod
    def __str__(self) -> str:
        """The designation as written."""

    def written_as(self, text: str) -> bool:
        """Whether ``text`` writes this designation, each of its numbers perhaps rounded half up
        to the decimals ``text`` gives it: ``Kcmil(30.58)`` is written ``30.6 kcmil``;
        ``Kcmil(795)`` is not ``800 kcmil``."""
        try:
            given = type(self).parse(text)
        except ValueError:
            return False
        tokens: list[str] = re.findall(r"\d+(?:\.\d+)?", text)
        for field in fields(self):
            ours, theirs = getattr(self, field.name), getattr(given, field.name)
            if not isinstance(ours, float):
                if ours != theirs:
                    return False
                continue
            token = next((each for each in tokens if float(each) == theirs), repr(theirs))
            step = Decimal(1).scaleb(-len(token.partition(".")[2]))
            if Decimal(repr(ours)).quantize(step, ROUND_HALF_UP) != Decimal(token):
                return False
        return True


def _size(text: str, unit: str) -> float:
    """The number of a size written in ``unit``, by its symbol: 795 of ``"795.0 kcmil"``."""
    number, _, given = text.partition(" ")
    if given != unit:
        raise ValueError(f"not in {unit}: {text!r}")
    return float(number)


class Kcmil(Designation, kw_only=False):
    """A size in thousands of circular mils: 795 kcmil."""

    metric = False

    kcmil: float
    """The size: 266.8."""

    @classmethod
    def parse(cls, text: str) -> Self:
        return cls(_size(text, symbol(kcmil)))

    def __str__(self) -> str:
        return f"{self.kcmil:g} {symbol(kcmil)}"


class Mm2(Designation, kw_only=False):
    """A nominal size in square millimeters: 240 mm²."""

    metric = True

    mm2: float
    """The size: 37.7."""

    @classmethod
    def parse(cls, text: str) -> Self:
        return cls(_size(text, symbol(mm2)))

    def __str__(self) -> str:
        return f"{self.mm2:g} {symbol(mm2)}"


class Gauge(Designation, kw_only=False):
    """The AWG gauge of the conductor: 4/0 AWG."""

    metric = False

    gauge: int
    """The gauge; 1/0 to 4/0 are 0 to -3."""

    @classmethod
    def parse(cls, text: str) -> Self:
        number, _, unit = text.partition(" ")
        if unit != "AWG":
            raise ValueError(f"not an AWG gauge: {text!r}")
        return cls(gauge_number(number))

    def __str__(self) -> str:
        return f"{aught(self.gauge)} AWG"


class WireGauge(Designation, kw_only=False):
    """The AWG gauge of each wire: No. 6."""

    metric = False

    gauge: int
    """The gauge; 1/0 to 4/0 are 0 to -3."""

    @classmethod
    def parse(cls, text: str) -> Self:
        if not text.startswith("No. "):
            raise ValueError(f"not a gauge of wires: {text!r}")
        return cls(gauge_number(text.removeprefix("No. ")))

    def __str__(self) -> str:
        return f"No. {aught(self.gauge)}"


class Code(Designation, kw_only=False):
    """A code number: 250."""

    metric = True

    code: int
    """The code."""

    @classmethod
    def parse(cls, text: str) -> Self:
        return cls(int(text))

    def __str__(self) -> str:
        return str(self.code)
