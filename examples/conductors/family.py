"""Compare candidate sizes

Compare ampacity and 60 Hz resistance for three ASTM B232 conductors with the same 26/7
construction, at 100 °C and the stated weather and surface conditions.
"""

from openline import Environment, Surface, conductors, electrical, ratings
from openline import units as u

# %% Setup
weather = Environment(
    air=u.celsius(40),
    wind=u.m_per_s(0.61),
    wind_angle=u.degrees(90),
    sun=u.w_per_m2(1000),
    elevation=u.m(0),
)
surface = Surface(emissivity=0.8, absorptivity=0.8)

# %% Calculation
catalog = conductors.astm.b232
for conductor in (catalog.GROSBEAK, catalog.STARLING, catalog.DRAKE):
    ampacity = ratings.ampacity(
        conductor,
        temperature=u.celsius(100),
        frequency=u.hz(60),
        environment=weather,
        surface=surface,
    )
    resistance = electrical.resistance(conductor, temperature=u.celsius(100), frequency=u.hz(60))
    print(f"{conductor.title}: {ampacity}; {resistance}")
