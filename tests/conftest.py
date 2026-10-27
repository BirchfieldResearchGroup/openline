"""Fixtures shared by every part of the tests: where the repository keeps what they read.

The tests mirror the code: ``openline/`` the library, ``docs/`` what readers see (the Sphinx
extension, figures, examples, and the validation of the catalog against its sources)."""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root(pytestconfig: pytest.Config) -> Path:
    """The repository."""
    return pytestconfig.rootpath


@pytest.fixture(scope="session")
def sources(root: Path) -> Path:
    """The transcribed documents: ``sources/<publisher>/<document>/``."""
    return root / "sources"
