"""Temperature, sag, and impedance

Calculate how conductor temperature changes sag and phase-A self impedance. Sag is measured
below the support position, not as clearance above terrain. The line calculation applies the
supplied temperature to phase and shield-wire sag.
"""

from openline import (
    Circuit,
    Earth,
    Line,
    Shield,
    Strung,
    conductors,
    electrical,
    mechanical,
    structures,
)
from openline import units as u

# %% Setup
drake = conductors.astm.b232.DRAKE
frame = structures.frame.TH_230
stringing = Strung(tension=u.kn(28), temperature=u.celsius(15))
line = Line(
    structure=frame,
    height=u.m(22),
    span=u.m(300),
    circuits=(
        Circuit.uniform(
            drake,
            at=dict(zip("ABC", frame.phases, strict=True)),
            strung=stringing,
            insulator_drop=u.m(2.5),
        ),
    ),
    shields=Shield.each(
        conductors.astm.b232.TURKEY,
        at=frame.shields,
        strung=Strung(u.kn(8), u.celsius(15)),
    ),
    earth=Earth(resistivity=u.ohm_m(100), relative_permittivity=10),
)

# %% Calculation
for degrees in (15, 75, 150):
    temperature = u.celsius(degrees)
    sag = mechanical.sag(drake, span=line.span, strung=stringing, temperature=temperature)
    impedance = electrical.impedance(line, temperature=temperature, frequency=u.hz(60))
    print(f"{degrees} °C: sag={sag}; phase-A self impedance={impedance['main.A', 'main.A']}")
