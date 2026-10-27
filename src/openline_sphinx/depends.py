"""What a page depends on: its own files, and one stamp for the code that writes every page. The
stamp is renewed when what openline's or this extension's Python does changes, and only then: not
for a docstring, a comment or layout, which no page holding it shows. A page holds two
dependencies, not one for each module of the code."""

import ast
import hashlib
from importlib import import_module
from inspect import getfile
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

import openline

STAMP = "openline-code.sha256"
DATA = ("conductors", "structures")  # openline's catalog: a page depends on its own module


def code() -> list[Path]:
    """The code that writes a page: openline's but its catalog, and this extension's Python; its
    styles, scripts and fonts are copied beside the pages."""
    package, extension = Path(getfile(openline)).parent, Path(__file__).parent
    found = [
        path
        for path in sorted(package.rglob("*.py"))
        if path.relative_to(package).parts[0] not in DATA
    ]
    return found + sorted(extension.rglob("*.py"))


def syntax(path: Path) -> str:
    """A module's syntax without its docstrings. The API pages, which show docstrings, depend on
    their modules' files instead."""
    tree = ast.parse(path.read_bytes())
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list):
            body[:] = [each for each in body if not docstring(each)]
    return ast.dump(tree)


def docstring(node: ast.AST) -> bool:
    """Whether a statement is a string alone: a docstring, or an attribute's."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def renew(app: Sphinx) -> None:
    """Write the stamp where its digest of the code changed: pages depending on it rebuild."""
    digest = hashlib.sha256()
    for path in code():
        digest.update(path.name.encode())
        digest.update(syntax(path).encode())
    stamp = Path(app.doctreedir) / STAMP
    if not stamp.exists() or stamp.read_text(encoding="utf-8") != digest.hexdigest():
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text(digest.hexdigest(), encoding="utf-8")


def note(env: BuildEnvironment, *paths: str | Path) -> None:
    """Note a page's dependencies: the code's stamp, and its own files."""
    env.note_dependency(str(Path(env.doctreedir) / STAMP))
    for path in paths:
        env.note_dependency(str(path))


def source(module: str) -> str:
    """The file of a catalog module, within openline: ``conductors.astm.b232``."""
    return getfile(import_module(f"{openline.__name__}.{module}"))
