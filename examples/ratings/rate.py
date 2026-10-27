"""Ampacity, temperature, and sag

Find ampacity at 100 °C and temperature at 1000 A under specified weather. Then use that
temperature to calculate sag in a 300 m level span. Surface properties and incident sunlight
are explicit assumptions.
"""

from openline import Environment, Strung, Surface, conductors, mechanical, ratings
from openline import units as u

# %% Setup
drake = conductors.astm.b232.DRAKE
weather = Environment(
    air=u.celsius(40),
    wind=u.m_per_s(0.61),
    wind_angle=u.degrees(90),
    sun=u.w_per_m2(1000),
    elevation=u.m(0),
)
surface = Surface(emissivity=0.8, absorptivity=0.8)

# %% Calculation
ampacity = ratings.ampacity(
    drake,
    temperature=u.celsius(100),
    frequency=u.hz(60),
    environment=weather,
    surface=surface,
)
temperature = ratings.temperature(
    drake,
    current=u.amperes(1000),
    frequency=u.hz(60),
    environment=weather,
    surface=surface,
)
print("Ampacity at 100 °C:", ampacity)
print("Temperature at 1000 A:", temperature)

sag = mechanical.sag(
    drake,
    span=u.m(300),
    strung=Strung(u.kn(28), u.celsius(15)),
    temperature=temperature,
)
print("Midspan sag at 1000 A:", sag)
