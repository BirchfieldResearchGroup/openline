"""The ``openline`` domain: its directives."""

from collections.abc import Set
from typing import Any, ClassVar

from docutils.parsers.rst import Directive
from sphinx.domains import Domain

from . import api
from .directives import Catalog, Diagram, Example, References, Spec, Validation
from .reference import Materials, Standards, Units


class OpenLineDomain(Domain):
    """Namespace the directives; Sphinx's standard domain owns their labels."""

    name = "openline"
    label = "OpenLine"
    directives: ClassVar[dict[str, type[Directive]]] = {
        "catalog": Catalog,
        "spec": Spec,
        "example": Example,
        "references": References,
        "validation": Validation,
        "diagram": Diagram,
        "api": api.Api,
        "fields": api.Fields,
        "members": api.Members,
        "class-variables": api.ClassVariables,
        "strandings": api.Strandings,
        "materials": Materials,
        "units": Units,
        "standards": Standards,
    }

    def merge_domaindata(self, docnames: Set[str], otherdata: dict[str, Any]) -> None:
        """Nothing to merge from a parallel read: the domain keeps no data."""
