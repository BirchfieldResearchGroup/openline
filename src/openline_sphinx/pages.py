"""The documentation's generated pages, each tree the generator's alone and ignored by Git.

``openline_catalog`` writes ``conductors/`` and ``structures/`` from the catalog's own modules:
a page per module, a standard of conductors or a family of structures, holding its catalog table
and titled by its class's name; a family of conductors lists its standards, and each tree's index
its families. Each design has its specification page.

``openline_examples``, a folder of example scripts relative to the documentation source, writes
``examples/``: a page per script, titled and introduced by its docstring, and an index per group,
whose ``README.md`` gives its title and its scripts in order; a script's line in it is the first
sentence of its introduction.

Each page but an index says what it is in its front matter's ``myst.html_meta`` description, the
snippet a search engine shows of it. Nothing is declared here: a new module or script has its
pages."""

import ast
import json
import os
import re
from collections import defaultdict
from pathlib import Path

from sphinx.application import Sphinx

from openline import _designs
from openline.types import Design
from openline.types.conductors import Conductor

from .figures.section import wire
from .presentation import presenter
from .presentation.conductors import caption, size, stranding


def catalogs(collection: str) -> dict[str, tuple[type[Design], dict[str, Design]]]:
    """Each catalog module of a collection: its designs' class, and its designs by name."""
    found = {}
    for module in _designs.modules(collection):
        listed = _designs.designs(module)
        kinds = {type(design) for design in listed.values()}
        if len(kinds) != 1:
            raise ValueError(f"Catalog {module} must list designs of one class")
        found[module] = (kinds.pop(), listed)
    return found


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def described(description: str, orphan: bool = False) -> str:
    """A page's front matter: its description, and whether no toctree holds it."""
    return (
        "---\n"
        + ("orphan: true\n" if orphan else "")
        + f"myst:\n  html_meta:\n    description: {json.dumps(description, ensure_ascii=False)}\n"
        + "---\n\n"
    )


def named(design: Design) -> tuple[str, list[str]]:
    """A design's title, and what tells it from others of that title: a conductor's family and
    name, then its size where its name is not, its stranding and its standard; a structure's
    title alone."""
    if isinstance(design, Conductor):
        sized = [size(design.designation)] if design.code_words else []
        return caption(design), [*sized, stranding(design), design.standard]
    return design.title, []


def summary(design: Design) -> str:
    """What a design is, beyond its title: a conductor's wires, as its figures name them, or a
    structure's facts."""
    if isinstance(design, Conductor):
        return "; ".join(f"{part.capitalize()}: {wire(strand)}" for part, strand in design.parts)
    return "; ".join(f"{label}: {value}" for label, value in presenter(design).sheet(design).facts)


def specification(reference: str, name: str, design: Design) -> str:
    """A design's page: its title, what tells it from others of that title beneath, muted, and
    its summary as its description."""
    title, details = named(design)
    beneath = (
        f":::{{container}} openline-subtitle\n{' · '.join(details)}\n:::\n\n" if details else ""
    )
    return (
        described(f"{', '.join([title, *details])}. {summary(design)}.", orphan=True)
        + f"# {title}\n\n{beneath}```{{openline:spec}} {reference}.{name}\n:catalog:\n```\n"
    )


def table(title: str, reference: str, description: str) -> str:
    return (
        described(description) + f"# {title}\n\n```{{openline:catalog}} {reference}\n:links:\n```\n"
    )


def toctree(entries: list[str], hidden: bool = False) -> str:
    """A list of pages, in the sidebar alone where ``hidden``."""
    options = ":maxdepth: 1\n:titlesonly:\n" + (":hidden:\n" if hidden else "")
    return f"```{{toctree}}\n{options}\n" + "\n".join(entries) + "\n```\n"


def conductor_pages() -> dict[str, str]:
    """``index.md`` and ``<family>/index.md``, then each standard's table and its conductors,
    under it: families and standards by name."""
    families: dict[str, list[tuple[str, type[Conductor], dict[str, Design]]]] = defaultdict(list)
    for module, (kind, listed) in catalogs("conductors").items():
        assert issubclass(kind, Conductor)
        families[kind.family].append((module, kind, listed))
    pages: dict[str, str] = {}
    for family, standards in sorted(families.items()):
        folder = slug(family)
        entries = []
        for module, kind, listed in sorted(standards, key=lambda given: given[1].standard):
            page = slug(kind.standard)
            entries.append(f"{page}/index")
            pages[f"{folder}/{page}/index.md"] = table(
                kind.standard,
                module,
                f"The {len(listed)} {family} conductors the OpenLine catalog lists to "
                f"{kind.standard}, by area.",
            )
            for name, value in listed.items():
                pages[f"{folder}/{page}/{name.lower()}.md"] = specification(module, name, value)
        pages[f"{folder}/index.md"] = f"# {family}\n\n" + toctree(entries)
    families_index = [f"{slug(family)}/index" for family in sorted(families)]
    pages["index.md"] = "# Conductors\n\n" + toctree(families_index)
    return pages


def structure_pages() -> dict[str, str]:
    """``index.md``, then each family's table and each structure's page beside it."""
    pages: dict[str, str] = {}
    folders = []
    for module, (kind, listed) in catalogs("structures").items():
        folder = module.rpartition(".")[2]
        folders.append(f"{folder}/index")
        pages[f"{folder}/index.md"] = table(
            kind.__name__,
            module,
            f"The {len(listed)} structures of the {kind.__name__} family the OpenLine catalog "
            "lists, by name.",
        )
        for name, value in listed.items():
            pages[f"{folder}/{name.lower()}.md"] = specification(module, name, value)
    pages["index.md"] = "# Structures\n\n" + toctree(folders)
    return pages


def example_pages(scripts: Path, tree: Path) -> dict[str, str]:
    """Each group's index and each script's page, the script run from where its page is."""
    pages: dict[str, str] = {}
    for readme in sorted(scripts.glob("*/README.md")):
        group = readme.parent.name
        heading, _, listing = readme.read_text(encoding="utf-8").partition("\n")
        names = re.findall(r"\(([a-z_0-9]+)\.py\)", listing)
        lines = []
        for name in names:
            script = scripts / group / f"{name}.py"
            title, text = introduced(script)
            lines.append(f"{{doc}}`{name}`\n: {first_sentence(text)}\n")
            path = Path(os.path.relpath(script, tree / group)).as_posix()
            pages[f"{group}/{name}.md"] = (
                described(first_sentence(text))
                + f"# {title}\n\n{text}\n\n```{{openline:example}} {path}\n```\n"
            )
        pages[f"{group}/index.md"] = (
            f"{heading}\n\n:::{{container}} examples\n"
            + "\n".join(lines)
            + ":::\n\n"
            + toctree(names, hidden=True)
        )
    return pages


def introduced(script: Path) -> tuple[str, str]:
    """A script's title, its docstring's first line, and its introduction beneath."""
    text = ast.get_docstring(ast.parse(script.read_text(encoding="utf-8")))
    if not text:
        raise ValueError(f"{script} gives no docstring to title its page")
    title, _, introduction = text.partition("\n\n")
    return title, introduction


def first_sentence(text: str) -> str:
    """The first sentence of a text, on one line."""
    line = " ".join(text.split())
    found = re.match(r"(.+?\.)(?:\s|$)", line)
    return found[1] if found else line


def write(root: Path, pages: dict[str, str]) -> None:
    """Write each page where it changed, and remove what is no longer one."""
    for name, content in pages.items():
        path = root / name
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    for path in sorted(root.rglob("*"), reverse=True):  # what a folder holds before it
        if path.is_file() and path.relative_to(root).as_posix() not in pages:
            path.unlink()
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def generate(app: Sphinx) -> None:
    """Every tree the configuration asks for, each made before any is written."""
    source = Path(app.srcdir)
    trees: dict[str, dict[str, str]] = {}
    if app.config.openline_catalog:
        trees |= {"conductors": conductor_pages(), "structures": structure_pages()}
    if app.config.openline_examples:
        scripts = (source / app.config.openline_examples).resolve()
        trees["examples"] = example_pages(scripts, source / "examples")
    for tree, pages in trees.items():
        write(source / tree, pages)


def setup(app: Sphinx) -> None:
    app.add_config_value("openline_catalog", False, "env", types=frozenset({bool}))
    app.add_config_value("openline_examples", "", "env", types=frozenset({str}))
    app.connect("builder-inited", generate)
