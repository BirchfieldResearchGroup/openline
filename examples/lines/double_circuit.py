"""Coupling between circuits

Build named west and east circuits with two Drake conductors per phase and Turkey shields.
ABC follows catalog attachment order on each side. The 25 kN stringing tension is per
subconductor. Select the mutual phase block by name, then transform the full six-phase model
to sequence coordinates, preserving coupling between circuits and sequences.
"""

from openline import (
    Bundle,
    Circuit,
    Earth,
    Line,
    Shield,
    Strung,
    conductors,
    electrical,
    structures,
)
from openline import units as u

# %% Setup
tower = structures.tower.D_2_D_2018_3_T1
drake = conductors.astm.b232.DRAKE
west = [a for a in tower.phases if a.point.across < u.m(0)]
east = [a for a in tower.phases if a.point.across > u.m(0)]
bundle = Bundle(conductor=drake, count=2, spacing=u.m(0.4))
stringing = Strung(tension=u.kn(25), temperature=u.celsius(15))

# %% Calculation
line = Line(
    structure=tower,
    height=u.m(32),
    span=u.m(400),
    circuits=tuple(
        Circuit.uniform(
            bundle,
            name=name,
            at=dict(zip("ABC", attachments, strict=True)),
            strung=stringing,
        )
        for name, attachments in {"west": west, "east": east}.items()
    ),
    shields=Shield.each(
        conductors.astm.b232.TURKEY,
        at=tower.shields,
        strung=Strung(u.kn(8), u.celsius(15)),
    ),
    earth=Earth(resistivity=u.ohm_m(100), relative_permittivity=10),
)
parameters = electrical.parameters(line, temperature=u.celsius(75), frequency=u.hz(60))
print("Mutual phase impedance:")
print(parameters.impedance.block(rows="west", columns="east"))
print("Zero-sequence mutual impedance:", parameters.sequence().impedance["west.0", "east.0"])
