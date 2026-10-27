"""Build a line

Build a 230 kV H-frame line with Drake phases, Turkey shield wires, and a 300 m level span.
`height` places the structure datum 22 m above earth; it is not generally total tower height.
The phase wires hang 2.5 m below the frame's mounts. Calculate named phase matrices at
50 °C and 60 Hz. Results are per unit length; span length controls sag, not route length.
"""

from openline import Circuit, Earth, Line, Shield, Strung, conductors, electrical, structures
from openline import units as u

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

parameters = electrical.parameters(line, temperature=u.celsius(50), frequency=u.hz(60))
print("Phase impedance:")
print(parameters.impedance)
print("Phase admittance:")
print(parameters.admittance)
