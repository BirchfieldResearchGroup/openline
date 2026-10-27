"""Inspect a conductor

Look up a specific catalog construction and read its outside diameter and calculated mass.
Use `print(drake)` when you need the full construction record.
"""

from openline import conductors, mechanical

drake = conductors.astm.b232.DRAKE
print(drake.title)
print("Diameter:", drake.diameter)
print("Mass:", mechanical.mass(drake))
