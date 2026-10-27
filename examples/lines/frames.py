"""Find frames by nominal voltage

Find frames whose catalog metadata lists 230 kV. This lookup does not establish structural
suitability or electrical clearance for a proposed installation.
"""

from openline import structures
from openline import units as u
from openline.types.structures import Frame

for frame in structures.of(Frame):
    if u.kv(230) in frame.voltages:
        print(f"{frame.title}: {frame.material.__name__}")
