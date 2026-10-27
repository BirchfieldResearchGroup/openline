"""The generated pages: one per catalog module and per design, one per example script, each
written where it changed and every other file of its tree removed."""

import ast
from pathlib import Path
from types import SimpleNamespace
from typing import cast

import pytest
from sphinx.application import Sphinx

from openline import _designs
from openline.conductors.astm import b231, b232
from openline.types.conductors import Conductor
from openline_sphinx import pages
from openline_sphinx.presentation.conductors import grids, nominal


def argument(page: str, directive: str) -> str:
    """What a page gives a directive: ``conductors.astm.b232`` of ``openline:catalog``."""
    return page.split(f"{{{directive}}} ")[1].partition("\n")[0]


@pytest.mark.parametrize("collection", ["conductors", "structures"])
def test_each_catalog_module_has_a_table_and_each_design_a_specification(collection: str) -> None:
    written = (pages.conductor_pages if collection == "conductors" else pages.structure_pages)()
    tables = [argument(p, "openline:catalog") for p in written.values() if "openline:catalog" in p]
    assert sorted(tables) == sorted(_designs.modules(collection))
    specifications = [page for page in written.values() if "openline:spec" in page]
    assert sorted(argument(page, "openline:spec") for page in specifications) == sorted(
        f"{module}.{name}" for module in tables for name in _designs.designs(module)
    )
    for page in specifications:  # an orphan, described, titled by its design's title
        assert page.startswith("---\norphan: true\nmyst:\n  html_meta:\n    description: ")
        title, details = pages.named(_designs.resolve(argument(page, "openline:spec")))
        assert f"\n# {title}\n" in page
        assert " · ".join(details) in page
        assert ":catalog:\n" in page


def test_each_example_has_a_page_titled_by_its_docstring(root: Path, tmp_path: Path) -> None:
    examples = root / "examples"
    written = pages.example_pages(examples, tmp_path)
    scripts = sorted(examples.glob("*/*.py"))
    assert sorted(written) == sorted(
        [f"{script.parent.name}/{script.stem}.md" for script in scripts]
        + [f"{readme.parent.name}/index.md" for readme in examples.glob("*/README.md")]
    )  # each script listed in its group's README
    for script in scripts:
        page = written[f"{script.parent.name}/{script.stem}.md"]
        docstring = ast.get_docstring(ast.parse(script.read_text(encoding="utf-8")))
        assert docstring
        assert page.startswith("---\nmyst:\n  html_meta:\n    description: ")
        assert f"\n# {docstring.splitlines()[0]}\n" in page
        path = tmp_path / script.parent.name / argument(page, "openline:example")
        assert path.resolve() == script.resolve()


def test_writing_rewrites_what_changed_and_removes_the_rest(tmp_path: Path) -> None:
    given = {"standard/index.md": "# Standard\n", "standard/drake.md": "# Drake\n"}
    pages.write(tmp_path, given)
    written = {path: path.stat().st_mtime_ns for path in tmp_path.rglob("*.md")}
    pages.write(tmp_path, given)
    assert {path: path.stat().st_mtime_ns for path in written} == written

    (tmp_path / "standard" / "notes.md").write_text("Not generated", encoding="utf-8")
    pages.write(tmp_path, {"index.md": "# Conductors\n"})
    assert [path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*")] == ["index.md"]


def test_a_catalog_module_of_two_classes_writes_nothing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    mixed = {"DRAKE": b232.DRAKE, "ARBUTUS": b231.ARBUTUS}
    monkeypatch.setattr(_designs, "designs", lambda module: mixed)
    config = SimpleNamespace(openline_catalog=True, openline_examples="")
    app = cast(Sphinx, SimpleNamespace(srcdir=tmp_path, config=config))
    with pytest.raises(ValueError, match="must list designs of one class"):
        pages.generate(app)
    assert not any(tmp_path.iterdir())


@pytest.mark.parametrize("module", _designs.modules("conductors"))
def test_a_standard_lists_conductors_by_code_word_then_by_each_way_of_sizing(module: str) -> None:
    # Each conductor once: those known by a code word, then a table for each way the rest are
    # sized, kcmil apart from mm², each table by size, as a standard's tables order them.
    listed = {
        name: design
        for name, design in _designs.designs(module).items()
        if isinstance(design, Conductor)
    }
    found = grids(list(listed.items()))
    assert sorted(constant for grid in found for constant, _ in grid.rows) == sorted(listed)
    kinds = [
        {
            "named" if listed[c].code_words else type(listed[c].designation).__name__
            for c, _ in grid.rows
        }
        for grid in found
    ]
    assert all(len(kind) == 1 for kind in kinds)
    assert all("named" not in kind for kind in kinds[1:])  # code words first
    for grid in found:
        sizes = [nominal(listed[constant].designation) for constant, _ in grid.rows]
        assert sizes == sorted(sizes)
