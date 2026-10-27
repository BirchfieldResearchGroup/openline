"""What every figure shares: its svg element, titled and described, its numbers, and its
dimensions. Colors and type are figures.css's alone, light or dark."""

from html import escape
from typing import NamedTuple

LABEL = 14  # a label's size on screen, in pixels, at any width (figures.js keeps it)
WIDTH = 760  # the width a figure is drawn for, in pixels, where no script sizes its labels


class XY(NamedTuple):
    """A point in a figure, its y downwards."""

    x: float
    y: float


def number(value: float) -> str:
    """A coordinate to a tenth of a unit, as briefly as it prints: ``12.3``, ``-4``."""
    text = f"{value:.1f}".rstrip("0").rstrip(".")
    return "0" if text in ("", "-0") else text


def svg(
    kind: str,
    box: tuple[float, float, float, float],
    title: str,
    description: str,
    body: str,
    *,
    interactive: bool,
) -> str:
    """A figure's svg: ``ol-<kind>``, scaled to its container, its labels sized for its width
    until figures.js sizes them for the screen. Its title and description name it to a reader as
    an attribute, not text, so that what searches and crawlers read of a page is its own."""
    left, top, width, height = box
    label = LABEL * width / WIDTH
    name = f"{title}. {description}" if description else title
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" class="ol-diagram ol-{kind}"'
        f' viewBox="{number(left)} {number(top)} {number(width)} {number(height)}"'
        f' style="--ol-label-size:{label:.3g}px" role="{"group" if interactive else "img"}"'
        f' aria-label="{escape(name, True)}">{body}</svg>'
    )


def controls(interactive: bool, label: str) -> str:
    """What makes a part of an interactive figure a button, named for a reader."""
    if not interactive:
        return ""
    return f' role="button" tabindex="0" aria-pressed="false" aria-label="{escape(label, True)}"'


def dimension(start: XY, end: XY, label: str, offset: float) -> str:
    """A dimension between two points, drawn ``offset`` beyond them, its extension lines back to
    the points: above a horizontal one, or below where ``offset`` is negative; right of a
    vertical one, or left."""
    tick = 3
    beyond = tick if offset > 0 else -tick
    if abs(start.y - end.y) < abs(start.x - end.x):
        y = min(start.y, end.y) - offset
        lines = (
            f"M{number(start.x)},{number(start.y)}V{number(y - beyond)}"
            f"M{number(end.x)},{number(end.y)}V{number(y - beyond)}"
            f"M{number(start.x)},{number(y)}H{number(end.x)}"
        )
        x, mark = (start.x + end.x) / 2, (start, end)
        text = f'x="{number(x)}" y="{number(y)}" dy="-0.5em"'
        ticks = "".join(
            f"M{number(p.x - tick)},{number(y + tick)}l{2 * tick},{-2 * tick}" for p in mark
        )
    else:
        x = max(start.x, end.x) + offset if offset > 0 else min(start.x, end.x) + offset
        lines = (
            f"M{number(start.x)},{number(start.y)}H{number(x + beyond)}"
            f"M{number(end.x)},{number(end.y)}H{number(x + beyond)}"
            f"M{number(x)},{number(start.y)}V{number(end.y)}"
        )
        middle = number((start.y + end.y) / 2)
        text = (
            f'x="{number(x)}" y="{middle}" dy="-0.5em" transform="rotate(-90,{number(x)},{middle})"'
        )
        ticks = "".join(
            f"M{number(x - tick)},{number(p.y + tick)}l{2 * tick},{-2 * tick}" for p in (start, end)
        )
    return (
        f'<g class="ol-dimension"><path d="{lines}{ticks}"/><text {text}>{escape(label)}</text></g>'
    )
