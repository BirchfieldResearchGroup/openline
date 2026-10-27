"""Current schedules and heat-balance interfaces for conductor ratings."""

from abc import ABC, abstractmethod
from collections.abc import Callable, Mapping
from datetime import timedelta
from typing import ClassVar

from . import Record
from .conductors import Surface
from .environment import Environment, Sun
from .units import (
    Current,
    Frequency,
    HeatCapacityPerLength,
    HeatFlux,
    Length,
    PowerPerLength,
    ResistancePerLength,
    Temperature,
    celsius,
    m,
)

__all__ = ["Interval", "RatingStandard", "TemperatureProfile", "Thermal"]


class Interval(Record):
    """A time interval with constant current and weather conditions."""

    current: Current
    """The current."""
    environment: Environment
    """The environment."""
    duration: timedelta
    """How long it lasts."""

    def __post_init__(self) -> None:
        if self.duration <= timedelta(0):
            raise ValueError("an operating interval must have positive duration")


class Thermal(Record):
    """Supplied thermal data for ratings, with a resistance callback or ``from_resistances``.

    For catalog conductors, pass the conductor and frequency directly to ``openline.ratings``.
    """

    diameter: Length
    """Outside diameter."""
    resistance: Callable[[Temperature, Current], ResistancePerLength]
    """AC resistance per length at a temperature and current."""
    heat_capacity: HeatCapacityPerLength | None = None
    """Heat capacity per length; none where unknown, which only transient ratings need."""
    core_diameter: Length = m(0)
    """Diameter of its steel core; zero without one."""

    frequency: Frequency | None = None
    """Frequency represented by the resistance data, if specified."""

    @classmethod
    def from_resistances(
        cls,
        *,
        diameter: Length,
        frequency: Frequency,
        resistances: Mapping[Temperature, ResistancePerLength],
        heat_capacity: HeatCapacityPerLength | None = None,
        core_diameter: Length | None = None,
    ) -> "Thermal":
        """Use supplied AC resistances, linear between and beyond the nearest two points.

        The selected rating standard still controls how it samples this resistance curve.
        Heat capacity is required only for transient calculations.
        """
        return cls(
            diameter=diameter,
            resistance=_interpolated(resistances),
            frequency=frequency,
            heat_capacity=heat_capacity,
            core_diameter=core_diameter if core_diameter is not None else m(0),
        )


class TemperatureProfile(Record):
    """Temperatures at elapsed times, including time zero and every interval boundary."""

    elapsed: tuple[timedelta, ...]
    """Elapsed times from the start of the schedule."""
    temperatures: tuple[Temperature, ...]
    """Conductor temperatures at those times."""


class RatingStandard(ABC):
    """Heat-balance interface implemented by rating standards.

    Pass the class, not an instance, to the rating functions."""

    step: ClassVar[timedelta]
    """The longest time step it allows."""

    @staticmethod
    @abstractmethod
    def convection(
        thermal: Thermal, temperature: Temperature, environment: Environment
    ) -> PowerPerLength:
        """Convective heat loss per unit length; negative below air temperature."""

    @staticmethod
    @abstractmethod
    def radiation(
        thermal: Thermal,
        temperature: Temperature,
        environment: Environment,
        *,
        surface: Surface,
    ) -> PowerPerLength:
        """Net radiative heat loss per unit length."""

    @staticmethod
    @abstractmethod
    def flux(sun: Sun, elevation: Length) -> HeatFlux:
        """Solar heat flux at the specified elevation."""

    @staticmethod
    @abstractmethod
    def resistance(
        thermal: Thermal, temperature: Temperature, current: Current
    ) -> ResistancePerLength:
        """Resistance per unit length at the specified temperature and current."""


def _interpolated(
    points: Mapping[Temperature, ResistancePerLength],
) -> Callable[[Temperature, Current], ResistancePerLength]:
    """Interpolate supplied resistance data and extrapolate with the nearest pair."""
    given = sorted(points.items(), key=lambda point: point[0].si)
    if len(given) < 2:
        raise ValueError("a stated resistance takes two temperatures or more")

    def resistance(at: Temperature, _current: Current) -> ResistancePerLength:
        below = [point for point in given if point[0] < at]
        above = [point for point in given if point[0] > at]
        if len(below) + len(above) < len(given):
            return next(value for when, value in given if when == at)
        if below and above:
            (low, cold), (high, hot) = below[-1], above[0]
        else:
            (low, cold), (high, hot) = above[:2] if above else below[-2:]
        share = (at.to(celsius) - low.to(celsius)) / (high.to(celsius) - low.to(celsius))
        return cold + (hot - cold) * share

    return resistance
