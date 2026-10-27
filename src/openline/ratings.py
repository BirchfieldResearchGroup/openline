"""Steady and transient ratings from a conductor or supplied thermal data.

A catalog conductor requires frequency. A Thermal owns its resistance data and accepts no
frequency override. Surface and weather assumptions remain explicit for every calculation.
"""

import math
from collections.abc import Iterable
from datetime import timedelta

from .electrical import _heat, internal_impedance
from .electrical.ieee738 import IEEE738
from .mechanical import masses
from .types.conductors import Conductor, SteelCored, Surface
from .types.environment import Environment
from .types.ratings import Interval, RatingStandard, TemperatureProfile, Thermal
from .types.units import (
    Current,
    Frequency,
    HeatCapacityPerLength,
    Temperature,
    ThermalConductivity,
    celsius,
    j_per_m_k,
    m,
)

__all__ = ["ampacity", "core_temperature", "heat_capacity", "temperature", "temperature_profile"]


def ampacity(
    conductor: Conductor | Thermal,
    *,
    temperature: Temperature,
    environment: Environment,
    surface: Surface,
    frequency: Frequency | None = None,
    duration: timedelta | None = None,
    initial_temperature: Temperature | None = None,
    standard: type[RatingStandard] = IEEE738,
) -> Current:
    """Current holding a temperature, or reaching it after a specified duration.

    Transient ratings require both duration and initial_temperature. Steady ratings need no
    heat capacity. The standard defaults to IEEE 738.
    """
    _transient(duration, initial_temperature)
    model = _model(conductor, frequency, duration is not None)
    if duration is None:
        return _heat.held_current(model, temperature, environment, standard, surface=surface)
    assert initial_temperature is not None
    return _heat.reached_current(
        model, temperature, environment, standard, initial_temperature, duration, surface=surface
    )


def temperature(
    conductor: Conductor | Thermal,
    *,
    current: Current,
    environment: Environment,
    surface: Surface,
    frequency: Frequency | None = None,
    duration: timedelta | None = None,
    initial_temperature: Temperature | None = None,
    standard: type[RatingStandard] = IEEE738,
) -> Temperature:
    """Temperature at a steady current, or after a specified duration from an initial state."""
    _transient(duration, initial_temperature)
    model = _model(conductor, frequency, duration is not None)
    if duration is None:
        return _heat.held_temperature(model, current, environment, standard, surface=surface)
    assert initial_temperature is not None
    interval = Interval(current=current, environment=environment, duration=duration)
    return _heat.stepped(model, [interval], standard, initial_temperature, surface=surface)[-1]


def temperature_profile(
    conductor: Conductor | Thermal,
    intervals: Iterable[Interval],
    *,
    surface: Surface,
    initial_temperature: Temperature,
    frequency: Frequency | None = None,
    sample_every: timedelta | None = None,
    standard: type[RatingStandard] = IEEE738,
) -> TemperatureProfile:
    """Temperatures through a schedule with constant current and weather per interval.

    Always includes time zero and interval boundaries. Without sample_every, returns those
    points only. Other samples interpolate the standard's fixed integration trajectory, so
    output sampling does not change calculated endpoint temperatures. Sun inputs are held
    fixed within each interval; supply changed weather for changing solar conditions.
    """
    if sample_every is not None and sample_every <= timedelta(0):
        raise ValueError("sample_every must be positive")
    given = tuple(intervals)
    model = _model(conductor, frequency, bool(given))
    times = {timedelta(0)}
    end = timedelta(0)
    for interval in given:
        end += interval.duration
        times.add(end)
    if sample_every is not None:
        sample = sample_every
        while sample < end:
            times.add(sample)
            sample += sample_every
    elapsed = tuple(sorted(times))
    if not given:
        return TemperatureProfile(elapsed=elapsed, temperatures=(initial_temperature,))
    trajectory = iter(
        _heat.trajectory(model, given, standard, initial_temperature, surface=surface)
    )
    left = right = next(trajectory)
    temperatures = []
    for at in elapsed:
        while right[0] < at:
            left, right = right, next(trajectory)
        if at == right[0]:
            temperatures.append(right[1])
        else:
            fraction = (at - left[0]) / (right[0] - left[0])
            low, high = left[1].to(celsius), right[1].to(celsius)
            temperatures.append(celsius(low + fraction * (high - low)))
    return TemperatureProfile(elapsed=elapsed, temperatures=tuple(temperatures))


def core_temperature(
    conductor: Conductor | Thermal,
    *,
    current: Current,
    surface_temperature: Temperature,
    conductivity: ThermalConductivity,
    frequency: Frequency | None = None,
    standard: type[RatingStandard] = IEEE738,
) -> Temperature:
    """Core (or center) temperature from surface temperature and radial conductivity.

    Uses IEEE 738-2023 informative annex C, equations C.1 to C.3, iterating on average
    wire temperature. For conductors without a steel core, returns center temperature.
    """
    model = _model(conductor, frequency, False)
    outside = surface_temperature.to(celsius)
    outer, core = model.diameter.si, model.core_diameter.si
    if core > 0:
        shape = (0.5 - core**2 / (outer**2 - core**2) * math.log(outer / core)) / (2 * math.pi)
    else:
        shape = 1 / (4 * math.pi)
    inside = outside
    for _ in range(100):
        average = celsius((inside + outside) / 2)
        ohms = standard.resistance(model, average, current)
        warmer = outside + current.si**2 * ohms.si * shape / conductivity.si
        if abs(warmer - inside) < 1e-6:
            break
        inside = warmer
    return celsius(inside)


def heat_capacity(conductor: Conductor) -> HeatCapacityPerLength:
    r"""Heat capacity per meter: each strand's mass times its specific heat (IEEE 738-2023,
    equation 34).

    .. math:: C = \sum_s m_s c_s
    """
    parts = zip(masses(conductor), conductor.strands, strict=True)
    return j_per_m_k(sum(m.si * strand.material.specific_heat.si for m, strand in parts))


def _model(given: Conductor | Thermal, frequency: Frequency | None, transient: bool) -> Thermal:
    if isinstance(given, Thermal):
        if frequency is not None:
            raise TypeError("Thermal already owns its resistance data; omit frequency")
        return given
    if frequency is None:
        raise TypeError("a conductor rating requires frequency")
    return Thermal(
        diameter=given.diameter,
        frequency=frequency,
        resistance=lambda at, _current: (
            internal_impedance(given, temperature=at, frequency=frequency).resistance
        ),
        heat_capacity=heat_capacity(given) if transient else None,
        core_diameter=given.core_diameter if isinstance(given, SteelCored) else m(0),
    )


def _transient(duration: timedelta | None, initial: Temperature | None) -> None:
    if (duration is None) != (initial is None):
        raise TypeError("a transient rating requires both duration and initial_temperature")
    if duration is not None and duration <= timedelta(0):
        raise ValueError("duration must be positive")
