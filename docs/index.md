---
myst:
  html_meta:
    description: "OpenLine is a Python library for overhead transmission lines: line impedance and admittance, conductor ampacity, sag and tension, with a catalog of conductors and structures from standards and manufacturers' documents."
---

# Start here

:::{container} lede
Model overhead transmission lines in Python.
:::

Calculate line impedance and admittance, conductor ampacity, sag, and tension.
The included catalog has conductor and structure data from standards and manufacturers.

```{figure} images/banner.webp
:figclass: home-banner
:alt: Bluebird conductor with four aluminum layers cut back to expose its steel core

{ref}`ACSR Bluebird <openline-conductors.astm.b232.bluebird>` · 2156 kcmil · 84/19 · ASTM B232
```

(install)=
## Quickstart

:::{container} quickstart
Python 3.12–3.14

```bash
pip install openline
```

```python
from openline import conductors, electrical, mechanical, units as u

drake = conductors.astm.b232.DRAKE
resistance = electrical.resistance(drake, temperature=u.celsius(75), frequency=u.hz(60))
print(resistance)  # 0.08559 Ω/km
print(mechanical.mass(drake))  # 1.63 kg/m
```
:::

:::{container} calculation-note
Calculations take a conductor's construction, its materials and its standard alone; the catalog
holds no reported values. {doc}`development/validation` compares each calculation with what
manufacturers and standards report.
:::

## Examples

:::{container} examples
{doc}`Inspect a conductor <examples/conductors/look_up>`
: Read diameter and mass from a specific catalog construction.

{doc}`Calculate resistance <examples/conductors/resistance>`
: Compare resistance at operating temperatures.

{doc}`Find ampacity <examples/ratings/rate>`
: Calculate ampacity, temperature, and sag for specified weather.

{doc}`Calculate sag and tension <examples/conductors/sag_tension>`
: See how temperature changes a level span.

{doc}`Build a line <examples/lines/build>`
: Calculate named phase and sequence parameters.

{doc}`Model an overload <examples/ratings/dynamic>`
: Calculate temperature through changes in load and wind.
:::

## Author

[Luke Lowery](https://lukelowry.github.io/), PhD student in the
[Birchfield Research Group](https://birchfield.engr.tamu.edu/) at Texas A&M University ·
[Google Scholar](https://scholar.google.com/citations?user=CTynuRMAAAAJ&hl=en) ·
[ORCID](https://orcid.org/0009-0000-0029-3403)

Also by the author: [pyvectorfit](https://github.com/BirchfieldResearchGroup/pyvectorfit), vector
fitting for EMT line models.

<nav class="project-links" aria-label="Project links">
  <a href="https://github.com/BirchfieldResearchGroup/openline">GitHub</a>
  <a href="https://pypi.org/project/openline/">PyPI</a>
  <a href="https://github.com/BirchfieldResearchGroup/openline/actions/workflows/ci.yml">CI</a>
  <a href="https://github.com/BirchfieldResearchGroup/openline/blob/main/LICENSE">MIT license</a>
</nav>

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:

Start here <self>
```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:
:caption: Examples

examples/conductors/index
examples/ratings/index
examples/lines/index
examples/emt/index
```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:
:caption: Catalog

conductors/index
structures/index
```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:
:caption: API

api/common/index
api/electrical/index
api/mechanical/index
```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:
:caption: Development

development/references
development/validation
```
