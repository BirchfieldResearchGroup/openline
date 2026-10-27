"""Towers, frames, poles, and their wire attachments."""

from typing import Any

from openline import _designs
from openline.types.structures import Structure

from . import frame, pole, tower

__all__ = ["frame", "named", "of", "pole", "tower"]


def of[T: Structure[Any]](cls: type[T]) -> tuple[T, ...]:
    """Return every structure of ``cls`` or its subclasses, in order of ``Structure.order``."""
    return _designs.of(__name__, cls)


def named(word: str) -> tuple[Structure[Any], ...]:
    """Return every structure listed under ``word``, in any case."""
    return _designs.named(__name__, word, Structure)
