"""Resistance at operating temperature

Calculate Drake's 60 Hz resistance at several conductor temperatures. Use `frequency=u.hz(0)`
for DC. Resistance is per unit length; multiply by route length in compatible units for a total.
"""

from openline import conductors, electrical
from openline import units as u

drake = conductors.astm.b232.DRAKE
print("Temperature (°C)  AC resistance (Ω/km)")
for degrees in (20, 50, 75, 100):
    resistance = electrical.resistance(drake, temperature=u.celsius(degrees), frequency=u.hz(60))
    print(f"{degrees:15}  {resistance.to(u.ohm_per_km):.5f}")
