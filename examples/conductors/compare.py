"""Which Drake?

A code word can identify different constructions in different standards. Compare their
standard, designation, wire shape, and wire counts before choosing one for a calculation.
"""

from openline import conductors

for conductor in conductors.named("drake"):
    construction = ", ".join(
        f"{strand.count} {type(strand).__name__.lower()} wires" for strand in conductor.strands
    )
    print(f"{conductor.title}: {construction}")
