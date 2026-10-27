"""Find attachment heights

Find the lowest phase attachment at each available tower datum height. These are support
coordinates; they are not the conductor's minimum clearance over a span.
"""

from openline import structures
from openline.types.structures.attachments import Wire

tower = structures.tower.D_2_D_2018_3_T1
for height in tower.datum.heights:
    lowest = min(
        attachment.point.height for attachment in tower.at(height) if attachment.wire is Wire.PHASE
    )
    print(f"Datum at {height}: lowest phase attachment at {lowest}")
