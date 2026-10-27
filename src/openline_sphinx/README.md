# OpenLine Sphinx

Catalog tables, specifications, figures, API references, and source citations for OpenLine.
The documentation's own, kept in the repository and not shipped with openline: the `docs`
dependency group installs Sphinx 9, Furo and MyST, and an editable install of the repository
makes the extension importable.

```python
# docs/conf.py
extensions = ["myst_parser", "openline_sphinx"]
autodoc_typehints = "none"
html_theme = "furo"
exclude_patterns = ["_build"]
openline_sources = "../sources"
```

## Directives

````markdown
# Drake

```{openline:spec} conductors.astm.b232.DRAKE
:catalog:
```

```{openline:diagram} structures.tower.D_2_D_2018_3_T1
```

```{openline:catalog} conductors.astm.b232
:links:
```

```{openline:api} openline.types.structures
```

```{openline:materials}
```

```{openline:units}
```

```{openline:standards}
```

```{openline:example} ../examples/conductors/sag_tension.py
```

```{openline:references}
```

```{openline:validation}
```
````

Catalog references are module paths such as `conductors.astm.b232` or `structures.tower`.
Specifications append a constant name. Catalogs define Sphinx labels such as
`openline-conductors.astm.b232`; specifications define labels for every exported alias,
including `openline-conductors.astm.b232.drake`. Define each target once.

`:links:` links catalog rows to specifications. `:catalog:` links a specification back to
its catalog. Include the target pages before enabling these options. Specification pages
can use MyST's `orphan: true` to remain searchable without appearing in the sidebar.

`openline:example` runs a script and displays its code, what it prints, and each figure it
leaves open in matplotlib, as inline SVG in the page's colors, light or dark; paths are
relative to the page. Without matplotlib, figures are skipped. `openline:api` uses autodoc in
source order, with tables for dataclass fields, enum members, class variables, and conductor
stranding rules. `openline:materials` tabulates every material beneath the one it derives from,
a metal's properties grouped electrical, thermal and mechanical, those it inherits dimmed;
`openline:units` tabulates every unit, by its symbol, under the SI unit it measures in and the
quantities measured in it (`reference.py`). Each row is the target of links to its class or
function, and what a table does not hold follows as `openline:api` documents it.
`openline:standards` tabulates every standard the catalog lists conductors to, under the body
that writes it, each row linking to its class's entry and its catalog table.

References and validation read `openline_sources`, relative to the documentation source
directory; `provenance.py` reads them, and documents their layout. References use IEEE format.
Each row, a listing, names its catalog design. `listings.py` reads what it gives: its wires,
which must be its design's, and its `reported` columns, which the catalog holds none of.
`validation.py` compares the wires with the catalog's, and what the row reports with what
openline calculates of its design at the conditions its document states, reporting relative
differences as a signed median, 95th percentile magnitude, and maximum magnitude.

## Presentation

The extension takes every fact from openline: a material's `name`, a conductor's `family`,
`parts` and `layers`, a structure's `parts`, and designs by reference from
`openline._designs`. It holds no names or tables of its own.

`quantities.py` defines what the catalog tabulates of a conductor and the validation compares:
diameter, area, mass and DC resistance at 20 °C, each calculated once a design, a dash where
openline lacks what it takes. `presentation/conductors.py` and `presentation/structures.py`
define catalog columns, specification fields and figures; `tables.py` converts them into
standard Sphinx nodes.

A standard's conductors take a table for each way they are named: by code word first, then by
size in kcmil, in mm², by AWG gauge, code number or wire gauge; each by size and then area, as
standards' tables order them, aliases once. Specifications give a conductor's
wires by part, its layers from the outside in with their lay and hand, and its rated strength
by core grade where its standard leaves the grade open. Structure tables sort by name;
specifications give geometry, attachments and documented parts.

The extension supports HTML, text, and LaTeX writers. A page depends on its own files and on
one stamp for the code that writes every page (`depends.py`), renewed only when what openline's
or the extension's Python does changes, not its docstrings, comments or layout: editing a
catalog module rebuilds its pages alone. An orphan page, as each specification, shows the
sidebar's top level alone, every orphan in a folder the same, resolved once (`navigation.py`). Outside HTML, a figure is named rather than
drawn. HTML uses bundled styles and licensed Inter fonts.
Override colors with Furo's `light_css_variables` and `dark_css_variables`, and logos with
Sphinx's `html_logo` / `html_favicon` or Furo's `light_logo` / `dark_logo`. LaTeX output
requires a TeX installation to compile to PDF.

## Repository documentation

```console
python -m sphinx -W --keep-going -j auto -b html docs docs/_build/html
```

`-j auto` builds in parallel on Linux and macOS; Sphinx builds serially on Windows.

Edit the homepage, API, and development Markdown in `docs/`; `docs/conf.py` holds settings
alone. `pages.py` generates the rest at each build, into trees ignored by Git and the
generator's alone: `openline_catalog = True` writes a page per catalog module, and one per
design, into `docs/conductors/` (by family, then standard) and `docs/structures/`;
`openline_examples = "../examples"` writes `docs/examples/`, a page per script, from its
docstring, and an index per group, from the group's `README.md`. Nothing is declared there: a
new module or script has its pages. The generator checks that each module lists designs of one
class before writing, rewrites only changed pages, and removes every other file in its trees.

The homepage's hidden toctrees define navigation: Examples, Catalog (the generated
`conductors/index` and `structures/index`), API and Development, every page titled with a
capital. `docs/images/banner.webp` is a fixed image.

## Figures

Every specification opens on its design's figures: a conductor's construction and its cross
section, or a structure's elevations. `openline:diagram` draws them alone. Each is one vector
SVG, written inline into the page as it is built and scaled to any width; it needs nothing
beyond Sphinx. A doctree holds a figure's reference only.

- `figures/section.py`: each wire a disc where openline lays it (`Conductor.layers`). Wires
  openline cannot lay, as trapezoidal ones, fill a ring of their area; no layers are guessed.
- `figures/cutback.py`: the conductor from the side, each layer cut back from the one within
  it, every wire turning at its layer's radius, lay and hand. A wire's near half turn is drawn
  once for its layer and placed at each pass; a band of trapezoidal wires shows its outside,
  closed, each wire a ribbon between its seams. Drawn where openline has every ring's lay and
  hand.
- `figures/elevation.py`: a structure's front and side, at one scale, from its parts and
  points. Nominal ground follows a ground datum or the lowest tower legs; upper-only pole and
  frame drawings do not invent an installation height.
- `figures/svg.py`: the svg element, its title and description, numbers and dimensions.
- `figures/metals.py`: a part's classes, from its material's class and its bases
  (`ol-Aluminum1350H19 ol-HardDrawnAluminum ol-Aluminum ol-Metal`), and its shading.

`assets/figures.css` owns every color: its metal tokens (`--ol-aluminum`, `--ol-alloy`,
`--ol-steel`, `--ol-copper`) for light and dark, applied through those classes from the most
general to the most specific, and the figure surface, type, responsive and print rules.
`assets/figures.js` links a specification's figures and table rows by `data-ol-key`, keeps
labels a constant size on screen, and toggles dimensions. Hover or focus selects a part or an
attachment; arrow keys move among them, click pins a selection, and Escape clears it. Static
drawings, `svg(interactive=False, ...)`, keep their labels and dimensions without controls.
