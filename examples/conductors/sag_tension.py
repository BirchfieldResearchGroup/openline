"""Sag and tension as temperature changes

Calculate midspan sag and horizontal tension for Drake across a 300 m level span. The stated
28 kN stringing condition at 15 °C includes creep; this example does not model ice or wind loading.
"""

from openline import Strung, conductors, mechanical
from openline import units as u

drake = conductors.astm.b232.DRAKE
span = u.m(300)
stringing = Strung(tension=u.kn(28), temperature=u.celsius(15))

print("Temperature (°C)  Sag (m)  Horizontal tension (kN)")
for degrees in (-20, 15, 75, 100, 150):
    temperature = u.celsius(degrees)
    sag = mechanical.sag(drake, span=span, strung=stringing, temperature=temperature)
    tension = mechanical.tension(drake, span=span, strung=stringing, temperature=temperature)
    print(f"{degrees:15}  {sag.to(u.m):7.2f}  {tension.to(u.kn):23.2f}")
