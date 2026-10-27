"""Temperature during an overload

Model 900 A for an hour, 1200 A for 40 minutes, then 600 A for an hour. Wind drops halfway
through the overload. Solar input is fixed. Output sampling does not change the solver's
time steps; every interval boundary and the initial temperature are included.
"""

from dataclasses import replace
from datetime import timedelta

import matplotlib.pyplot as plt

from openline import Environment, Interval, Surface, conductors, ratings
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

calm = replace(weather, wind=u.m_per_s(0.2))
initial = ratings.temperature(
    drake,
    current=u.amperes(900),
    frequency=u.hz(60),
    environment=weather,
    surface=surface,
)

# %% Calculation
schedule = [
    Interval(current=u.amperes(900), environment=weather, duration=timedelta(hours=1)),
    Interval(current=u.amperes(1200), environment=weather, duration=timedelta(minutes=20)),
    Interval(current=u.amperes(1200), environment=calm, duration=timedelta(minutes=20)),
    Interval(current=u.amperes(600), environment=weather, duration=timedelta(hours=1)),
]
profile = ratings.temperature_profile(
    drake,
    schedule,
    frequency=u.hz(60),
    surface=surface,
    initial_temperature=initial,
    sample_every=timedelta(minutes=1),
)
print("Peak sampled temperature:", max(profile.temperatures))
print("Final temperature:", profile.temperatures[-1])

# %% Plot
fig, ax = plt.subplots(num="Conductor temperature over the load and wind schedule")
ax.plot(
    [elapsed.total_seconds() / 60 for elapsed in profile.elapsed],
    [temperature.to(u.celsius) for temperature in profile.temperatures],
)
ax.set(xlabel="Elapsed time (min)", ylabel="Conductor temperature (°C)", xlim=(0, 160))
ax.text(2, 0.97, "900 A", transform=ax.get_xaxis_transform(), va="top", fontsize=9)
for minute, label in ((60, "1200 A"), (80, "Low wind"), (100, "600 A\nWind restored")):
    ax.axvline(minute, color="#777777", linewidth=0.6, linestyle=":")
    ax.text(
        90 if minute == 80 else minute + 2,
        0.97,
        label,
        transform=ax.get_xaxis_transform(),
        ha="center" if minute == 80 else "left",
        va="top",
        fontsize=9,
    )
ax.set_ylim(top=160)
plt.show()
