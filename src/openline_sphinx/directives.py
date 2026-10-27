"""Sphinx directives for catalog tables, specifications, examples, references, and validation."""

import ast
import hashlib
import os
import runpy
from contextlib import redirect_stdout
from importlib import import_module
from io import StringIO
from pathlib import Path
from types import ModuleType
from typing import ClassVar
from urllib.parse import urlparse

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import OptionSpec

import openline
from openline import _designs
from openline.types import Design

from . import depends, figures, plots, provenance, tables, validation
from .presentation import presenter
from .tables import Cell, facts, link, note, table, target

MONTHS = (  # as IEEE abbreviates them
    "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
)  # fmt: skip


class CatalogDirective(SphinxDirective):
    required_arguments = 1

    def module(self, reference: str) -> ModuleType:
        """A catalog module, its page depending on it and on the code alone."""
        if any(not part.isidentifier() or part.startswith("_") for part in reference.split(".")):
            raise self.error(f"Invalid catalog module: {reference!r}")
        try:
            module = import_module(f"{openline.__name__}.{reference}")
        except ImportError as exc:
            raise self.error(f"Cannot load catalog {reference!r}: {exc}") from exc
        depends.note(self.env, depends.source(reference))
        return module

    def design(self, reference: str) -> tuple[str, ModuleType, Design]:
        """A catalog design, its module's reference and its module."""
        module_ref, separator, name = reference.rpartition(".")
        if not separator or name.startswith("_"):
            raise self.error("Expected a reference such as conductors.astm.b232.DRAKE")
        module = self.module(module_ref)
        try:
            return module_ref, module, _designs.resolve(reference)
        except ValueError as error:
            raise self.error(str(error)) from error


class Catalog(CatalogDirective):
    """Render a catalog table. ``:links:`` requires specification pages for its designs."""

    option_spec: ClassVar[OptionSpec] = {"links": directives.flag}

    def run(self) -> list[nodes.Node]:
        reference = self.arguments[0]
        self.module(reference)
        listed = list(_designs.designs(reference).items())
        if not listed:
            raise self.error(f"No designs in catalog module {reference!r}")
        anchor = target([tables.label(reference)])
        self.state.document.note_explicit_target(anchor)
        found: list[nodes.Node] = [anchor]
        for grid in presenter(listed[0][1]).grids(listed):
            rows: list[list[Cell]] = []
            for name, given in grid.rows:
                cells: list[Cell] = list(given)
                if "links" in self.options:
                    cells[0] = link(given[0], f"{reference}.{name}", self.env.docname)
                rows.append(cells)
            made = table(grid.headers, rows, numeric=grid.numeric)
            if grid.title:
                made.insert(0, nodes.title(text=grid.title))
            found.append(made)
        return found


class Spec(CatalogDirective):
    """Render a specification with a shared target for all aliases, and the design's figures.

    ``:catalog:`` links the first field back to the catalog table.
    """

    option_spec: ClassVar[OptionSpec] = {"catalog": directives.flag}

    def run(self) -> list[nodes.Node]:
        reference = self.arguments[0]
        module_ref, module, value = self.design(reference)
        aliases = [
            tables.label(f"{module_ref}.{key}")
            for key, item in vars(module).items()
            if not key.startswith("_") and item is value
        ]
        anchor = target(aliases)
        self.state.document.note_explicit_target(anchor)

        body = nodes.container(classes=["openline-spec"])
        body += figures.request(self, reference)
        sheet = presenter(value).sheet(value)
        rows: list[tuple[str, Cell]] = list(sheet.facts)
        if "catalog" in self.options:
            rows[0] = (rows[0][0], link(str(rows[0][1]), module_ref, self.env.docname))
        body += facts(rows)
        for given in sheet.blocks:
            body += tables.block(given)
        return [anchor, body]


class Diagram(CatalogDirective):
    """A catalog design's figures alone: ``openline:diagram:: conductors.astm.b232.DRAKE``."""

    def run(self) -> list[nodes.Node]:
        reference = self.arguments[0]
        self.design(reference)
        found = figures.request(self, reference)
        if not found:
            raise self.error(f"No drawing for {reference}")
        return list(found)


class Example(SphinxDirective):
    """Display a script, what it prints, and the figures it draws. The path is relative to the
    page."""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        _, path = self.env.relfn2path(self.arguments[0], self.env.docname)
        depends.note(self.env, path)
        printed = StringIO()
        try:
            code = Path(path).read_text(encoding="utf-8")
            with redirect_stdout(printed), plots.drawing() as drawn:
                runpy.run_path(path, run_name="__main__")
        except Exception as error:
            raise self.error(f"{self.arguments[0]} failed: {error!r}") from error
        output = printed.getvalue().rstrip("\n")
        shown = example_code(without_docstring(code))
        shown.append(
            nodes.literal_block(output, output, language="none", classes=["openline-output"])
        )
        shown.append(
            nodes.paragraph(
                "",
                "",
                addnodes.download_reference(
                    "",
                    "Download complete example",
                    reftarget=self.arguments[0],
                ),
            )
        )
        if drawn:
            key = hashlib.sha256(f"{self.env.docname}:{path}".encode()).hexdigest()[:12]
            directory = Path(self.env.doctreedir) / "plots" / key
            directory.mkdir(parents=True, exist_ok=True)
            # A download's target is relative to its page: Sphinx reads a leading "/" as the
            # documentation's root, so an absolute path on POSIX would not be found.
            page = Path(self.env.srcdir, self.env.docname).parent
            for index, figure in enumerate(drawn, start=1):
                shown.append(
                    nodes.raw(
                        "", f'<figure class="openline-plot">{figure.svg}</figure>', format="html"
                    )
                )
                downloads = nodes.paragraph()
                for extension, content in (("svg", figure.svg.encode()), ("pdf", figure.pdf)):
                    artifact = directory / f"{Path(path).stem}-{index}.{extension}"
                    artifact.write_bytes(content)
                    if downloads.children:
                        downloads += nodes.Text(" · ")
                    downloads += addnodes.download_reference(
                        "",
                        extension.upper(),
                        reftarget=Path(os.path.relpath(artifact, page)).as_posix(),
                    )
                shown.append(downloads)
        return shown


def without_docstring(code: str) -> str:
    """A script's code after its docstring, which its page gives as prose."""
    module = ast.parse(code)
    if ast.get_docstring(module) is None:
        return code
    return "\n".join(code.splitlines()[module.body[0].end_lineno or 0 :])


def example_code(code: str) -> list[nodes.Node]:
    """Show calculation code, with optional Setup and Plot script regions collapsed in HTML.

    The complete script is always executed and available to download. Other builders retain
    every region as ordinary code. Markers are Python comments, not a second example source.
    """
    regions: list[tuple[str, list[str]]] = [("Calculation", [])]
    for line in code.splitlines():
        if line in ("# %% Setup", "# %% Calculation", "# %% Plot"):
            regions.append((line.removeprefix("# %% "), []))
        else:
            regions[-1][1].append(line)
    shown: list[nodes.Node] = []
    for name, lines in regions:
        text = "\n".join(lines).strip()
        if not text:
            continue
        if name != "Calculation":
            shown.append(nodes.raw("", f"<details><summary>{name}</summary>", format="html"))
        shown.append(
            nodes.literal_block(text, text, language="python", classes=["openline-example"])
        )
        if name != "Calculation":
            shown.append(nodes.raw("", "</details>", format="html"))
    return shown


class SourcesDirective(SphinxDirective):
    """Base directive for documents in ``openline_sources``."""

    def documents(self) -> tuple[provenance.Document, ...]:
        folder = self.config.openline_sources
        if not folder:
            raise self.error("Set openline_sources relative to the documentation source directory")
        root = (Path(self.env.srcdir) / folder).resolve()
        found = provenance.documents(root)
        if not found:
            raise self.error(f"No documents in {root}")
        depends.note(self.env, *(path for document in found for path in document.files))
        return found


class References(SourcesDirective):
    """List transcribed and cited documents in IEEE reference format."""

    def run(self) -> list[nodes.Node]:
        listing = nodes.enumerated_list(classes=["openline-references"])
        for document in self.documents():
            if document.used:
                listing += nodes.list_item("", nodes.paragraph("", "", *citation(document)))
        return [listing]


def citation(document: provenance.Document) -> list[nodes.Node]:
    """Format an IEEE reference with publication details or a web access date."""
    address = urlparse(document.url)
    if address.netloc == "doi.org":
        found: list[nodes.Node] = [nodes.Text("doi: "), web(document.url, address.path[1:])]
    else:
        found = [nodes.Text("[Online]. Available: "), web(document.url, address.netloc)]
    if document.published:
        (publication,) = document.published
        return [
            nodes.Text(f"{document.publisher}, "),
            nodes.emphasis(text=document.title),
            nodes.Text(f", {publication.designation}, {publication.year}. "),
            *found,
            nodes.Text("."),
        ]
    retrieved = document.retrieved
    accessed = f"{MONTHS[retrieved.month - 1]} {retrieved.day}, {retrieved.year}"
    return [
        nodes.Text(f"{document.publisher}, \u201c{document.title}.\u201d "),
        *found,
        nodes.Text(f". Accessed: {accessed}."),
    ]


def web(url: str, text: str) -> nodes.reference:
    """A link to a page on the web."""
    return nodes.reference("", text, refuri=url)


class Validation(SourcesDirective):
    """How near openline's calculations come to what listings print: each check summarized
    (``summary``), or the 95th percentile of each standard's differences (``standards``)."""

    option_spec: ClassVar[OptionSpec] = {
        "view": lambda text: directives.choice(text, ("summary", "standards"))
    }

    def run(self) -> list[nodes.Node]:
        found = compared(self.documents())
        if self.options.get("view", "summary") == "standards":
            return standards(found)
        return summary(found, self.env.docname)


_COMPARED: dict[tuple[tuple[str, int], ...], validation.Compared] = {}


def compared(found: tuple[provenance.Document, ...]) -> validation.Compared:
    """Every check's comparisons, calculated once for the documents as they stand."""
    stamp = tuple(sorted((str(p), p.stat().st_mtime_ns) for d in found for p in d.files))
    if stamp not in _COMPARED:
        _COMPARED.clear()
        _COMPARED[stamp] = validation.comparisons(found)
    return _COMPARED[stamp]


def reference(design: Design) -> str:
    """A catalog design's reference, its module and constant: ``conductors.astm.b232.DRAKE``."""
    module = _designs.path(type(design))
    return next(f"{module}.{n}" for n, d in _designs.designs(module).items() if d is design)


def percent(fraction: float) -> str:
    """A fraction as a percentage to two places: ``0.38``."""
    return f"{100 * fraction:.2f}"


def summary(found: validation.Compared, docname: str) -> list[nodes.Node]:
    """Each check: its comparisons, their median and 95th percentile, its bound, and the
    largest, linked to its conductor."""
    rows: list[list[Cell]] = []
    for check, comparisons in found:
        given = validation.summary(comparisons)
        worst = validation.largest(comparisons)
        largest: Cell = percent(given.largest)
        if worst.design is not None:  # the conductor's name on hover
            linked = link(percent(given.largest), reference(worst.design), docname)
            largest = nodes.abbreviation("", "", linked, explanation=worst.design.title)
        rows.append(
            [
                check.label,
                str(given.compared),
                signed(100 * given.median),
                percent(given.percentile),
                f"{100 * check.bound:.1f}",
                largest,
            ]
        )
    headers = [
        ("Value", ""),
        ("Compared", ""),
        ("Median", "%"),
        ("95th percentile", "%"),
        ("Bound", "%"),
        ("Largest", "%"),
    ]
    return [
        table(headers, rows, numeric={1, 2, 3, 4, 5}),
        note(
            "Relative difference: openline's ÷ the listing's\u2212 1; positive where openline's is "
            "higher. Construction compares the catalog's wires with each listing's; the rest, what "
            "openline calculates with what the listing reports. Largest links to its conductor. "
            "AC resistance, GMR and ampacity leave out cores that magnetize."
        ),
    ]


def standards(found: validation.Compared) -> list[nodes.Node]:
    """Each standard's 95th percentile of each value, its listings beneath, marked where it
    passes the value's bound."""
    rows: list[list[Cell]] = []
    for standard, row in validation.by_standard(found).items():
        cells: list[Cell] = [standard]
        for column, _ in validation.STANDARDS:
            if column not in row:
                cells.append("")
                continue
            given, bound = row[column]
            cell = nodes.inline()
            over = ["over"] if given.percentile > bound else []
            cell += nodes.inline(text=percent(given.percentile), classes=over)
            cell += nodes.inline(text=str(given.compared), classes=["count"])
            cells.append(cell)
        rows.append(cells)
    headers = [("Standard", ""), *((column, "%") for column, _ in validation.STANDARDS)]
    return [
        table(headers, rows, numeric=set(range(1, len(validation.STANDARDS) + 1))),
        note("95th percentile, listings beneath. Red: past the value's bound."),
    ]


def signed(percent: float) -> str:
    """A percentage to two places, with its sign: ``+0.26``; ``0.00`` where it rounds to none."""
    rounded = round(percent, 2)
    return f"{rounded:+.2f}" if rounded else "0.00"
