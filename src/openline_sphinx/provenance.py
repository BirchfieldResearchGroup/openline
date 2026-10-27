"""The documents behind the catalog, and what they give of it. The catalog is openline's own
Python; ``sources/`` holds the evidence, a folder for each pinned document,
``sources/<publisher>/<document>/``:

- ``document.toml``: its title, publisher, url, sha256 and the date it was retrieved; a published
  work's designation and year; ``pending``, what is not yet entered; ``cited_by``, the modules
  that cite it; ``conditions``, those it states for the results it reports. Its local copy,
  ``documents/<publisher>/<document>.*``, is kept out of Git.
- ``<path>.<Class>.csv``: a table of conductors of a class under ``openline.types``,
  ``conductors.astm.B232.csv``. A row gives where it is printed (``locator``), the design it
  lists (``design``, a constant of the class's module: ``DRAKE``), then, as printed, what the
  catalog holds of it, its ``designation`` (perhaps as another standard writes it: ``795 kcmil``
  for a code number), ``code_word``, ``classes`` and wires
  (``outer.count``, ``outer.diameter[in]``, a trapezoidal part's ``outer.area[in²]``), and what
  it reports (``reported.mass[lb/kft]``, ``reported.strength.SteelGA2[lbf]``,
  ``reported.ac_resistances.60Hz.75°C[Ω/kft]``, ``reported.ampacity.standard.75°C[A]``). A
  column takes the unit in its brackets, by its symbol (``units.SYMBOLS``); a row fills one
  column of a value.

The validation checks each row, a listing, against its design (``listings``). A structure's
document cites the module that holds it."""

import re
import tomllib
from datetime import date
from importlib import import_module
from pathlib import Path
from typing import Any, NamedTuple

import openline.types
from openline.types.conductors import Conductor

CITATION = {"title": str, "publisher": str, "url": str, "sha256": str, "retrieved": date}
OPTIONAL = {"designation": str, "year": int, "pending": list, "cited_by": list, "conditions": dict}


class Table(NamedTuple):
    """A document's table of conductors: its file, and their class."""

    path: Path
    cls: type[Conductor]


class Publication(NamedTuple):
    """How a published work is known: its designation, ``ASTM B232/B232M-17``, and year."""

    designation: str
    year: int


class Document(NamedTuple):
    """A pinned document, and what is entered from it."""

    files: tuple[Path, ...]
    title: str
    publisher: str
    url: str
    sha256: str
    retrieved: date
    published: tuple[Publication, ...]
    """Its publication, a standard's, handbook's, bulletin's or edition's; none for a document
    online, which the date it was retrieved dates."""
    tables: tuple[Table, ...]
    cited_by: tuple[str, ...]
    conditions: dict[str, Any]
    """The conditions it states for the results it reports: ``conditions["ampacity"]``."""

    @property
    def used(self) -> bool:
        """Whether openline uses it: enters values from it, or cites it."""
        return bool(self.tables or self.cited_by)


def documents(root: Path) -> tuple[Document, ...]:
    """Every document of a sources folder, ``<publisher>/<document>/``, by publisher and title:
    each with what a document gives, and entered, pending or cited."""
    found = []
    for path in sorted(root.glob("*/*/document.toml")):
        where = path.parent.relative_to(root).as_posix()
        given = tomllib.loads(path.read_text(encoding="utf-8"))
        kinds = {**CITATION, **OPTIONAL}
        wrong = [  # each a document must give, or gives, not of its kind
            name
            for name in sorted(kinds.keys() | given.keys())
            if (name in CITATION or name in given)
            and not isinstance(given.get(name), kinds.get(name, ()))
        ]
        if wrong:
            raise ValueError(f"{where}: document.toml gives {', '.join(wrong)} wrongly, or not")
        if ("designation" in given) != ("year" in given):
            raise ValueError(f"{where}: a published work gives its designation and its year")
        transcriptions = sorted(path.parent.glob("*.csv"))
        tables = tuple(Table(each, _class(each)) for each in transcriptions)
        cited = tuple(given.get("cited_by", ()))
        for module in cited:
            import_module(module)
        if not tables and not cited and not given.get("pending"):
            raise ValueError(f"{where}: nothing entered, pending or cited")
        found.append(
            Document(
                files=(path, *transcriptions),
                title=given["title"],
                publisher=given["publisher"],
                url=given["url"],
                sha256=given["sha256"],
                retrieved=given["retrieved"],
                published=(
                    (Publication(given["designation"], given["year"]),)
                    if "designation" in given
                    else ()
                ),
                tables=tables,
                cited_by=cited,
                conditions=given.get("conditions", {}),
            )
        )
    return tuple(
        sorted(found, key=lambda document: (_words(document.publisher), _words(document.title)))
    )


def _class(table: Path) -> type[Conductor]:
    """The class a table lists conductors of, by its name: ``conductors.astm.B232.csv``."""
    module, _, name = table.stem.rpartition(".")
    cls = getattr(import_module(f"{openline.types.__name__}.{module}"), name, None)
    if not (isinstance(cls, type) and issubclass(cls, Conductor)):
        raise ValueError(f"{table}: {table.stem} is no class of conductors")
    return cls


def _words(text: str) -> tuple[tuple[str, float], ...]:
    """Text as it sorts in a list: its words in any case, its numbers by value, 34.5 before 115."""
    parts = re.split(r"(\d+(?:\.\d+)?)", text.casefold())
    return tuple((part, 0.0) if n % 2 == 0 else ("", float(part)) for n, part in enumerate(parts))
