"""Sequence parameters

Calculate positive- and zero-sequence parameters for one ideally transposed ABC circuit.
`.transposed()` applies ideal phase averaging; `.sequence()` alone only changes coordinates
and retains all sequence coupling. Diagonal conveniences such as `.positive` do not imply
that the off-diagonal entries vanish. The full matrices remain accessible.
"""

from openline import Circuit, Earth, Line, Shield, Strung, conductors, electrical, structures
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
parameters = electrical.parameters(line, temperature=u.celsius(50), frequency=u.hz(60))
sequence = parameters.transposed().sequence()
print("Positive-sequence impedance:", sequence.positive.impedance)
print("Zero-sequence impedance:", sequence.zero.impedance)
print("Positive-sequence admittance:", sequence.positive.admittance)
