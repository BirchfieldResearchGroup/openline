r"""Steady-state and transient heat-balance solvers for Joule heating, solar gain, and cooling."""

import math
from collections.abc import Iterator, Sequence
from datetime import timedelta

from ..types import Missing
from ..types.conductors import Surface
from ..types.environment import Environment
from ..types.ratings import Interval, RatingStandard, Thermal
from ..types.units import (
    Current,
    HeatFlux,
    PowerPerLength,
    Temperature,
    amperes,
    celsius,
    w_per_m,
)

__all__ = ["cooling", "held_current", "held_temperature", "reached_current", "stepped"]

HOTTEST = 500.0  # °C: the highest temperature a steady state is looked for at


def held_current(
    thermal: Thermal,
    temperature: Temperature,
    environment: Environment,
    standard: type[RatingStandard],
    *,
    surface: Surface,
) -> Current:
    r"""The steady current that holds the conductor at ``temperature``,

    .. math::  I = \sqrt{\frac{q_c(T) + q_r(T) - q_s}{R(T, I)}}

    iterated to within 1 mA, for the resistance may depend on the current."""
    spare = cooling(thermal, temperature, environment, standard, surface=surface)
    if spare.si <= 0:
        raise ValueError(f"the sun alone holds the conductor above {temperature}")
    current = amperes(0)
    while True:
        ohms = standard.resistance(thermal, temperature, current)
        held = amperes(math.sqrt(spare.si / ohms.si))
        if abs(held.si - current.si) < 1e-3:
            return held
        current = held


def held_temperature(
    thermal: Thermal,
    current: Current,
    environment: Environment,
    standard: type[RatingStandard],
    *,
    surface: Surface,
) -> Temperature:
    """Solve steady-state temperature by bisection to within 0.01 °C."""

    def excess(degrees: float) -> float:
        held = celsius(degrees)
        ohms = standard.resistance(thermal, held, current)
        return (
            cooling(thermal, held, environment, standard, surface=surface).si
            - current.si**2 * ohms.si
        )

    low, high = environment.air.to(celsius), HOTTEST
    if excess(high) < 0:
        raise ValueError(f"{current} holds the conductor above {HOTTEST:g} °C")
    while high - low > 0.01:
        middle = (low + high) / 2
        low, high = (middle, high) if excess(middle) < 0 else (low, middle)
    return celsius((low + high) / 2)


def reached_current(
    thermal: Thermal,
    temperature: Temperature,
    environment: Environment,
    standard: type[RatingStandard],
    begin: Temperature,
    duration: timedelta,
    *,
    surface: Surface,
) -> Current:
    """Find current reaching ``temperature`` after ``duration`` (bisection within 0.1 A)."""
    if temperature <= begin:
        raise ValueError(f"the conductor is already at {begin}, not below {temperature}")

    def reached(amps: float) -> Temperature:
        interval = Interval(current=amperes(amps), environment=environment, duration=duration)
        return stepped(thermal, [interval], standard, begin, surface=surface)[-1]

    low = 0.0
    high = held_current(thermal, temperature, environment, standard, surface=surface).si
    while reached(high) < temperature:
        low, high = high, 2 * high
    while high - low > 0.1:
        middle = (low + high) / 2
        low, high = (middle, high) if reached(middle) < temperature else (low, middle)
    return amperes((low + high) / 2)


def stepped(
    thermal: Thermal,
    intervals: Sequence[Interval],
    standard: type[RatingStandard],
    begin: Temperature,
    *,
    surface: Surface,
) -> tuple[Temperature, ...]:
    r"""The conductor's temperature at the end of each interval, from ``begin``, its heat
    capacity per length :math:`C` the ``Thermal``'s: the balance stepped through time,

    .. math::  T(t + \Delta t) = T(t) + \frac{\Delta t}{C}\Bigl[I^2R\bigl(T(t)\bigr) + q_s
               - q_c\bigl(T(t)\bigr) - q_r\bigl(T(t)\bigr)\Bigr]

    each step :math:`\Delta t` no longer than the standard allows. A ``Thermal`` without heat
    capacity raises ``Missing``."""
    boundaries = set()
    elapsed = timedelta(0)
    for interval in intervals:
        elapsed += interval.duration
        boundaries.add(elapsed)
    return tuple(
        temperature
        for at, temperature in trajectory(thermal, intervals, standard, begin, surface=surface)
        if at in boundaries
    )


def trajectory(
    thermal: Thermal,
    intervals: Sequence[Interval],
    standard: type[RatingStandard],
    begin: Temperature,
    *,
    surface: Surface,
) -> Iterator[tuple[timedelta, Temperature]]:
    """The unchanged Euler trajectory, including initial state and every solver step.

    Output sampling interpolates these points rather than changing integration steps.
    """
    if thermal.heat_capacity is None:
        raise Missing("a transient rating takes the conductor's heat capacity")
    capacity = thermal.heat_capacity.si
    longest = standard.step.total_seconds()
    degrees = begin.to(celsius)
    elapsed = timedelta(0)
    yield elapsed, begin
    for interval in intervals:
        seconds = interval.duration.total_seconds()
        steps = max(1, math.ceil(seconds / longest))
        for step in range(1, steps + 1):
            held = celsius(degrees)
            ohms = standard.resistance(thermal, held, interval.current)
            joule = ohms.si * interval.current.si**2
            net = joule - cooling(thermal, held, interval.environment, standard, surface=surface).si
            degrees += net / capacity * seconds / steps
            yield elapsed + interval.duration * (step / steps), celsius(degrees)
        elapsed += interval.duration


def cooling(
    thermal: Thermal,
    temperature: Temperature,
    environment: Environment,
    standard: type[RatingStandard],
    *,
    surface: Surface,
) -> PowerPerLength:
    r"""Return net cooling per unit length: convection plus radiation minus absorbed solar heat."""
    sun = environment.sun
    flux = sun if isinstance(sun, HeatFlux) else standard.flux(sun, environment.elevation)
    solar = w_per_m(surface.absorptivity * flux.si * thermal.diameter.si)
    convection = standard.convection(thermal, temperature, environment)
    return (
        convection + standard.radiation(thermal, temperature, environment, surface=surface) - solar
    )
