"""A wire looks like its material: it carries a class for its material and for each one that
material derives from, ``ol-Aluminum1350H19 ol-HardDrawnAluminum ol-Aluminum ol-Metal``, and
figures.css colors the most particular of them it styles, light or dark."""

from functools import cache

from openline.types.materials import Material


@cache
def classes(material: type[Material]) -> str:
    """A material's classes: its own, then each it derives from, to ``ol-Metal``."""
    return " ".join(
        f"ol-{each.__name__}"
        for each in material.__mro__
        if isinstance(each, type) and issubclass(each, Material) and each is not Material
    )


def shade(identifier: str, key: str, material: type[Material]) -> str:
    """A part's wire faces, cut across, in its material's color, lit from the upper left; its
    ``key`` the part's, so that selecting the part tints it."""
    return (
        f'<radialGradient id="{identifier}" class="ol-shade {classes(material)}"'
        f' data-ol-key="{key}" cx=".36" cy=".3" r=".75">'
        '<stop class="ol-lit"/><stop class="ol-tone" offset=".55"/>'
        '<stop class="ol-deep" offset="1"/></radialGradient>'
    )
