"""Each listing: a row of a document's table, the catalog design it names, and what it gives of
it, its construction, which must be the catalog's, and what it reports, at the conditions its
document states. The validation compares both with the model; ``openline`` holds no reported
values.

Inductive and capacitive reactances at a document's spacing are not read: they follow from the
GMR and the diameter, which are compared."""

import csv
import re
from collections.abc import Iterable, Iterator
from importlib import import_module
from typing import Any, NamedTuple

from openline import _designs
from openline.types import materials
from openline.types.conductors import Conductor, Surface
from openline.types.conductors.designations import Code, Designation, Gauge, Kcmil, Mm2, WireGauge
from openline.types.environment import Atmosphere, Environment, Sun
from openline.types.materials import Steel
from openline.types.units import (
    SYMBOLS,
    Area,
    Current,
    Force,
    Frequency,
    Length,
    MassPerLength,
    Quantity,
    ResistancePerLength,
    Temperature,
    amperes,
    awg,
    celsius,
    equivalent,
    hz,
)

from .provenance import Document

LISTING = ("locator", "design", "code_word", "designation", "classes")
COLUMN = re.compile(r"reported\.(?P<field>[\w°]+(?:\.[\w°]+)*)\[(?P<unit>[^\]]+)\]")
WIRES = re.compile(
    r"(?P<part>[a-z]+)\.(?P<field>count|layers|diameter|area|outside_diameter)"
    r"(?:\[(?P<unit>[^\]]+)\])?"
)
AC = re.compile(r"ac_resistances\.(?P<frequency>\d+)Hz\.(?P<temperature>\d+)°C")
AMPACITY = re.compile(r"ampacity\.(?P<surface>\w+)\.(?P<temperature>\d+)°C")
SCALARS = ("area", "diameter", "mass", "dc_resistance", "outer_dc_resistance", "gmr")
UNREAD = ("inductive_reactance", "capacitive_reactance")
KEY = re.compile(r"(?P<name>\w+)\[(?P<unit>[^\]]+)\]")


class ACResistance(NamedTuple):
    """An AC resistance as reported, at a temperature and frequency."""

    temperature: Temperature
    frequency: Frequency
    resistance: ResistancePerLength


class Rating(NamedTuple):
    """An ampacity as reported, at a conductor temperature, weather and surface."""

    temperature: Temperature
    environment: Environment
    surface: Surface
    current: Current
    document: Document
    locator: str
    """Its row and surface: ``row Drake, E3X surface``."""

    @property
    def where(self) -> str:
        return f"{self.document.title}, {self.locator}"


class Construction(NamedTuple):
    """A measure of a design's wires as a listing gives it, beside the catalog's:
    ``outer.diameter``; a trapezoidal part's area as its wires' equivalent diameter."""

    field: str
    ours: Length
    theirs: Length


class Listing(NamedTuple):
    """A row of a document's table: the catalog design it names, and what it gives of it."""

    design: Conductor
    document: Document
    locator: str
    """Its row, as its transcription locates it: ``p. 2-3, row Drake``."""
    code_word: str
    """The name it prints the design by; none for most IEC sizes."""
    construction: tuple[Construction, ...]
    frequency: Frequency | None
    area: Area | None
    diameter: Length | None
    mass: MassPerLength | None
    dc_resistance: ResistancePerLength | None
    outer_dc_resistance: ResistancePerLength | None
    gmr: Length | None
    ac_resistances: tuple[ACResistance, ...]
    strengths: dict[type[Steel] | None, Force]
    """Rated strength by the grade of core it is reported for; by none where one is."""
    ratings: tuple[Rating, ...]

    @property
    def where(self) -> str:
        return f"{self.document.title}, {self.locator}"

    def resistances(self, frequency: Frequency) -> dict[Temperature, ResistancePerLength]:
        """Its AC resistances at a frequency, by temperature."""
        return {
            r.temperature: r.resistance for r in self.ac_resistances if r.frequency == frequency
        }


def listings(documents: Iterable[Document]) -> Iterator[Listing]:
    """Each row of each document's tables, as a listing."""
    for document in documents:
        given = conditions(document)
        for table in document.tables:
            with table.path.open(newline="", encoding="utf-8") as file:
                for row in csv.DictReader(file):
                    yield _row(document, given, table.cls, row)


def conditions(document: Document) -> dict[str, Any]:
    """A document's conditions, each value in its unit: ``"air[C]" = 25`` is ``air``,
    ``celsius(25)``."""

    def read(table: dict[str, Any]) -> dict[str, Any]:
        values: dict[str, Any] = {}
        for key, value in table.items():
            match = KEY.fullmatch(key)
            if isinstance(value, dict):
                values[key] = read(value)
            elif match:
                values[match["name"]] = SYMBOLS[match["unit"]](value)
            else:
                values[key] = value
        return values

    return read(document.conditions)


def sun(at: dict[str, Any]) -> Sun:
    """The sun a document's ampacities are rated under."""
    return Sun(
        latitude=at["latitude"],
        azimuth=at["azimuth"],
        when=at["when"],
        atmosphere=Atmosphere[at["atmosphere"].upper()],
    )


def _row(
    document: Document, given: dict[str, Any], cls: type[Conductor], row: dict[str, str]
) -> Listing:
    """What a row gives: its design's construction, and each ``reported`` column it fills, in
    the unit its header gives."""
    where = f"{document.title}, {row['locator']}"
    design = _design(cls, row, where)
    construction: list[Construction] = []
    scalars: dict[str, Quantity[Any]] = {}
    resistances: list[ACResistance] = []
    strengths: dict[type[Steel] | None, Force] = {}
    ratings: list[Rating] = []
    for name, text in row.items():
        if name in LISTING or not text.strip():
            continue
        match = COLUMN.fullmatch(name)
        if not match:
            if not (wires := WIRES.fullmatch(name)):
                raise ValueError(f"{where}: {name} is no column of a listing")
            construction.extend(_wires(design, wires, text, where))
            continue
        if match["field"] in UNREAD:
            continue
        field, value = match["field"], SYMBOLS[match["unit"]](float(text))
        if field in SCALARS:
            if field in scalars:
                raise ValueError(f"{where}: {field} is given in two units")
            scalars[field] = value
        elif at := AC.fullmatch(field):
            frequency, temperature = hz(float(at["frequency"])), celsius(float(at["temperature"]))
            resistances.append(ACResistance(temperature, frequency, ResistancePerLength.of(value)))
        elif field == "strength" or field.startswith("strength."):
            strengths[_grade(field, where)] = Force.of(value)
        elif at := AMPACITY.fullmatch(field):
            degrees = float(at["temperature"])
            if rating := _rating(document, given, at["surface"], degrees, text, row):
                ratings.append(rating)
        else:
            raise ValueError(f"{where}: reported.{field} is not a value openline compares")
    return Listing(
        design=design,
        document=document,
        locator=row["locator"],
        code_word=row["code_word"].strip(),
        construction=tuple(construction),
        frequency=given.get("frequency"),
        area=_as(Area, scalars.get("area")),
        diameter=_as(Length, scalars.get("diameter")),
        mass=_as(MassPerLength, scalars.get("mass")),
        dc_resistance=_as(ResistancePerLength, scalars.get("dc_resistance")),
        outer_dc_resistance=_as(ResistancePerLength, scalars.get("outer_dc_resistance")),
        gmr=_as(Length, scalars.get("gmr")),
        ac_resistances=tuple(resistances),
        strengths=strengths,
        ratings=tuple(ratings),
    )


def _design(cls: type[Conductor], row: dict[str, str], where: str) -> Conductor:
    """The catalog design a row names, which must be as the row gives it: its code word, its
    classes, and its designation, perhaps rounded, where the row writes it as the design's is
    written. A row may write it another way, 795 kcmil for CAN/CSA C61089's code number 403,
    as a table of another standard's sizes does; its code word and its wires then name the
    design."""
    design = getattr(import_module(f"openline.{_designs.path(cls)}"), row["design"], None)
    if not isinstance(design, cls):
        raise ValueError(f"{where}: {cls.__name__} has no design {row['design']}")
    printed, given = row["designation"].strip(), design.designation
    if printed and _kind(printed) is type(given) and not given.written_as(printed):
        raise ValueError(f"{where}: {printed}, the catalog's {given}")
    if (word := row["code_word"].strip()) and word not in design.code_words:
        raise ValueError(f"{where}: {word} is none of {row['design']}'s code words")
    if (classes := row.get("classes", "").split()) and tuple(sorted(classes)) != getattr(
        design, "classes", None
    ):
        raise ValueError(f"{where}: classes {' '.join(classes)}, not the catalog's")
    return design


def _kind(printed: str) -> type[Designation]:
    """The kind of designation a row writes: a size in kcmil, mm² or AWG, a gauge of wires, or a
    code number."""
    for kind in (Kcmil, Mm2, Gauge, WireGauge, Code):
        try:
            kind.parse(printed)
        except ValueError:
            continue
        return kind
    raise ValueError(f"{printed!r} is no designation")


def _wires(
    design: Conductor, match: re.Match[str], text: str, where: str
) -> Iterator[Construction]:
    """A part's wires as a row gives them: its counts and layers the catalog's; its diameters
    beside the catalog's, a trapezoidal part's area as its wires' equivalent diameter."""
    part, field = match["part"], match["field"]
    strand = getattr(design, part, None)
    if strand is None:
        raise ValueError(f"{where}: {type(design).__name__} has no {part}")
    if field in ("count", "layers"):
        if int(text) != getattr(strand, field, None):
            raise ValueError(f"{where}: {part}.{field} {text}, the catalog's differs")
        return
    unit = match["unit"]
    if field == "area":
        area = Area.of(SYMBOLS[unit](float(text)))
        yield Construction(f"{part}.diameter", strand.diameter, equivalent(area, strand.count))
        return
    ours = getattr(strand, field)
    if ours is None:
        raise ValueError(f"{where}: the catalog gives {part}.{field} none")
    given = awg(text) if unit == "AWG" else Length.of(SYMBOLS[unit](float(text)))
    yield Construction(f"{part}.{field}", ours, given)


def _as[Q: Quantity[Any]](kind: type[Q], value: Quantity[Any] | None) -> Q | None:
    """A reported value as the quantity its field holds; none where none is reported."""
    return None if value is None else kind.of(value)


def _grade(field: str, where: str) -> type[Steel] | None:
    """The core grade a strength is reported for, ``strength.SteelGA2``; none for one strength."""
    _, _, name = field.partition(".")
    if not name:
        return None
    grade = getattr(materials, name, None)
    if not (isinstance(grade, type) and issubclass(grade, Steel)):
        raise ValueError(f"{where}: {name} is no grade of steel")
    return grade


def _rating(
    document: Document,
    given: dict[str, Any],
    surface: str,
    temperature: float,
    text: str,
    row: dict[str, str],
) -> Rating | None:
    """An ampacity at its document's weather and the named surface; none where the document
    sets the row, or the row for that surface, apart."""
    at = given.get("ampacity", {})
    stated = at.get("surfaces", {}).get(surface)
    if stated is None:
        where = f"{document.title}, {row['locator']}"
        raise ValueError(f"{where}: ampacity.{surface} has no surface conditions")
    if row["locator"] in at.get("apart", []) or row["locator"] in stated.get("apart", []):
        return None
    environment = Environment(
        air=at["air"],
        wind=at["wind"],
        wind_angle=at["angle"],
        sun=at["sun"],
        elevation=at["elevation"],
    )
    return Rating(
        celsius(temperature),
        environment,
        Surface(emissivity=stated["emissivity"], absorptivity=stated["absorptivity"]),
        amperes(float(text)),
        document,
        f"{row['locator']}, {surface} surface",
    )
