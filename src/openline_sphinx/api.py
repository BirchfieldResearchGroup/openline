"""API reference generation using autodoc and tables for fields, members, and stranding rules."""

import ast
import dataclasses
import textwrap
import typing
from collections.abc import Iterable
from enum import Enum
from importlib import import_module
from inspect import get_annotations, getfile, getsource, isclass, isfunction
from types import ModuleType, UnionType
from typing import Any, ClassVar

from docutils import nodes
from docutils.parsers.rst import Parser
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.pycode import ModuleAnalyzer
from sphinx.util.docutils import SphinxDirective, new_document
from sphinx.util.nodes import make_id

import openline
from openline.types import Record

from .tables import Cell, table

OWN_TABLES = ("strandings",)  # class variables shown in a table of their own, its directive


def public(module: ModuleType) -> list[Any]:
    """The classes and functions a module exports, including its public facade."""
    exported = set(module.__all__)
    return [
        value
        for name, value in vars(module).items()
        if name in exported and (isclass(value) or isfunction(value))
    ]


def packaged(value: Any) -> bool:
    """Whether a class is one of the package's own."""
    return bool(value.__module__.partition(".")[0] == openline.__name__)


def record(cls: object) -> bool:
    """Whether a class is a record, or a named tuple of a calculation's own: a class of fields."""
    if isclass(cls) and issubclass(cls, tuple) and hasattr(cls, "_fields"):
        return True
    return isclass(cls) and issubclass(cls, Record) and dataclasses.is_dataclass(cls)


def fields(cls: type[Any]) -> list[str]:
    if not record(cls):
        return []
    if issubclass(cls, tuple):
        return list(getattr(cls, "_fields", ()))
    return [field.name for field in dataclasses.fields(cls)]


def class_variables(cls: type) -> list[tuple[str, str]]:
    """The class variables a class assigns that its bases declare, each as the class writes it:
    ``("resistivity", "ohm_mm2_per_m(0.028172)")``."""
    declared: set[str] = set()
    for base in cls.__mro__[1:]:
        hints: dict[str, Any] = get_annotations(base, eval_str=True)
        declared |= {name for name, hint in hints.items() if typing.get_origin(hint) is ClassVar}
    source = textwrap.dedent(getsource(cls))
    body = ast.parse(source).body[0]
    if not isinstance(body, ast.ClassDef):
        raise TypeError(f"{cls.__qualname__}'s source is no class")
    return [
        (node.targets[0].id, ast.get_source_segment(source, node.value) or "")
        for node in body.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id in declared
    ]


def described(cls: type, name: str) -> str:
    """The docstring of a field, member or class variable, from the class that declares it."""
    for owner in cls.__mro__:
        if packaged(owner):
            docs = ModuleAnalyzer.for_module(owner.__module__).find_attr_docs()
            if lines := docs.get((owner.__qualname__, name)):
                return " ".join(" ".join(lines).split())
    return ""


def shown(hint: Any) -> list[nodes.Node]:
    """A type as a field's table gives it: a type variable as its bound, the package's classes
    linked to their entries."""
    if isinstance(hint, typing.TypeVar):
        bound = hint.__bound__
        return shown(bound) if bound is not None else [nodes.Text(hint.__name__)]
    origin, arguments = typing.get_origin(hint), typing.get_args(hint)
    if origin in (UnionType, typing.Union):
        return joined((shown(argument) for argument in arguments), " | ")
    if origin is not None:
        inner = joined((shown(argument) for argument in arguments), ", ")
        return [*shown(origin), nodes.Text("["), *inner, nodes.Text("]")]
    if hint is Ellipsis:
        return [nodes.Text("...")]
    if hint is type(None):
        return [nodes.Text("None")]
    if isclass(hint) and packaged(hint):
        return [
            addnodes.pending_xref(
                "",
                nodes.Text(hint.__name__),
                refdomain="py",
                reftype="class",
                reftarget=f"{hint.__module__}.{hint.__qualname__}",
                refexplicit=True,
            )
        ]
    return [nodes.Text(getattr(hint, "__name__", str(hint)))]


def parsed(directive: SphinxDirective, lines: list[str]) -> list[nodes.Node]:
    """reStructuredText that a directive gives, parsed as such in a Markdown page too, as MyST's
    ``eval-rst`` parses it: in a document of its own, with the page's settings."""
    page = directive.state.document
    document = new_document(page["source"], page.settings)
    document.reporter = page.reporter
    Parser().parse("\n".join(lines), document)
    return document.children


def joined(parts: Iterable[list[nodes.Node]], between: str) -> list[nodes.Node]:
    result: list[nodes.Node] = []
    for part in parts:
        result.extend([nodes.Text(between), *part] if result else part)
    return result


class TableDirective(SphinxDirective):
    """A table of the API: its cells parse a docstring's markup, and a row can be the entry of
    the class it names."""

    def inline(self, text: str) -> nodes.inline:
        parsed, messages = self.state.inline_text(text, self.lineno)
        return nodes.inline("", "", *parsed, *messages)

    def declare(self, value: Any, objtype: str) -> nodes.target:
        """A target that makes ``value`` a Python object of this page, for links to it."""
        name = f"{value.__module__}.{value.__qualname__}"
        node_id = make_id(self.env, self.state.document, "", name)
        result = nodes.target("", "", ids=[node_id])
        self.env.domains.python_domain.note_object(name, objtype, node_id, location=result)
        return result

    def declare_module(self, module: ModuleType) -> nodes.target:
        """A target that makes a module one of this page's, for links to it."""
        node_id = f"module-{module.__name__}"
        result = nodes.target("", "", ids=[node_id])
        domain = self.env.domains.python_domain
        domain.note_module(module.__name__, node_id, "", "", False)
        domain.note_object(module.__name__, "module", node_id, location=result)
        return result

    def named(self, value: Any, objtype: str, text: str) -> nodes.inline:
        """A name, as code, that is its object's target."""
        return nodes.inline("", "", self.declare(value, objtype), nodes.literal(text=text))


class ClassDirective(TableDirective):
    """A table about one class, named in full: ``openline.types.structures.Datum``."""

    required_arguments = 1

    def documented(self) -> Any:
        """The class, its page depending on each of its classes that it takes descriptions from."""
        module, _, name = self.arguments[0].rpartition(".")
        cls = getattr(import_module(module), name)
        for owner in cls.__mro__:
            if packaged(owner):
                self.env.note_dependency(getfile(owner))
        return cls


class Fields(ClassDirective):
    """A dataclass's fields, the inherited first: each name, type and description."""

    def run(self) -> list[nodes.Node]:
        cls = self.documented()
        hints = typing.get_type_hints(cls)
        rows: list[list[Cell]] = [
            [
                nodes.literal(text=name),
                nodes.literal("", "", *shown(hints[name])),
                self.inline(described(cls, name)),
            ]
            for name in fields(cls)
        ]
        return [table([("Field", ""), ("Type", ""), ("Description", "")], rows)]


class Members(ClassDirective):
    """An enumeration's members, each with its description."""

    def run(self) -> list[nodes.Node]:
        cls = self.documented()
        rows: list[list[Cell]] = [
            [nodes.literal(text=member.name), self.inline(described(cls, member.name))]
            for member in cls
        ]
        return [table([("Member", ""), ("Description", "")], rows)]


class ClassVariables(ClassDirective):
    """The class variables a class assigns that its bases declare, each as the class writes it,
    with its base's description; but those with a table of their own."""

    def run(self) -> list[nodes.Node]:
        cls = self.documented()
        rows: list[list[Cell]] = [
            [nodes.literal(text=name), nodes.literal(text=text), self.inline(described(cls, name))]
            for name, text in class_variables(cls)
            if name not in OWN_TABLES
        ]
        return [table([("Class variable", ""), ("Value", ""), ("Description", "")], rows)]


class Api(SphinxDirective):
    """A module's classes and functions, in its order (``documented``)."""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        module = import_module(self.arguments[0])
        return parsed(self, documented(module, public(module)))


def documented(module: ModuleType, values: Iterable[Any]) -> list[str]:
    """The reStructuredText that documents some of a module's classes and functions, in its
    order: a dataclass with its fields, an enumeration with its members, and a class with the
    class variables it assigns."""
    lines = [f".. py:module:: {module.__name__}", ""]
    for value in values:
        name = f"{module.__name__}.{value.__qualname__}"
        if isfunction(value):
            lines += [f".. autofunction:: {name}", ""]
            continue
        enumeration = issubclass(value, Enum)
        hidden = [member.name for member in value] if enumeration else fields(value)
        lines += [f".. autoclass:: {name}", "   :members:"]
        if ancestry(getattr(value, "__orig_bases__", value.__bases__)):
            lines.append("   :show-inheritance:")
        if hidden:
            lines.append(f"   :exclude-members: {', '.join(hidden)}")
        lines.append("")
        own = set(get_annotations(value)) & set(fields(value))  # a table where it adds fields
        assigned = {name for name, _ in class_variables(value)}
        tables = (
            (enumeration, "members"),
            (own, "fields"),
            (assigned - set(OWN_TABLES), "class-variables"),
            *((name in assigned, name) for name in OWN_TABLES),
        )
        for shows, directive in tables:
            if shows:
                lines += [f"   .. openline:{directive}:: {name}", ""]
    return lines


class Strandings(ClassDirective):
    """What a standard gives for each stranding, a strand at a time from the outside in: each
    strand's wires, its rings' lay ratios, each with the one preferred, how much the lay
    lengthens them where the standard fixes the lay by that, and the share of their strength the
    conductor is rated at."""

    def run(self) -> list[nodes.Node]:
        cls = self.documented()
        rows: list[list[Cell]] = []
        for counts, given in cls.strandings.items():
            for index, (count, stranding) in enumerate(zip(counts, given, strict=True)):
                ratios = (str(ratio) for ratio in stranding.lay_ratios)
                increment, factor = stranding.increment, stranding.rating_factor
                rows.append(
                    [
                        "/".join(map(str, counts)) if index == 0 else "",
                        str(count),
                        "; ".join(ratios),
                        "" if increment is None else f"{increment:.4g}",
                        "" if factor is None else f"{factor:g}",
                    ]
                )
        headers = ("Stranding", "Wires", "Lay ratios", "Increment", "Rating factor")
        return [table([(header, "") for header in headers], rows, numeric=(1, 3, 4))]


def signature(
    _app: Sphinx,
    what: str,
    _name: str,
    value: Any,
    _options: Any,
    _signature: str,
    _returned: str,
) -> tuple[str, None] | None:
    """Keep record constructor signatures; enums list their members instead."""
    if what == "class" and isclass(value) and issubclass(value, Enum):
        return "", None
    return None


def ancestry(given: Iterable[Any]) -> list[type]:
    """Bases in the package, unparameterized, but ``Record``, which every record has."""
    shown = [typing.get_origin(base) or base for base in given]
    return [base for base in shown if isclass(base) and packaged(base) and base is not Record]


def bases(_app: Sphinx, _name: str, _value: Any, _options: Any, given: list[Any]) -> None:
    given[:] = ancestry(given)


def setup(app: Sphinx) -> None:
    app.setup_extension("sphinx.ext.autodoc")
    app.connect("autodoc-process-signature", signature)
    app.connect("autodoc-process-bases", bases)
