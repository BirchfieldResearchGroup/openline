"""IEEE 738 benchmark

Reproduce the steady and 15-minute reference calculations in IEEE 738-2023. Keep the
sample's stated diameter, resistance curve, heat capacity, and solar conditions. The thermal
model owns its 60 Hz resistance data; no frequency override is passed to the rating functions.
The `Sun.when` value is local solar time.
"""

from datetime import datetime, timedelta

from openline import Atmosphere, Environment, Sun, Surface, Thermal, ratings
from openline import units as u

# %% Setup
# IEEE 738-2023, 4.6.1.1 and 4.6.3: retain the sample's stated thermal data.
reference = Thermal.from_resistances(
    diameter=u.mm(28.14),
    frequency=u.hz(60),
    resistances={
        u.celsius(25): u.ohm_per_km(0.07283),
        u.celsius(75): u.ohm_per_km(0.08688),
        u.celsius(200): u.ohm_per_km(0.1220),
    },
    heat_capacity=u.j_per_m_k(1310),
)
sun = Sun(
    latitude=u.degrees(30),
    azimuth=u.degrees(90),
    when=datetime(2026, 6, 10, 11),  # Local solar time.
    atmosphere=Atmosphere.CLEAR,
)
weather = Environment(
    air=u.celsius(40),
    wind=u.m_per_s(0.61),
    wind_angle=u.degrees(90),
    sun=sun,
    elevation=u.m(0),
)
surface = Surface(emissivity=0.8, absorptivity=0.8)

# %% Calculation
steady = ratings.ampacity(
    reference,
    temperature=u.celsius(100),
    environment=weather,
    surface=surface,
)
hot = ratings.temperature(
    reference,
    current=u.amperes(1000),
    environment=weather,
    surface=surface,
)
emergency = ratings.ampacity(
    reference,
    temperature=u.celsius(125),
    initial_temperature=u.celsius(100),
    duration=timedelta(minutes=15),
    environment=weather,
    surface=surface,
)
print("Steady ampacity:", steady, "(IEEE: 1025 A)")
print("Temperature at 1000 A:", hot, "(IEEE: 97.5 °C)")
print("15-minute ampacity:", emergency, "(IEEE: 1312 A)")
