"""Reference tables of the API: every material by its properties, those it inherits dimmed;
every unit openline reads under the SI unit it measures in; and every standard the catalog lists
conductors to. What a table does not hold follows, or precedes, as the API documents it."""

import re
import typing
from collections.abc import Callable, Iterator, Sequence
from inspect import isclass, isfunction, signature
from typing import Any, NamedTuple

from docutils import nodes

from openline import _designs
from openline.types import Missing, materials, units
from openline.types.conductors import ASTM, BS, CSA, IEC, Conductor
from openline.types.materials import ByDiameter, Material, Metal
from openline.types.units import (
    OhmMeter,
    OhmMeterPerKelvin,
    Quantity,
    Unit,
    gpa,
    j_per_kg_k,
    kg_per_m3,
    mpa,
    symbol,
)

from . import depends
from .api import TableDirective, documented, parsed, public, shown
from .presentation import Header
from .tables import Cell, Row, link, note, table

SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


class Property(NamedTuple):
    """A column of the materials' table: the class variable it shows, its header, and its value
    as a number in the header's unit."""

    name: str
    header: Header
    shown: Callable[[Any], str]


def strengths(given: ByDiameter) -> str:
    """The least and the most stress a wire table rates, in whole MPa, a dash between."""
    stresses = [round(stress.to(mpa)) for _, _, stress in given.metric or given.inch_pound]
    low, high = min(stresses), max(stresses)
    return str(low) if low == high else f"{low}\u2013{high}"


GROUPS: tuple[tuple[str, tuple[Property, ...]], ...] = (
    (
        "Electrical",
        (
            Property(
                "resistivity",
                ("Resistivity at 20\u202f°C", f"n{OhmMeter.symbol}"),
                lambda v: f"{v.si * 1e9:.4g}",
            ),
            Property(
                "resistivity_rise",
                ("Rise", f"n{OhmMeterPerKelvin.symbol}"),
                lambda v: f"{v.si * 1e9:.4g}",
            ),
            Property("relative_permeability", ("Permeability", "relative"), lambda v: f"{v:.7g}"),
        ),
    ),
    (
        "Thermal",
        (
            Property(
                "specific_heat",
                ("Specific heat", symbol(j_per_kg_k)),
                lambda v: f"{v.to(j_per_kg_k):.4g}",
            ),
            Property("expansion", ("Expansion", "10⁻⁶/K"), lambda v: f"{v.si * 1e6:.4g}"),
        ),
    ),
    (
        "Mechanical",
        (
            Property("density", ("Density", symbol(kg_per_m3)), lambda v: f"{v.to(kg_per_m3):.4g}"),
            Property("modulus", ("Modulus", symbol(gpa)), lambda v: f"{v.to(gpa):.4g}"),
            Property("tensile_strength", ("Tensile strength", symbol(mpa)), strengths),
            Property("extension_stress", ("At 1% extension", symbol(mpa)), strengths),
        ),
    ),
)
PROPERTIES = tuple(given for _, group in GROUPS for given in group)


class Materials(TableDirective):
    """Every material, a row each beneath the one it derives from: a metal's properties, those
    it inherits dimmed and named for the class they come from; then ``Material``, ``Metal`` and
    ``ByDiameter``."""

    def run(self) -> list[nodes.Node]:
        depends.note(self.env)
        rows: list[Row] = []
        for top in Material.__subclasses__():
            for cls, depth in tree(top.__subclasses__() if top is Metal else [top]):
                classes = (f"depth-{depth}", *(("family",) if depth == 1 else ()))
                cells: list[Cell] = [self.material(cls)]
                if issubclass(cls, Metal):
                    cells += [self.value(cls, given) for given in PROPERTIES]
                else:
                    cells.append(nodes.inline(text="No properties", classes=["none"]))
                rows.append(Row(cells, classes))
        headers = [("Material", ""), *(given.header for given in PROPERTIES)]
        tabulated = {cls for cls, _ in tree(Material.__subclasses__())} - {Metal}
        return [
            table(
                headers,
                rows,
                numeric=set(range(1, len(headers))),
                groups=[(title, len(group)) for title, group in GROUPS],
            ),
            note(
                "Dimmed: inherited, from the class its hover names. Strengths: the least to the "
                "most its wire standard rates, over the diameters it tabulates."
            ),
            *parsed(
                self, documented(materials, [v for v in public(materials) if v not in tabulated])
            ),
        ]

    def material(self, cls: type[Material]) -> nodes.inline:
        """A material's class, the target of links to it, and beneath it the name documents give
        it, where that says more than the class's: ``Carbon fiber composite``."""
        result = nodes.inline("", "", self.named(cls, "class", cls.__name__))
        if re.sub(r"\W", "", cls.name).casefold() != cls.__name__.casefold():
            result += nodes.inline(text=cls.name, classes=["also"])
        return result

    def value(self, cls: type[Metal], given: Property) -> Cell:
        """A metal's property: dimmed where it inherits it; a dash where no document gives it."""
        try:
            found = getattr(cls, given.name)
        except (Missing, AttributeError):
            return "—"
        text = given.shown(found)
        if given.name in vars(cls):
            return text
        owner = next(each for each in cls.__mro__ if given.name in vars(each))
        return nodes.abbreviation(
            "", text, explanation=f"From {owner.__name__}", classes=["inherited"]
        )


def tree(roots: Sequence[type[Material]], depth: int = 1) -> Iterator[tuple[type[Material], int]]:
    """Each class and those derived from it, in the order they are written, by their depth."""
    for cls in roots:
        yield cls, depth
        yield from tree(cls.__subclasses__(), depth + 1)


class Units(TableDirective):
    """Every unit openline reads, under the SI unit it measures in and each quantity measured in
    it: its function, its symbol, one of it in SI, and its name; then what the table does not
    hold."""

    def run(self) -> list[nodes.Node]:
        depends.note(self.env)
        quantities = [
            value
            for value in vars(units).values()
            if isclass(value) and issubclass(value, Quantity) and value is not Quantity
        ]
        measured: dict[type[Unit], list[type[Quantity[Any]]]] = {}
        for quantity in quantities:
            measured.setdefault(unit_of(quantity), []).append(quantity)
        readers = [value for value in public(units) if isfunction(value) and reads(value)]
        rows: list[Row | list[Cell]] = []
        for unit, kinds in measured.items():
            rows.append(Row([self.measured(unit, kinds)], ("group",)))
            for function in readers:
                if unit_of(typing.get_type_hints(function)["return"]) is unit:
                    known = function in units.SYMBOLS.values()
                    rows.append(
                        [
                            self.named(function, "function", call(function)),
                            nodes.literal(text=symbol(function)) if known else "",
                            scale(function),
                            self.inline(" ".join((function.__doc__ or "").split()).rstrip(".")),
                        ]
                    )
        headers = [("Function", ""), ("Symbol", ""), ("One is", "in SI"), ("Name", "")]
        tabulated = {*quantities, *measured, *readers}
        rest = [value for value in public(units) if value not in tabulated]
        return [
            table(headers, rows, numeric={2}),
            note(
                "Symbol: as openline prints the unit and its sources write it, its key in SYMBOLS. "
                "One is: one of the unit, in the SI unit above it."
            ),
            *parsed(self, documented(units, rest)),
        ]

    def measured(self, unit: type[Unit], kinds: list[type[Quantity[Any]]]) -> nodes.inline:
        """An SI unit's heading: its symbol, the target of links to its class, and each
        quantity measured in it, with what it is."""
        result = nodes.inline(
            "", "", self.declare(unit, "class"), nodes.inline(text=unit.symbol, classes=["symbol"])
        )
        for kind in kinds:
            line = nodes.inline(classes=["line"])
            line += self.named(kind, "class", kind.__name__)
            line += nodes.Text(" ")
            line += self.inline(" ".join((kind.__doc__ or "").split()))
            result += line
        return result


def unit_of(quantity: type[Quantity[Any]]) -> type[Unit]:
    """The SI unit a quantity measures in: ``Meter`` of ``Length``."""
    (unit,) = typing.get_args(quantity.__orig_bases__[0])  # type: ignore[attr-defined]
    return typing.cast(type[Unit], unit)


def reads(function: Callable[..., Any]) -> bool:
    """Whether a function reads a quantity from numbers or text as printed: a unit."""
    hints = typing.get_type_hints(function)
    returned = hints.pop("return", None)
    return (
        isclass(returned)
        and issubclass(returned, Quantity)
        and all(hint in (float, str) for hint in hints.values())
    )


def call(function: Callable[..., Any]) -> str:
    """How a unit is called: ``mm``; ``ft_in(feet, inches)`` where it takes more than a number."""
    names = list(signature(function).parameters)
    single = len(names) == 1 and typing.get_type_hints(function)[names[0]] is float
    return function.__name__ if single else f"{function.__name__}({', '.join(names)})"


def scale(function: Callable[..., Any]) -> str:
    """One of a unit in SI: ``0.0254``; ``x + 273.15`` where it starts from other than zero; a
    dash for one that takes more than a number."""
    if call(function) != function.__name__:
        return "—"
    zero = function(0).si
    one = function(1).si - zero
    return f"x + {number(zero)}" if zero else number(one)


def number(value: float) -> str:
    """A number to seven figures, written as a power of ten below a thousandth or from a
    million: ``6.213712 \u00d7 10\u207b\u2074``."""
    if not value or 1e-3 <= abs(value) < 1e6:
        return f"{value:.7g}"
    mantissa, _, exponent = f"{value:.6e}".partition("e")
    mantissa = mantissa.rstrip("0").rstrip(".")
    power = f"10{str(int(exponent)).translate(SUPERSCRIPT)}"
    return power if mantissa == "1" else f"{mantissa}\u202f\u00d7\u202f{power}"


BODIES = (ASTM, BS, CSA, IEC)  # who writes a standard: a conductor class derives from one


class Standards(TableDirective):
    """Every standard the catalog lists conductors to, under the body that writes it: its
    family, how it designates them, their wires, what it gives of their lay and rating, and how
    many the catalog lists; each linked to its class, documented below, and its catalog table."""

    def run(self) -> list[nodes.Node]:
        depends.note(self.env)
        written: dict[type[Conductor], list[tuple[str, list[Conductor]]]] = {}
        for module in _designs.modules("conductors"):
            given = _designs.designs(module).values()
            listed = sorted((d for d in given if isinstance(d, Conductor)), key=lambda d: d.order)
            body = next(each for each in BODIES if isinstance(listed[0], each))
            written.setdefault(body, []).append((module, listed))
        rows: list[Row | list[Cell]] = []
        for body in BODIES:
            rows.append(Row([nodes.inline("", "", *shown(body), classes=["symbol"])], ("group",)))
            standards = sorted(written.get(body, []), key=lambda each: type(each[1][0]).standard)
            rows.extend(self.standard(module, listed) for module, listed in standards)
        headers = [
            ("Standard", ""),
            ("Family", ""),
            ("Designated as", ""),
            ("Wires", ""),
            ("Lay", ""),
            ("Core grades", ""),
            ("Strandings", ""),
            ("Conductors", ""),
        ]
        groups = [("Construction", 3), ("What the standard gives", 3), ("Catalog", 1)]
        return [table(headers, rows, numeric={6, 7}, groups=groups)]

    def standard(self, module: str, listed: list[Conductor]) -> list[Cell]:
        """A standard's row: its name and class, and what its conductors are."""
        cls = type(listed[0])
        kinds = dict.fromkeys(type(design.designation) for design in listed)
        examples = [
            str(next(d.designation for d in listed if type(d.designation) is k)) for k in kinds
        ]
        names = [strand.material.name for _, strand in listed[0].parts]
        wires = " around ".join([names[0], *(name[0].lower() + name[1:] for name in names[1:])])
        grades = ", ".join(grade.name.split()[-1] for grade in cls.grades)
        hand = cls.hand.name.capitalize() if cls.hand is not None else "\u2014"
        return [
            nodes.inline(
                "",
                "",
                nodes.Text(cls.standard),
                nodes.inline("", "", *shown(cls), classes=["also"]),
            ),
            cls.family,
            ", ".join(examples),
            wires,
            hand,
            grades or "\u2014",
            str(len(cls.strandings)) if cls.strandings else "\u2014",
            link(str(len(listed)), module, self.env.docname),
        ]
