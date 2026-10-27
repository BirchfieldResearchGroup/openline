"""Bare overhead conductors, grouped by construction and standard."""

from openline import _designs
from openline.types.conductors import Conductor

from . import astm, bs, csa, iec

__all__ = ["astm", "bs", "csa", "iec", "named", "of"]


def of[T: Conductor](cls: type[T]) -> tuple[T, ...]:
    """Return every conductor of ``cls`` or its subclasses, in order of ``Conductor.order``."""
    return _designs.of(__name__, cls)


def named(word: str) -> tuple[Conductor, ...]:
    """Return every conductor listed under ``word``, in any case."""
    return _designs.named(__name__, word, Conductor)
