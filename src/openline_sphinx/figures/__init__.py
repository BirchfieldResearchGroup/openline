"""A design's figures: a conductor's construction and cross section, a structure's elevations.
A page's doctree holds each figure's reference alone; the figure is drawn as inline SVG when the
page is written, the designs it draws kept for the next few figures and no longer."""

import hashlib
from functools import lru_cache
from html import escape
from typing import Any

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

from openline import _designs

from ..presentation import Figure, presenter
from . import selection


class FigureNode(nodes.General, nodes.Element):
    """A design's figure, by its reference and its place among the design's figures."""


@lru_cache(maxsize=8)
def figures(reference: str) -> tuple[Figure, ...]:
    """A design's figures, drawn as a page asks for them; a page asks for one design's."""
    design = _designs.resolve(reference)
    return presenter(design).figures(design)


def request(directive: SphinxDirective, reference: str) -> list[FigureNode]:
    """A node for each of a design's figures."""
    title = _designs.resolve(reference).title
    found = []
    for view, figure in enumerate(figures(reference)):
        serial = directive.env.new_serialno("openline-figure")
        occurrence = hashlib.sha256(f"{directive.env.docname}#{serial}".encode()).hexdigest()[:12]
        found.append(
            FigureNode(
                reference=reference,
                view=view,
                heading=figure.heading,
                title=title,
                occurrence=occurrence,
            )
        )
    return found


def visit_html(writer: Any, node: FigureNode) -> None:
    figure = figures(node["reference"])[node["view"]]
    occurrence = f"ol-{node['occurrence']}-"
    toggle = (
        '<button type="button" class="ol-dimensions-toggle" hidden>Dimensions</button>'
        if figure.dimensioned
        else ""
    )
    writer.body.append(
        f'<figure class="openline-figure" aria-labelledby="{occurrence}heading">'
        f'<div class="ol-figure-heading"><h2 id="{occurrence}heading">'
        f"{escape(figure.heading)}</h2>{toggle}</div>"
        f"{figure.svg(interactive=True, occurrence=occurrence)}"
        '<span class="ol-selection-status" role="status" aria-live="polite"></span></figure>'
    )
    raise nodes.SkipNode


def named(app: Sphinx, doctree: nodes.document, _docname: str) -> None:
    """Outside HTML, a figure is named, not drawn."""
    if app.builder.format != "html":
        for node in list(doctree.findall(FigureNode)):
            node.replace_self(nodes.paragraph(text=f"{node['heading']}: {node['title']}"))


def setup(app: Sphinx) -> None:
    selection.setup(app)
    app.connect("doctree-resolved", named)
    app.add_node(FigureNode, html=(visit_html, None))
    app.add_js_file("figures.js", loading_method="defer")
    app.add_css_file("figures.css", priority=510)
