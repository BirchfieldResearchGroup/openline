"""OpenLine's palette, overridable through Furo's ordinary theme options. A figure's colors,
its metals' among them, are figures.css's."""

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config

ASSETS = Path(__file__).parent / "assets"
COLORS = {
    "color-brand-primary": ("#0b7a68", "#5cc8b0"),
    "color-brand-content": ("#0b7a68", "#5cc8b0"),
    "color-brand-visited": ("#0b7a68", "#5cc8b0"),
    "color-foreground-primary": ("#1b1f24", "#e6e9ed"),
    "color-foreground-secondary": ("#4a525c", "#b3bac3"),
    "color-foreground-muted": ("#6b737d", "#8a929c"),
    "color-foreground-border": ("#c4cad1", "#3a4048"),
    "color-background-primary": ("#ffffff", "#121417"),
    "color-background-secondary": ("#f6f7f9", "#181b1f"),
    "color-background-border": ("#e9ecef", "#23272c"),
    "color-code-background": ("#f6f7f9", "#181b1f"),
}


def configure(_app: Sphinx, config: Config) -> None:
    config.html_static_path = list(dict.fromkeys([str(ASSETS), *config.html_static_path]))
    if not config.html_favicon:
        config.html_favicon = str(ASSETS / "openline-icon.svg")
    if config.html_theme != "furo":
        return
    options = dict(config.html_theme_options)
    if not config.html_logo:
        options.setdefault("light_logo", "openline-logo.svg")
        options.setdefault("dark_logo", "openline-logo-dark.svg")
    options.setdefault("sidebar_hide_name", False)
    for index, mode in enumerate(("light", "dark")):
        key = f"{mode}_css_variables"
        defaults = {variable: pair[index] for variable, pair in COLORS.items()}
        defaults["font-stack--headings"] = '"Inter", var(--font-stack)'
        options[key] = {**defaults, **options.get(key, {})}
    config.html_theme_options = options
