"""A table cell that selects the same point in its specification's diagram."""

from html import escape
from typing import Any

from docutils import nodes
from sphinx.application import Sphinx


class Selection(nodes.Inline, nodes.TextElement):
    """A point label; the figure controller adds its button when a diagram is present."""


def visit_html(writer: Any, node: Selection) -> None:
    writer.body.append(
        f'<span class="ol-selection" data-ol-key="{escape(node["key"], quote=True)}">'
    )


def depart_html(writer: Any, _node: Selection) -> None:
    writer.body.append("</span>")


def text(_writer: Any, _node: Selection) -> None:
    pass


def setup(app: Sphinx) -> None:
    app.add_node(
        Selection,
        html=(visit_html, depart_html),
        latex=(text, text),
        text=(text, text),
        man=(text, text),
        texinfo=(text, text),
    )
