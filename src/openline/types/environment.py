"""Weather, solar inputs, and earth properties."""

from datetime import datetime
from enum import Enum, auto

from . import Record
from .units import Angle, HeatFlux, Length, Resistivity, Speed, Temperature

__all__ = ["Atmosphere", "Earth", "Environment", "Sun"]


class Atmosphere(Enum):
    """Air clarity categories used by the solar heat-flux model."""

    CLEAR = auto()
    """Clear air."""
    INDUSTRIAL = auto()
    """Industrial air with reduced solar transmission."""


class Sun(Record):
    """Inputs for solar heating at a conductor's location and orientation."""

    latitude: Angle
    """Latitude, north positive."""
    azimuth: Angle
    """Conductor bearing measured from north."""
    when: datetime
    """Local solar time, rather than civil clock time."""
    atmosphere: Atmosphere
    """Air clarity used by the solar model."""


class Environment(Record):
    """Weather and elevation at a conductor.

    Wind angle and solar input apply to the conductor's orientation.
    """

    air: Temperature
    """Air temperature."""
    wind: Speed
    """Wind speed."""
    wind_angle: Angle
    """Angle to the conductor axis: 90 degrees across it, 0 degrees along it."""
    sun: Sun | HeatFlux
    """Solar model inputs or incident heat flux, before surface absorption."""
    elevation: Length
    """Elevation above sea level."""


class Earth(Record, kw_only=False):
    """Uniform earth properties: ``Earth(ohm_m(100), 10)``."""

    resistivity: Resistivity
    """Electrical resistivity."""
    relative_permittivity: float
    """Permittivity relative to vacuum."""
