"""What openline calculates of a conductor, as its catalog tabulates it and the validation
compares it with what listings report: a column each, each value calculated once a design, and
none where openline does not have what it takes."""

from collections.abc import Callable
from functools import cache

from openline.electrical import internal_impedance
from openline.mechanical import mass
from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.units import (
    Area,
    Length,
    MassPerLength,
    ResistancePerLength,
    celsius,
    hz,
    kg_per_m,
    mm,
    mm2,
    ohm_per_km,
)

from .presentation import Column

AT = "20\u202f°C"


def calculated[Q](calculation: Callable[[Conductor], Q]) -> Callable[[Conductor], Q | None]:
    """A calculation of a design, once; none where openline does not have what it takes."""

    @cache
    def value(record: Conductor) -> Q | None:
        try:
            return calculation(record)
        except Missing:
            return None

    return value


def resistance(record: Conductor) -> ResistancePerLength:
    """DC resistance at 20 °C of all its wires."""
    return internal_impedance(record, temperature=celsius(20), frequency=hz(0)).resistance


DIAMETER = Column[Conductor, Length](
    "Diameter", calculated(lambda c: c.diameter), mm, reported="diameter"
)
AREA = Column[Conductor, Area]("Area", lambda c: c.area, mm2, reported="area")
MASS = Column[Conductor, MassPerLength]("Mass", calculated(mass), kg_per_m, reported="mass")
RESISTANCE = Column[Conductor, ResistancePerLength](
    "DC resistance",
    calculated(resistance),
    ohm_per_km,
    at=AT,
    reported="dc_resistance",
)
QUANTITIES = (DIAMETER, AREA, MASS, RESISTANCE)
