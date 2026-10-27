"""An orphan's sidebar. An orphan, such as a specification, is in no toctree, so no branch of the
sidebar is its own: it shows the top level alone, and every orphan in a folder the same, resolved
once for the folder."""

from posixpath import dirname
from typing import Any

from sphinx.application import Sphinx


def setup(app: Sphinx) -> None:
    resolved: dict[tuple[str, tuple[tuple[str, Any], ...]], str] = {}

    def shared(
        app: Sphinx, page: str, _template: str, context: dict[str, Any], _doctree: Any
    ) -> None:
        toctree = context.get("toctree")
        if toctree is None or "orphan" not in app.env.metadata.get(page, {}):
            return
        folder = dirname(page)

        def once(**options: Any) -> str:
            options["collapse"] = True  # no branch is an orphan's: the top level alone
            key = (folder, tuple(sorted(options.items())))
            if key not in resolved:
                resolved[key] = toctree(**options)
            return resolved[key]

        context["toctree"] = once

    app.connect("html-page-context", shared, priority=400)  # before the theme draws it, at 500
