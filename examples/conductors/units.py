"""Convert quantities

Read quantities in the units needed by your study. Drake's nominal 795 kcmil designation,
actual aluminum area, and total metal area including steel are distinct values. Complex
quantities use the same `.to(unit)` convention as scalar quantities.
"""

from openline import conductors, electrical
from openline import units as u

drake = conductors.astm.b232.DRAKE
print("Nominal designation:", drake.designation)
print(f"Outside diameter: {drake.diameter.to(u.inch):.3f} in")
print(f"Actual aluminum area: {drake.outer.area:.1f}")
print(f"Actual total metal area: {drake.area:.1f}")

impedance = electrical.internal_impedance(drake, temperature=u.celsius(75), frequency=u.hz(60))
print(f"Internal impedance: {impedance.to(u.ohm_per_mi):.4g} {u.symbol(u.ohm_per_mi)}")
