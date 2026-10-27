"""Sphinx extension for OpenLine catalogs, API references, examples, and diagrams.

See this package's README for directives, configuration, and rendering dependencies."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Sphinx is imported in setup alone: provenance and validation need none
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata


def setup(app: "Sphinx") -> "ExtensionMetadata":
    from . import api, depends, figures, navigation, pages
    from .domain import OpenLineDomain
    from .style import configure

    app.require_sphinx("9.0")
    app.add_domain(OpenLineDomain)
    api.setup(app)
    figures.setup(app)
    navigation.setup(app)
    pages.setup(app)
    app.connect("builder-inited", depends.renew)
    app.add_config_value("openline_sources", "", "env", types=frozenset({str}))
    app.connect("config-inited", configure)
    app.add_css_file("openline.css", priority=500)
    return {
        "version": "0.1",
        "env_version": 12,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
