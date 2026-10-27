"""Designs as ``openline.conductors`` and ``openline.structures`` list them: the module of a
class's designs, a module's designs by name, a design by its reference, and every design of a
class or known by a word. Those packages hold a module per class, beside its type."""

import pkgutil
import re
from functools import cache
from importlib import import_module

from . import types
from .types import Design

__all__ = ["designs", "modules", "named", "of", "path", "resolve"]


def path(cls: type[Design]) -> str:
    """The module of a class's designs, within ``openline``: ``conductors.astm.b232`` for
    ``openline.types.conductors.astm.B232``."""
    package = cls.__module__.removeprefix(f"{types.__name__}.")
    name = re.sub(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", cls.__name__)
    return f"{package}.{name.lower()}"


def modules(collection: str) -> tuple[str, ...]:
    """Each module of a collection's designs, within ``openline``: ``conductors.astm.b232``."""
    package = import_module(f"{__package__}.{collection}")
    found = pkgutil.walk_packages(package.__path__, f"{package.__name__}.")
    return tuple(
        sorted(each.name.removeprefix(f"{__package__}.") for each in found if not each.ispkg)
    )


def designs(module: str) -> dict[str, Design]:
    """A module's designs by the name of their constant, each once though some have more than
    one: ``DRAKE``, not also its other code words."""
    found: dict[int, tuple[str, Design]] = {}
    for name, value in vars(import_module(f"{__package__}.{module}")).items():
        if not name.startswith("_") and isinstance(value, Design):
            found.setdefault(id(value), (name, value))
    return dict(found.values())


def resolve(reference: str) -> Design:
    """The design a reference names, its module and constant: ``conductors.astm.b232.DRAKE``."""
    module, _, name = reference.rpartition(".")
    if not module or name.startswith("_"):
        raise ValueError(f"Expected a reference such as conductors.astm.b232.DRAKE: {reference}")
    value = getattr(import_module(f"{__package__}.{module}"), name, None)
    if not isinstance(value, Design):
        raise ValueError(f"Unknown design: {reference}")
    return value


def of[T: Design](collection: str, cls: type[T]) -> tuple[T, ...]:
    """Every design of a class, or of its subclasses, that a collection lists, in its order."""
    return tuple(design for design in _listed(collection) if isinstance(design, cls))


def named[T: Design](collection: str, word: str, cls: type[T]) -> tuple[T, ...]:
    """Every design of a class that a collection lists known by ``word``, in any case."""
    word = word.casefold()
    return tuple(d for d in of(collection, cls) if word in (name.casefold() for name in d.names))


@cache
def _listed(collection: str) -> tuple[Design, ...]:
    """A collection's designs, each once though some have more than one name, by
    ``Design.order``: ``openline.conductors``'s."""
    within = collection.removeprefix(f"{__package__}.")
    found = {id(d): d for module in modules(within) for d in designs(module).values()}
    return tuple(sorted(found.values(), key=lambda design: design.order))
