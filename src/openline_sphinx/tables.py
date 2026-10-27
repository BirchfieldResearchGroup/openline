"""Tables, specification fields, and links built from standard Sphinx nodes."""

from collections.abc import Container, Iterable, Sequence
from itertools import accumulate
from typing import NamedTuple

from docutils import nodes
from sphinx import addnodes

from .figures.selection import Selection
from .presentation import Block, Header

type Cell = str | nodes.Element


def label(reference: str) -> str:
    """A catalog's or specification's label: ``openline-conductors.astm.b232``."""
    return f"openline-{reference.casefold()}"


def target(names: Sequence[str]) -> nodes.target:
    return nodes.target("", "", ids=[nodes.make_id(names[0])], names=list(names))


def link(text: str, reference: str, docname: str) -> addnodes.pending_xref:
    """A link to a catalog table or specification by its reference: ``conductors.astm.b232``."""
    return addnodes.pending_xref(
        "",
        nodes.inline(text=text),
        refdomain="std",
        reftype="ref",
        reftarget=label(reference),
        refexplicit=True,
        refwarn=True,
        refdoc=docname,
    )


def paragraph(value: Cell) -> nodes.paragraph:
    return nodes.paragraph(text=value) if isinstance(value, str) else nodes.paragraph("", "", value)


def heading(title: str, unit: str) -> nodes.inline:
    """A column's header: its title, and its unit beneath, or a blank line where it has
    none, so that every title of a table with units stands on the same line."""
    result = nodes.inline(text=title)
    result += nodes.inline(text=unit or "\N{NO-BREAK SPACE}", classes=["unit"])
    return result


class Row(NamedTuple):
    """A row and its classes: ``depth-2`` in a tree of rows. A row of fewer cells than its table
    has columns spans the rest with its last."""

    cells: Sequence[Cell]
    classes: tuple[str, ...] = ()


def table(
    headers: Sequence[Header],
    rows: Iterable[Row | Sequence[Cell]],
    *,
    numeric: Container[int] = (),
    groups: Sequence[tuple[str, int]] = (),
) -> nodes.table:
    """A table under one row of headers: each title on one line, and its unit beneath where
    any column has one. ``groups`` heads each run of the columns after the first above them, by
    its title and how many columns it takes."""
    units = any(unit for _, unit in headers)
    opens = set(accumulate((count for _, count in groups[:-1]), initial=1)) if groups else set()
    result = nodes.table(classes=["openline-table"])
    tgroup = nodes.tgroup(cols=len(headers))
    result += tgroup
    for index in range(len(headers)):
        tgroup += nodes.colspec(colwidth=1, stub=index == 0)

    def entry(value: Cell, index: int, span: int = 0) -> nodes.entry:
        classes = ["number"] * (index in numeric and not span) + ["opens"] * (index in opens)
        result = nodes.entry("", paragraph(value), classes=classes)
        if span:
            result["morecols"] = span
        return result

    def row(given: Row | Sequence[Cell]) -> nodes.row:
        cells, classes = (given.cells, given.classes) if isinstance(given, Row) else (given, ())
        result = nodes.row(classes=list(classes))
        for index, value in enumerate(cells):
            last = index == len(cells) - 1
            result += entry(value, index, len(headers) - len(cells) if last else 0)
        return result

    head, body = nodes.thead(), nodes.tbody()
    if groups:
        above = nodes.row(classes=["groups"])
        above += nodes.entry("", paragraph(""))
        for title, count in groups:
            above += nodes.entry("", paragraph(title), morecols=count - 1, classes=["group"])
        head += above
    head += row([heading(title, unit) if units else title for title, unit in headers])
    for values in rows:
        body += row(values)
    tgroup += head
    tgroup += body
    return result


def block(given: Block) -> nodes.table:
    """A specification's table, under its caption."""
    rows: list[list[Cell]] = [list(row) for row in given.rows]
    if given.keys:
        for row, key in zip(rows, given.keys, strict=True):
            row[0] = Selection(text=str(row[0]), key=key)
    result = table(given.headers, rows, numeric=given.numeric)
    result.insert(0, nodes.title(text=given.title))
    return result


def note(text: str) -> nodes.paragraph:
    """A note under a table."""
    return nodes.paragraph(text=text, classes=["openline-note"])


def facts(rows: Iterable[tuple[str, Cell]]) -> nodes.definition_list:
    result = nodes.definition_list(classes=["openline-facts"])
    for name, value in rows:
        result += nodes.definition_list_item(
            "", nodes.term(text=name), nodes.definition("", paragraph(value))
        )
    return result
