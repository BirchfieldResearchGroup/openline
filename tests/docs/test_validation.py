"""The catalog against what each listing gives, within bounds: the validation the documentation
tabulates. Every listing's wires agree with its design's within 1%, every design is listed by
the names its listings print, and each local copy of a document is the one pinned.

Reported-resistance ampacity must agree within 2.5 A (half the published rounding step) or 1%.
Solar flux must agree within 0.05 W/ft².
"""

import hashlib
from datetime import date
from pathlib import Path

import pytest

from openline import conductors
from openline.types.conductors import Conductor, Surface
from openline.types.conductors.astm import B232
from openline.types.units import celsius, w_per_ft2
from openline_sphinx import provenance, validation
from openline_sphinx.listings import listings

type Comparisons = dict[str, list[validation.Comparison]]


@pytest.fixture(scope="module")
def found(sources: Path) -> validation.Compared:
    """Every calculated value beside its published one, by check, computed once."""
    return validation.comparisons(provenance.documents(sources))


@pytest.fixture(scope="module")
def comparisons(found: validation.Compared) -> Comparisons:
    return {check.label: compared for check, compared in found}


def test_every_check_compares_some_listing(comparisons: Comparisons) -> None:
    assert all(comparisons.values())


@pytest.mark.parametrize("check", validation.CHECKS, ids=lambda check: check.label)
def test_most_come_within_their_bound(comparisons: Comparisons, check: validation.Check) -> None:
    assert validation.summary(comparisons[check.label]).percentile <= check.bound


def test_each_rating_from_reported_resistances_meets_its_own(comparisons: Comparisons) -> None:
    far = [
        each.where
        for each in comparisons["Ampacity, from reported resistances"]
        if abs(each.ours - each.theirs) > max(2.5, 0.01 * each.theirs)
    ]
    assert far == []


def test_each_sun_is_as_given(comparisons: Comparisons) -> None:
    near = w_per_ft2(0.05).si
    assert all(abs(each.ours - each.theirs) <= near for each in comparisons["Sun's heat flux"])


@pytest.fixture
def surfaces(tmp_path: Path) -> provenance.Document:
    """A source rating Drake for two surfaces, one rating left blank."""
    path = tmp_path / "conductors.astm.B232.csv"
    path.write_text(
        "locator,design,code_word,designation,reported.ampacity.standard.75°C[A],"
        "reported.ampacity.E3X.75°C[A],reported.ampacity.E3X.200°C[A]\n"
        "row Drake,DRAKE,Drake,795 kcmil,910,1040,\n",
        encoding="utf-8",
    )
    ampacity = {
        "air[°C]": 25,
        "wind[ft/s]": 2,
        "angle[°]": 90,
        "sun[W/ft²]": 96,
        "elevation[ft]": 0,
        "surfaces": {
            "standard": {"emissivity": 0.5, "absorptivity": 0.5},
            "E3X": {"emissivity": 0.9, "absorptivity": 0.2},
        },
    }
    return provenance.Document(
        files=(path,),
        title="Surface observations",
        publisher="Example",
        url="",
        sha256="",
        retrieved=date(2026, 10, 26),
        published=(),
        tables=(provenance.Table(path, B232),),
        cited_by=(),
        conditions={"frequency[Hz]": 60, "ampacity": ampacity},
    )


def test_each_rating_is_of_its_surface(surfaces: provenance.Document) -> None:
    ((standard, coated),) = (row.ratings for row in listings([surfaces]))
    assert standard.surface == Surface(emissivity=0.5, absorptivity=0.5)
    assert coated.surface == Surface(emissivity=0.9, absorptivity=0.2)
    assert standard.environment == coated.environment
    assert standard.temperature == coated.temperature == celsius(75)
    assert (standard.current.si, coated.current.si) == (910, 1040)
    assert coated.where == "Surface observations, row Drake, E3X surface"


def test_a_surface_sets_apart_only_its_own_ratings(surfaces: provenance.Document) -> None:
    surfaces.conditions["ampacity"]["surfaces"]["E3X"]["apart"] = ["row Drake"]
    ((standard,),) = (row.ratings for row in listings([surfaces]))
    assert standard.current.si == 910


def test_a_rating_needs_its_surface(surfaces: provenance.Document) -> None:
    del surfaces.conditions["ampacity"]["surfaces"]["E3X"]
    with pytest.raises(ValueError, match=r"row Drake: ampacity\.E3X has no surface"):
        list(listings([surfaces]))


def test_every_listing_gives_its_design_s_wires_within_1_percent(
    comparisons: Comparisons,
) -> None:
    far = [each.where for each in comparisons["Construction"] if abs(each.difference) > 0.01]
    assert far == []


def test_every_design_is_listed_by_the_names_its_listings_print(sources: Path) -> None:
    printed: dict[int, set[str]] = {}
    for row in listings(provenance.documents(sources)):
        printed.setdefault(id(row.design), set()).update({row.code_word} - {""})
    for design in conductors.of(Conductor):
        assert printed.get(id(design)) == set(design.code_words), design.title


def test_each_local_copy_is_the_document_pinned(root: Path, sources: Path) -> None:
    """``documents/``, kept out of Git, holds a copy of a document where one is at hand."""
    for document in provenance.documents(sources):
        key = document.files[0].parent.relative_to(sources).as_posix()
        copies = list((root / "documents").glob(f"{key}.*"))
        assert len(copies) == (1 if (root / "documents").exists() else 0), key
        for copy in copies:
            assert hashlib.sha256(copy.read_bytes()).hexdigest() == document.sha256, copy
