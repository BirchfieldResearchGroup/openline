"""Inspect material assumptions

Inspect the resistivity and density used for Drake's aluminum wires and steel core. This is
a reference example for understanding the material inputs to a calculation.
"""

from openline import conductors, electrical
from openline import units as u

drake = conductors.astm.b232.DRAKE
for part, strand in drake.parts:
    resistivity = electrical.resistivity(strand.material, temperature=u.celsius(75))
    print(f"{part}: resistivity at 75 °C = {resistivity}; density = {strand.material.density}")
