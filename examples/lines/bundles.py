"""Compare bundle counts

Compare one to four Drake conductors per phase on the west side of a 380 kV tower. This
configuration has no shield wires. The 25 kN tension applies to each subconductor.
ABC follows catalog attachment order on that side. Surge impedance loading uses line-to-line
voltage and the magnitude of positive-sequence characteristic impedance.
"""

import cmath

from openline import Bundle, Circuit, Earth, Line, Strung, conductors, electrical, structures
from openline import units as u

# %% Setup
drake = conductors.astm.b232.DRAKE
tower = structures.tower.D_2_D_2018_3_T1
west = [a for a in tower.phases if a.point.across < u.m(0)]
stringing = Strung(tension=u.kn(25), temperature=u.celsius(15))
voltage = u.kv(380)

# %% Calculation
for count in (1, 2, 3, 4):
    circuit = Circuit.uniform(
        Bundle(conductor=drake, count=count, spacing=u.m(0.4)),
        at=dict(zip("ABC", west, strict=True)),
        strung=stringing,
    )
    line = Line(
        structure=tower,
        height=u.m(32),
        span=u.m(400),
        circuits=(circuit,),
        shields=(),
        earth=Earth(resistivity=u.ohm_m(100), relative_permittivity=10),
    )
    sequence = (
        electrical.parameters(line, temperature=u.celsius(75), frequency=u.hz(60))
        .transposed()
        .sequence()
    )
    z1 = sequence.positive.impedance.to(u.ohm_per_m)
    y1 = sequence.positive.admittance.to(u.s_per_m)
    surge_ohms = abs(cmath.sqrt(z1 / y1))
    loading_mw = voltage.to(u.kv) ** 2 / surge_ohms
    print(
        f"{count} conductors/phase: {sequence.positive.impedance}; "
        f"|Zc|={surge_ohms:.1f} Ω; SIL={loading_mw:.0f} MW"
    )
