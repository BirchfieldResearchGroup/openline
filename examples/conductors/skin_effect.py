"""Frequency, resistance, and GMR

Compare Drake's AC/DC resistance ratio and geometric mean radius at 75 °C from 10 Hz to 1 MHz.
The present conductor model uses fixed material permeability, independent of current.
"""

from openline import conductors, electrical
from openline import units as u

drake = conductors.astm.b232.DRAKE
temperature = u.celsius(75)
dc = electrical.resistance(drake, temperature=temperature, frequency=u.hz(0))

print("Frequency (Hz)  AC/DC resistance  GMR (mm)")
for frequency in (10, 60, 1_000, 10_000, 100_000, 1_000_000):
    ac = electrical.resistance(drake, temperature=temperature, frequency=u.hz(frequency))
    gmr = electrical.gmr(drake, temperature=temperature, frequency=u.hz(frequency))
    print(f"{frequency:14}  {ac / dc:16.3f}  {gmr.to(u.mm):8.3f}")
