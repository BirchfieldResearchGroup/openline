"""Compare each catalog design with what each listing gives of it (``listings``): its wires with
the catalog's, and what openline calculates with what the listing reports, at the conditions its
document states. Each listing on its own, a relative difference, openline's / the listing's - 1."""

import math
import statistics
from collections.abc import Callable, Iterable, Iterator, Sequence
from functools import cache
from typing import Any, NamedTuple

from openline.electrical import gmr, internal_impedance, magnetized, resistivity
from openline.electrical.ieee738 import IEEE738
from openline.mechanical import strength
from openline.ratings import ampacity
from openline.types import Missing
from openline.types.conductors import Conductor, Reinforced
from openline.types.conductors.strands import Helical
from openline.types.materials import Steel
from openline.types.ratings import Thermal
from openline.types.units import Force, Frequency, ResistancePerLength, celsius

from .listings import Listing, Rating, conditions, listings, sun
from .provenance import Document
from .quantities import QUANTITIES, RESISTANCE


class Comparison(NamedTuple):
    """A calculated value beside the one a listing prints, in SI, and what it is of."""

    ours: float
    theirs: float
    design: Conductor | None
    """The catalog conductor compared; none for a document's sun."""
    document: Document
    locator: str
    """Where the document prints it: ``p. 2-3, row Drake``; none for its sun."""

    @property
    def difference(self) -> float:
        """Calculated over reported, less one."""
        return self.ours / self.theirs - 1

    @property
    def standard(self) -> str:
        """The standard of the conductor compared: ``ASTM B232``."""
        return self.design.standard if self.design else ""

    @property
    def where(self) -> str:
        """``Drake, 795 kcmil, 26/7 (ASTM B232): TransPowr ACSR…, p. 2-3, row Drake``."""
        given = ", ".join(filter(None, (self.document.title, self.locator)))
        return f"{self.design.title}: {given}" if self.design else given


class Summary(NamedTuple):
    """Relative differences: count, signed median, and 95th percentile and maximum magnitudes."""

    compared: int
    median: float
    percentile: float
    largest: float


class Check(NamedTuple):
    """A value compared, and the bound the 95th percentile of its differences keeps within."""

    label: str
    bound: float
    of: str = ""
    """The value it takes some comparisons of, where not its own label's."""
    takes: Callable[[Comparison], bool] = lambda each: True


DC = "DC resistance at 20\u202f°C"
ACSS = ("ASTM B856", "ASTM B856, AW", "ASTM B857", "ASTM B857, AW")
# ASTM B231's, B399's and B524's mass and resistance are reported with their tables' approximate
# increments, 2% and, for B524's largest sizes, up to 4% (B524, table 8). Makers rate ACSS's
# 1350-O, round or trapezoidal, at 63% IACS, where B856-03 and B857-14, 11.2, prescribe 0.0279
# Ω·mm²/m, 1.95% more.
# Helical coupling affects AC resistance, GMR and ampacity, most with four layers. B524-99's metric
# rated strengths fall below the wire tables at hand, by up to 6%. Prysmian's
# GMRs run above openline's by up to 2.5%.
CHECKS = (
    Check("Construction", 0.01),
    Check("Diameter", 0.005),
    Check("Area", 0.005),
    Check("Mass", 0.01),
    Check(DC, 0.015, takes=lambda each: each.standard not in ACSS),
    Check(f"{DC}, ACSS", 0.025, of=DC, takes=lambda each: each.standard in ACSS),
    Check(f"{DC}, outer wires", 0.01),
    Check("AC resistance", 0.02),
    Check("Rated strength", 0.01),
    Check("GMR", 0.025),
    Check("Sun's heat flux", 0.001),
    Check("Ampacity", 0.01),
    Check("Ampacity, from reported resistances", 0.01),
)
STANDARDS = (  # the values tabulated by standard: a column each, and the value it takes
    ("Mass", "Mass"),
    ("DC resistance", DC),
    ("AC resistance", "AC resistance"),
    ("Rated strength", "Rated strength"),
    ("GMR", "GMR"),
    ("Ampacity", "Ampacity"),
)

type Compared = list[tuple[Check, list[Comparison]]]


def comparisons(documents: Iterable[Document]) -> Compared:
    """Each check's comparisons: those of its value it takes."""
    values = dict(_values(documents))
    if untaken := set(values) - {check.of or check.label for check in CHECKS}:
        raise ValueError(f"no check takes {', '.join(sorted(untaken))}")
    return [
        (check, [each for each in values[check.of or check.label] if check.takes(each)])
        for check in CHECKS
    ]


def by_standard(found: Compared) -> dict[str, dict[str, tuple[Summary, float]]]:
    """Each standard's comparisons of each value ``STANDARDS`` tabulates, summarized, with the
    bound of the check that takes them."""
    table: dict[str, dict[str, tuple[Summary, float]]] = {}
    for column, value in STANDARDS:
        groups: dict[tuple[str, float], list[Comparison]] = {}
        for check, compared in found:
            if (check.of or check.label) == value:
                for each in compared:
                    if each.standard:
                        groups.setdefault((each.standard, check.bound), []).append(each)
        for (standard, bound), group in groups.items():
            table.setdefault(standard, {})[column] = (summary(group), bound)
    return dict(sorted(table.items()))


def largest(compared: Sequence[Comparison]) -> Comparison:
    """The comparison farthest apart."""
    return max(compared, key=lambda each: abs(each.difference))


def _values(documents: Iterable[Document]) -> list[tuple[str, list[Comparison]]]:
    """Compare each value openline calculates with each listing that reports it.

    ``Ampacity, from reported resistances`` rates a listing's own diameter and AC resistances,
    testing the heat balance alone."""
    found = tuple(documents)
    rows = list(listings(found))
    computed = [r for r in rows if RESISTANCE.value(r.design) is not None]
    return [
        (
            "Construction",
            [
                Comparison(each.ours.si, each.theirs.si, r.design, r.document, r.locator)
                for r in rows
                for each in r.construction
            ],
        ),
        *(
            (
                quantity.label,
                [
                    _compared(ours, theirs, r)
                    for r in rows
                    if (theirs := getattr(r, quantity.reported)) is not None
                    and (ours := quantity.value(r.design)) is not None
                ],
            )
            for quantity in QUANTITIES
        ),
        (
            f"{RESISTANCE.label}, outer wires",
            [
                _compared(ours, r.outer_dc_resistance, r)
                for r in rows
                if r.outer_dc_resistance is not None and (ours := _outer(r.design)) is not None
            ],
        ),
        (
            "AC resistance",
            [
                _compared(
                    internal_impedance(
                        r.design, temperature=ac.temperature, frequency=ac.frequency
                    ).resistance,
                    ac.resistance,
                    r,
                )
                for r in computed
                if not magnetized(r.design)
                for ac in r.ac_resistances
            ],
        ),
        (
            "Rated strength",
            [
                _compared(rated, given, r)
                for r in rows
                for grade, given in r.strengths.items()
                if (rated := _strength(r.design, grade)) is not None
            ],
        ),
        (
            "GMR",
            [
                _compared(gmr(r.design, temperature=celsius(20), frequency=r.frequency), r.gmr, r)
                for r in computed
                if r.gmr is not None and r.frequency is not None and not magnetized(r.design)
            ],
        ),
        ("Sun's heat flux", list(_suns(found))),
        (
            "Ampacity",
            [
                _rating(r.design, rating, r.design, frequency=r.frequency)
                for r in computed
                if r.frequency is not None and not magnetized(r.design)
                for rating in r.ratings
            ],
        ),
        (
            "Ampacity, from reported resistances",
            [
                _rating(given, rating, r.design)
                for r in rows
                if (given := _stated(r)) is not None
                for rating in r.ratings
            ],
        ),
    ]


def summary(compared: Sequence[Comparison]) -> Summary:
    """Summarize relative differences as ``ours / theirs - 1``."""
    differences = [each.ours / each.theirs - 1 for each in compared]
    sizes = sorted(abs(difference) for difference in differences)
    percentile = sizes[math.ceil(0.95 * len(sizes)) - 1]
    return Summary(len(sizes), statistics.median(differences), percentile, sizes[-1])


def _compared(ours: Any, theirs: Any, given: Listing) -> Comparison:
    return Comparison(ours.si, theirs.si, given.design, given.document, given.locator)


@cache
def _strength(conductor: Conductor, grade: type[Steel] | None) -> Force | None:
    """Its rated strength, its core of ``grade`` where given; none where openline does not have
    its standard's rating factors or its wires' stresses, or its standard names no such grade
    (Prysmian rates ACSR/TW on GA5, which ASTM B779 does not name)."""
    if grade is not None and grade not in conductor.grades:
        return None
    try:
        return strength(conductor, core=grade)
    except Missing:
        return None


@cache
def _outer(conductor: Conductor) -> ResistancePerLength | None:
    """DC resistance at 20 °C of a reinforced conductor's outer wires alone, each lengthened by
    its lay; none where openline does not have their lay."""
    if not isinstance(conductor, Reinforced):
        raise ValueError(f"{conductor.title} has no outer wires apart from a core")
    conductance = 0.0
    try:
        layers = conductor.layers
    except Missing:
        return None
    for layer in layers:
        if conductor.outer not in layer.wires:
            continue
        if not isinstance(layer, Helical):
            return None
        for wire in layer.wires:
            if wire == conductor.outer:
                resistance = resistivity(wire.material, temperature=celsius(20)).si * layer.factor
                conductance += wire.area.si / wire.count / resistance
    return ResistancePerLength(1 / conductance)


def _stated(given: Listing) -> Thermal | None:
    """A listing's own diameter and AC resistances, as a heat balance takes them; none where it
    reports no diameter, or no two resistances at its document's frequency."""
    if given.diameter is None or given.frequency is None:
        return None
    points = given.resistances(given.frequency)
    if len(points) < 2:
        return None
    return Thermal.from_resistances(
        diameter=given.diameter, frequency=given.frequency, resistances=points
    )


def _rating(
    given: Conductor | Thermal,
    rating: Rating,
    design: Conductor,
    *,
    frequency: Frequency | None = None,
) -> Comparison:
    """A listing's ampacity of ``design``, rated from ``given``: the design itself, or the
    listing's own diameter and resistances."""
    ours = ampacity(
        given,
        temperature=rating.temperature,
        environment=rating.environment,
        frequency=frequency,
        standard=IEEE738,
        surface=rating.surface,
    )
    return Comparison(ours.si, rating.current.si, design, rating.document, rating.locator)


def _suns(documents: Iterable[Document]) -> Iterator[Comparison]:
    """Compare reported solar flux with IEEE 738 at the stated conditions."""
    for document in documents:
        if at := conditions(document).get("ampacity"):
            ours = IEEE738.flux(sun(at), at["elevation"])
            yield Comparison(ours.si, at["sun"].si, None, document, "")
