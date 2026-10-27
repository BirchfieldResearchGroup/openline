"""Select by resistance

Find the smallest actual metal cross-section among ASTM B232 26/7 conductors with DC
resistance below 0.078 Ω/km at 20 °C. Missing calculation data raises an error rather than
silently removing a candidate.
"""

from openline import conductors, electrical
from openline import units as u
from openline.types.conductors.astm import B232

candidates = (
    conductor
    for conductor in conductors.of(B232)
    if conductor.wire_counts == (26, 7)
    and electrical.resistance(conductor, temperature=u.celsius(20), frequency=u.hz(0))
    < u.ohm_per_km(0.078)
)
selected = min(candidates, key=lambda conductor: conductor.area, default=None)
print(selected.title if selected is not None else "No matching conductor")
