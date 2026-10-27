"""Compare earth-return assumptions

Isolate the earth-return contribution for a wire 20 m above earth. Compare soil resistivity,
relative permittivity, and frequency. Relative permittivity 1 recovers the conduction-only
series model; it does not disable finite-earth corrections in shunt calculations.
"""

from openline import Earth, conductors
from openline import units as u
from openline.electrical import series
from openline.types.lines import Placed
from openline.types.structures.geometry import Point

wire = Placed(conductors.astm.b232.DRAKE.diameter / 2, Point(u.m(0), u.m(0), u.m(20)))
print("Soil (Ω·m), relative permittivity, frequency (Hz), earth return (Ω/km)")
for resistivity in (10, 100, 1000):
    for permittivity in (1, 10):
        earth = Earth(resistivity=u.ohm_m(resistivity), relative_permittivity=permittivity)
        for frequency in (60, 1_000, 100_000, 1_000_000):
            impedance = series.earth(wire, wire, frequency=u.hz(frequency), earth=earth)
            print(f"{resistivity}, {permittivity}, {frequency}, {impedance.to(u.ohm_per_km):.4g}")
