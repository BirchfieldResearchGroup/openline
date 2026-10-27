"""PSRC benchmark

Compare relative errors against the IEEE PSRC 230 kV line's ATP results for 60 Hz, 50 Ω·m
soil, and 15 miles. Preserve the benchmark's stated diameter, mean heights, full Carson
series term, and perfect-earth capacitance. Self impedances are excluded because ATP uses
a solid conductor for this benchmark.
"""

import numpy as np

from openline import Earth
from openline import units as u
from openline.electrical import series, shunt
from openline.types.lines import Placed
from openline.types.structures.geometry import Point

# %% Setup
# PSRC table 4: tower and midspan heights (ft); appendix B.7: 15-mile mutual R/X/C.
heights = ((100.0, 73.0), (83.5, 56.5), (67.0, 40.0))
atp = {
    ("a", "b"): (1.32550570, 8.82314492, -0.0454680689),
    ("a", "c"): (1.33607442, 7.54892738, -0.0215476823),
    ("b", "c"): (1.34686707, 8.79786722, -0.0413213989),
}
length_m = u.mi(15).to(u.m)
radius = u.inch(1.216) / 2  # The benchmark's stated Marigold diameter.
earth = Earth(resistivity=u.ohm_m(50), relative_permittivity=1)
wires = {
    phase: Placed(radius, Point(u.m(0), u.m(0), u.ft(top - 2 / 3 * (top - middle))))
    for phase, (top, middle) in zip("abc", heights, strict=True)
}

# %% Calculation
# Preserve the benchmark's perfect-earth capacitance model.
potential = np.array(
    [[shunt.external(a, b).to(u.m_per_f).real for b in wires.values()] for a in wires.values()]
)
capacitance_uf = np.linalg.inv(potential) * length_m * 1e6
print("Pair  Resistance error (%)  Reactance error (%)  Capacitance error (%)")
for (i, k), (reference_r, reference_x, reference_c) in atp.items():
    a, b = wires[i], wires[k]
    air = series.external(a, b, frequency=u.hz(60))
    returned = series.earth(a, b, frequency=u.hz(60), earth=earth)
    impedance = (air.to(u.ohm_per_m) + returned.to(u.ohm_per_m)) * length_m
    capacitance = capacitance_uf["abc".index(i), "abc".index(k)]
    print(
        f"{i}{k}  {100 * (impedance.real / reference_r - 1):+.3f}  "
        f"{100 * (impedance.imag / reference_x - 1):+.3f}  "
        f"{100 * (capacitance / reference_c - 1):+.3f}"
    )
