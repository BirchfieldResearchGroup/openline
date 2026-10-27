"""IEEE Std 738-2023 heat balance, resistance interpolation, and time-step limit.

Solar flux follows the position and atmosphere model in 4.4.5. Resistance is interpolated
between 25 °C and 75 °C, or 200 °C above 100 °C (4.4.6, equation 33), its ends the
``Thermal``'s. Calculated resistance uses fixed permeability; magnetic heating is a known
limitation (4.5.1)."""

import math
from datetime import timedelta

from ..types.conductors import Surface
from ..types.environment import Atmosphere, Environment, Sun
from ..types.ratings import RatingStandard, Thermal
from ..types.units import (
    Current,
    HeatFlux,
    Length,
    PowerPerLength,
    ResistancePerLength,
    Temperature,
    celsius,
    w_per_m,
    w_per_m2,
)

__all__ = ["IEEE738"]

LOW, HIGH, HIGHER = 25.0, 75.0, 200.0  # °C: equation 33's ends, the higher above 100 °C

SUN = {
    Atmosphere.CLEAR: (
        -42.2391, 63.8044, -1.9220, 3.46921e-2, -3.61118e-4, 1.94318e-6, -4.07608e-9
    ),
    Atmosphere.INDUSTRIAL: (
        53.1821, 14.2110, 6.6138e-1, -3.1658e-2, 5.4654e-4, -4.3446e-6, 1.3236e-8
    ),
}  # fmt: skip
"""The coefficients, from the sun's altitude in degrees, of the heat flux it gives at sea level,
in clear air (table 4) and in industrial air (table 5), which is less conservative, for
engineering judgment (4.4.5.5)."""


class IEEE738(RatingStandard):
    """IEEE Std 738-2023, the default standard for ``openline.ratings`` calculations."""

    step = timedelta(seconds=10)
    """Transient and dynamic steps shall be 10 s or less (4.2.1)."""

    @staticmethod
    def convection(
        thermal: Thermal, temperature: Temperature, environment: Environment
    ) -> PowerPerLength:
        """Return maximum convection loss (4.4.3); negative below air temperature."""
        surface, air = temperature.to(celsius), environment.air.to(celsius)
        rise = abs(surface - air)
        film = (surface + air) / 2
        height = environment.elevation.si
        density = (1.293 - 1.525e-4 * height + 6.379e-9 * height**2) / (1 + 0.00367 * film)
        viscosity = 1.458e-6 * (film + 273) ** 1.5 / (film + 383.4)
        conductivity = 2.424e-2 + 7.477e-5 * film - 4.407e-9 * film**2
        diameter = thermal.diameter.si
        reynolds = diameter * density * environment.wind.si / viscosity
        phi = environment.wind_angle.si
        direction = 1.194 - math.cos(phi) + 0.194 * math.cos(2 * phi) + 0.368 * math.sin(2 * phi)
        low = direction * (1.01 + 1.35 * reynolds**0.52) * conductivity * rise
        high = direction * 0.754 * reynolds**0.6 * conductivity * rise
        natural = 3.645 * density**0.5 * diameter**0.75 * rise**1.25
        heat = math.copysign(max(low, high, natural), surface - air)
        return w_per_m(heat)

    @staticmethod
    def radiation(
        thermal: Thermal,
        temperature: Temperature,
        environment: Environment,
        *,
        surface: Surface,
    ) -> PowerPerLength:
        """Return net radiative heat loss to surroundings at air temperature (4.4.4)."""
        hot = (temperature.to(celsius) + 273) / 100
        cold = (environment.air.to(celsius) + 273) / 100
        across = thermal.diameter.si
        return w_per_m(17.8 * across * surface.emissivity * (hot**4 - cold**4))

    @staticmethod
    def flux(sun: Sun, elevation: Length) -> HeatFlux:
        """Calculate solar flux from position, atmosphere, and elevation (4.4.5); zero at night."""
        lat = sun.latitude.si
        day = sun.when.timetuple().tm_yday
        declination = math.radians(23.45 * math.sin(math.radians((284 + day) / 365 * 360)))
        hours = sun.when.hour + sun.when.minute / 60 + sun.when.second / 3600
        hour = math.radians(15 * (hours - 12))
        altitude = math.asin(
            math.cos(lat) * math.cos(declination) * math.cos(hour)
            + math.sin(lat) * math.sin(declination)
        )
        if altitude <= 0:
            return w_per_m2(0)
        chi = math.sin(hour) / (
            math.sin(lat) * math.cos(hour) - math.cos(lat) * math.tan(declination)
        )
        afternoon, behind = hour >= 0, chi < 0
        constant = 180.0 * (afternoon + behind)  # table 3's solar azimuth constant: 0, 180 or 360
        solar_azimuth = math.radians(constant + math.degrees(math.atan(chi)))
        incidence = math.acos(math.cos(altitude) * math.cos(solar_azimuth - sun.azimuth.si))
        degrees = math.degrees(altitude)
        flux = sum(c * degrees**power for power, c in enumerate(SUN[sun.atmosphere]))
        height = elevation.si
        flux *= 1 + 1.148e-4 * height - 1.108e-8 * height**2
        return w_per_m2(max(flux, 0.0) * math.sin(incidence))

    @staticmethod
    def resistance(
        thermal: Thermal, temperature: Temperature, current: Current
    ) -> ResistancePerLength:
        """Interpolate resistance using equation 33, between the ``Thermal``'s resistances at
        25 °C and 75 °C, or 200 °C above 100 °C."""
        degrees = temperature.to(celsius)
        high = HIGH if degrees <= 100 else HIGHER
        cold, hot = (thermal.resistance(celsius(at), current) for at in (LOW, high))
        return cold + (hot - cold) * ((degrees - LOW) / (high - LOW))
