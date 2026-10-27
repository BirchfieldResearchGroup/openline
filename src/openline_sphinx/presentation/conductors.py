"""Conductors in the documentation: a standard's catalog tables, by size, and a conductor's
specification: its facts, its wires, its layers as openline lays them, its rated strength by
grade, and its figures; what openline calculates of each, a dash where it cannot yet."""

import math
from collections.abc import Sequence
from dataclasses import dataclass

from openline.mechanical import strength
from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.conductors.designations import (
    Code,
    Designation,
    Gauge,
    Kcmil,
    Mm2,
    WireGauge,
)
from openline.types.conductors.strands import Hand, Helix, Trapezoidal
from openline.types.materials import Steel
from openline.types.units import Force, aught, awg, kcmil, kn, mm, mm2, symbol

from ..figures import cutback, section
from ..quantities import QUANTITIES, calculated
from . import Block, Figure, Grid, Header, Sheet

STRENGTH = "Rated breaking strength"
RATED = calculated(strength)
HANDS = {Hand.RIGHT: "Right", Hand.LEFT: "Left", None: "—"}
VIEWS = {"Construction": cutback.cutback, "Cross section": section.section}


@dataclass(frozen=True, slots=True)
class ConductorFigure:
    """A view of a conductor: its construction cut back, or its cross section."""

    record: Conductor
    heading: str

    @property
    def dimensioned(self) -> bool:
        return False

    def svg(self, *, interactive: bool, occurrence: str) -> str:
        draw = VIEWS[self.heading]
        return draw(
            self.record, caption(self.record), interactive=interactive, occurrence=occurrence
        )


def figures(record: Conductor) -> tuple[Figure, ...]:
    """Its construction, where openline lays every ring of it, and its cross section."""
    headings = (*(("Construction",) if cutback.helical(record) else ()), "Cross section")
    return tuple(ConductorFigure(record, heading) for heading in headings)


def designation(value: Designation) -> dict[Header, str]:
    """Keep nominal sizes, conductor gauges, wire gauges and codes distinct."""
    match value:
        case Kcmil():
            return {("Nominal size", symbol(kcmil)): f"{value.kcmil:g}"}
        case Mm2():
            return {("Nominal size", symbol(mm2)): f"{value.mm2:g}"}
        case Gauge():
            return {("Conductor gauge", "AWG"): aught(value.gauge)}
        case WireGauge():
            return {("Wire gauge", "AWG"): aught(value.gauge)}
        case Code():
            return {("Code", ""): str(value.code)}
        case _:
            raise TypeError(f"Unsupported designation: {type(value).__name__}")


def size(value: Designation) -> str:
    """A designation in one cell, its unit after it: 795 kcmil, 4/0 AWG, 240 mm²; a wire gauge
    and a code as printed: No. 6, 16."""
    match value:
        case Kcmil():
            return f"{value.kcmil:g}\u202f{symbol(kcmil)}"
        case Mm2():
            return f"{value.mm2:g}\u202f{symbol(mm2)}"
        case Gauge():
            return f"{aught(value.gauge)}\u202fAWG"
        case WireGauge() | Code():
            return str(value)
        case _:
            raise TypeError(f"Unsupported designation: {type(value).__name__}")


def nominal(value: Designation) -> float:
    """A designation's size, in square meters, by which a standard's tables order its conductors:
    an AWG gauge's, its solid wire's area; a code number's, so many mm²; a gauge of wires', one
    wire's area."""
    match value:
        case Kcmil():
            return kcmil(value.kcmil).si
        case Mm2():
            return mm2(value.mm2).si
        case Gauge() | WireGauge():
            return math.pi / 4 * awg(aught(value.gauge)).si ** 2
        case Code():
            return mm2(value.code).si
        case _:
            raise TypeError(f"Unsupported designation: {type(value).__name__}")


def code_name(value: Conductor) -> str:
    return "/".join(value.code_words)


def name(value: Conductor) -> str:
    """What its row and its page are titled: its code name, or else its size."""
    return code_name(value) or size(value.designation)


def stranding(record: Conductor) -> str:
    return "/".join(str(wire.count) for wire in record.strands)


def trapezoidal(record: Conductor) -> bool:
    return any(isinstance(strand, Trapezoidal) for strand in record.strands)


def caption(record: Conductor) -> str:
    """What its page and figures are titled: its family, then its name, ``ACSR Drake``,
    ``ACSS/TW Drake``."""
    return f"{record.family}{'/TW' if trapezoidal(record) else ''} {name(record)}"


def specification(record: Conductor) -> tuple[tuple[str, str], ...]:
    """Identification and quantities, each in one labelled row."""
    rated = RATED(record)
    return (
        ("Standard", record.standard),
        *(
            (title, f"{value}\u202f{unit}" if unit else value)
            for (title, unit), value in designation(record.designation).items()
        ),
        ("Stranding", stranding(record)),
        *((quantity.label, quantity.text(record)) for quantity in QUANTITIES),
        *([(STRENGTH, f"{rated.to(kn):.4g}\u202f{symbol(kn)}")] if rated is not None else []),
    )


def parts(record: Conductor) -> tuple[tuple[str, str, str, str, str], ...]:
    """Each part's wires, outside to inside: the part, how many, their shape, diameter and
    material."""
    return tuple(
        (
            part.capitalize(),
            str(strand.count),
            type(strand).__name__,
            format(strand.diameter.to(mm), ".4g"),
            strand.material.name,
        )
        for part, strand in record.parts
    )


def layers(record: Conductor) -> Block | None:
    """Its layers from the outside in, where openline lays a ring of it to a lay: their parts,
    wires, lay and hand; the center wire last."""
    try:
        laid = record.layers[::-1]
    except Missing:
        return None
    if not any(isinstance(layer, Helix) for layer in laid):
        return None
    names = {id(strand): part for part, strand in record.parts}
    rows, keys = [], []
    for number, layer in enumerate(laid, start=1):
        owners = list(dict.fromkeys(names[id(wire)] for wire in layer.wires))
        lay = (
            [
                f"{layer.lay / (2 * layer.outer_radius):.3g}",
                f"{layer.lay.to(mm):.4g}",
                HANDS[layer.hand],
            ]
            if isinstance(layer, Helix)
            else ["—", "—", "—"]
        )
        part = ", ".join(owner.capitalize() for owner in owners)
        rows.append([str(number), part, str(len(layer.wires)), *lay])
        keys.append(owners[0])
    headers: list[Header] = [
        ("Layer", ""),
        ("Part", ""),
        ("Wires", ""),
        ("Lay ratio", ""),
        ("Lay", symbol(mm)),
        ("Hand", ""),
    ]
    return Block("Layers", headers, rows, frozenset({2, 3, 4}), tuple(keys))


def ratings(record: Conductor) -> tuple[tuple[str, str], ...]:
    """Its rated strength for each grade of core its standard names, of those whose wires'
    stresses openline has."""
    found = ((grade, _strength(record, grade)) for grade in record.grades)
    return tuple((grade.name, f"{rated.to(kn):.4g}") for grade, rated in found if rated)


def _strength(record: Conductor, grade: type[Steel]) -> Force | None:
    try:
        return strength(record, core=grade)
    except Missing:
        return None


def grids(listed: Sequence[tuple[str, Conductor]]) -> list[Grid]:
    """A standard's conductors as its tables order them, by size and then by area, more steel
    later: those known by a code word, each by its name and its size, then those known by their
    size alone, a table for each way of giving it; each with its stranding and quantities, its
    specification giving the rest."""
    sized = {
        Kcmil: f"By size in {symbol(kcmil)}",
        Mm2: f"By size in {symbol(mm2)}",
        Gauge: "By AWG gauge",
        Code: "By code number",
        WireGauge: "By wire gauge",
    }
    groups: list[tuple[str, bool, list[tuple[str, Conductor]]]] = [
        ("By code word", True, [item for item in listed if item[1].code_words]),
        *(
            (
                title,
                False,
                [i for i in listed if not i[1].code_words and type(i[1].designation) is k],
            )
            for k, title in sized.items()
        ),
    ]
    found = []
    for title, named, given_records in groups:
        records = sorted(
            given_records, key=lambda item: (nominal(item[1].designation), item[1].order)
        )
        if not records:
            continue
        given: list[Header] = [("Name", ""), ("Size", "")] if named else [("Size", "")]
        headers = [*given, ("Stranding", ""), *(quantity.header for quantity in QUANTITIES)]
        rows = [
            (
                constant,
                [
                    *([name(value)] if named else []),
                    size(value.designation),
                    stranding(value),
                    *(quantity.number(value) for quantity in QUANTITIES),
                ],
            )
            for constant, value in records
        ]
        found.append(Grid(headers, rows, frozenset(range(len(given) + 1, len(headers))), title))
    if len(found) == 1:  # one way of naming them: one table, needing no caption
        found = [found[0]._replace(title="")]
    return found


def sheet(record: Conductor) -> Sheet:
    """A conductor's specification: its facts, its parts' wires, its layers, and its ratings by
    grade."""
    given = parts(record)
    blocks = [
        Block(
            "Wires",
            [
                ("Part", ""),
                ("Wires", ""),
                ("Shape", ""),
                ("Wire diameter", symbol(mm)),
                ("Material", ""),
            ],
            [list(part) for part in given],
            frozenset({1, 3}),
            tuple(part[0].lower() for part in given),
        )
    ]
    if laid := layers(record):
        blocks.append(laid)
    if grades := ratings(record):
        blocks.append(
            Block(
                "Strength by grade",
                [("Grade", ""), (STRENGTH, symbol(kn))],
                [list(g) for g in grades],
                frozenset({1}),
                (),
            )
        )
    return Sheet(list(specification(record)), blocks)
