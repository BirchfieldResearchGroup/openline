"""Structures in the documentation: a family's catalog table, by name, and a structure's
specification: where it holds its wires, the parts its family has, and its elevations."""

import re
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from openline.types.structures import Datum, Frame, Pole, Structure, Tower
from openline.types.structures.attachments import Mount, WirePosition
from openline.types.structures.geometry import Point
from openline.types.structures.members import Beam, Rectangle, Truss
from openline.types.structures.panels import Part
from openline.types.units import Length, degrees, kv, m, mm, symbol

from ..figures import elevation
from . import Block, Figure, Grid, Header, Sheet


@dataclass(frozen=True, slots=True)
class StructureFigure:
    """A structure's elevations, drawn from its catalog parts and points."""

    record: Structure[Any]

    @property
    def heading(self) -> str:
        """A tower's whole elevation; of a frame or pole, what stands above the ground, whose
        depth in it the line sets."""
        return "Elevation" if isinstance(self.record, Tower) else "Upper structure"

    @property
    def dimensioned(self) -> bool:
        return elevation.plan(self.record).dimensioned

    def svg(self, *, interactive: bool, occurrence: str) -> str:
        return elevation.draw(
            elevation.plan(self.record), interactive=interactive, occurrence=occurrence
        )


def figures(record: Structure[Any]) -> tuple[Figure, ...]:
    """Its elevations, where its parts or points draw one."""
    return (StructureFigure(record),) if elevation.plan(record).views else ()


def meters(length: Length) -> str:
    return format(length.to(m), ".4g")


def millimeters(length: Length) -> str:
    return format(length.to(mm), ".4g")


def datum(given: Datum) -> str:
    """What a datum is, from its class: ``Lowest crossarm``."""
    return re.sub(r"(?<!^)(?=[A-Z])", " ", type(given).__name__).capitalize()


def heights(given: Datum) -> str:
    return ", ".join(meters(height) for height in given.heights) or "—"


def voltages(structure: Structure[Any]) -> str:
    return ", ".join(format(v.to(kv), "g") for v in structure.voltages) or "—"


def holds(structure: Structure[Any]) -> str:
    return ", ".join(dict.fromkeys(str(a.hold) for a in structure.phases)) or "—"


def material(structure: Structure[Any]) -> str:
    """What a frame's or pole's poles are made of; a tower names none."""
    return structure.material.name if isinstance(structure, Frame | Pole) else "—"


def grids(listed: Sequence[tuple[str, Structure[Any]]]) -> list[Grid]:
    """A family's structures by name: what its poles are made of, where it has poles; its
    voltages, datum and heights; and how many wires it holds, and how."""
    records = sorted(listed, key=lambda item: item[1].name)
    poled = any(isinstance(value, Frame | Pole) for _, value in records)
    headers: list[Header] = [
        ("Name", ""),
        *([("Material", "")] if poled else []),
        ("Voltages", symbol(kv)),
        ("Datum", ""),
        ("Heights", symbol(m)),
        ("Phase points", ""),
        ("Shield points", ""),
        ("Holds", ""),
    ]
    rows = [
        (
            name,
            [
                value.name,
                *([material(value)] if poled else []),
                voltages(value),
                datum(value.datum),
                heights(value.datum),
                str(len(value.phases)) if value.attachments else "\u2014",
                str(len(value.shields)) if value.attachments else "\u2014",
                holds(value),
            ],
        )
        for name, value in records
    ]
    shift = int(poled)
    return [Grid(headers, rows, frozenset({1 + shift, 4 + shift, 5 + shift}))]


def point(at: Point) -> list[str]:
    return [meters(at.across), meters(at.along), meters(at.height)]


def section(given: Rectangle) -> str:
    """A section's sides, in millimetres."""
    return f"{millimeters(given.width)} \u00d7 {millimeters(given.depth)}"


def crossarms(given: Sequence[Beam[Any]]) -> Block:
    """A frame's or pole's crossarms: what each is made of, its ends, its section and how many
    beams it has."""
    headers: list[Header] = [
        ("Material", ""),
        ("Start", symbol(m)),
        ("End", symbol(m)),
        ("Section", symbol(mm)),
        ("Count", ""),
    ]
    rows = [
        [
            arm.material.name,
            ", ".join(point(arm.start)),
            ", ".join(point(arm.end)),
            section(arm.section),
            str(arm.count),
        ]
        for arm in given
    ]
    return Block("Crossarms", headers, rows, frozenset({4}), ())


def bars(given: tuple[Part, ...]) -> Block | None:
    """A tower's parts drawn as bars: each part's bars by their role."""
    rows: list[list[str]] = []
    for i, part in enumerate(given, start=1):
        if not isinstance(part.construction, Truss):
            continue
        roles = Counter(bar.role for bar in part.construction.bars)
        rows.extend(
            [
                f"{type(part).__name__} {i}",
                part.construction.material.name,
                role.name.lower().replace("_", " "),
                str(count),
            ]
            for role, count in roles.items()
        )
    if not rows:
        return None
    headers: list[Header] = [("Part", ""), ("Material", ""), ("Role", ""), ("Bars", "")]
    return Block("Bars", headers, rows, frozenset({3}), ())


def sheet(structure: Structure[Any]) -> Sheet:
    """A structure's specification: its facts, where it holds its wires, and its family's
    parts, where its drawing gives them."""
    facts = [
        ("Family", type(structure).__name__),
        *([("Material", material(structure))] if isinstance(structure, Frame | Pole) else []),
        ("Datum", datum(structure.datum)),
        *(
            [("Heights", f"{heights(structure.datum)}\u202f{symbol(m)}")]
            if structure.datum.heights
            else []
        ),
        *([("Voltages", f"{voltages(structure)}\u202f{symbol(kv)}")] if structure.voltages else []),
        *(
            ("Line angles", f"{a.low.to(degrees):g} to {a.high.to(degrees):g}{symbol(degrees)}")
            for a in structure.line_angles
        ),
        *(
            (f"Base at {meters(b.height)}\u202f{symbol(m)}", f"{meters(b.width)}\u202f{symbol(m)}")
            for b in (structure.bases if isinstance(structure, Tower) else ())
        ),
    ]
    places: list[Header] = [("Across", symbol(m)), ("Along", symbol(m)), ("Height", symbol(m))]
    blocks: list[Block] = []
    drawing = elevation.plan(structure)
    if isinstance(structure, Tower) and drawing.views:
        blocks.append(
            Block(
                "Outline",
                [("View", ""), ("Width", symbol(m)), ("Height", symbol(m))],
                [
                    [
                        view.name,
                        f"{view.bounds.width:.4g}",
                        f"{view.bounds.height:.4g}",
                    ]
                    for view in drawing.views
                ],
                frozenset({1, 2}),
                (),
            )
        )
    for cls, title in {Mount: "Mounts", WirePosition: "Wire positions"}.items():
        listed = [(i, a) for i, a in enumerate(structure.attachments) if isinstance(a, cls)]
        if listed:
            blocks.append(
                Block(
                    title,
                    [("Wire", ""), ("Hold", ""), *places],
                    [[str(a.wire), str(a.hold), *point(a.point)] for _, a in listed],
                    frozenset({2, 3, 4}),
                    tuple(str(i) for i, _ in listed),
                )
            )
    if isinstance(structure, Frame) and structure.poles:
        blocks.append(
            Block(
                "Pole tops",
                [("Pole", ""), *places],
                [[str(n), *point(top)] for n, top in enumerate(structure.poles, start=1)],
                frozenset({1, 2, 3}),
                (),
            )
        )
    if isinstance(structure, Frame | Pole) and structure.crossarms:
        blocks.append(crossarms(structure.crossarms))
    if block := bars(structure.parts):
        blocks.append(block)
    return Sheet(facts, blocks)
