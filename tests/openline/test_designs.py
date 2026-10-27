"""openline._designs, behind ``openline.conductors`` and ``openline.structures``: every design of a
class, every design known by a word, each once, in its collection's order; a module per class at
its type's own path; a design by its reference; and the data sheet a design prints."""

import re
from importlib import import_module

import pytest

from openline import _designs, conductors, structures
from openline.conductors.astm import b231, b856
from openline.conductors.astm.b232 import DRAKE
from openline.conductors.csa import c61089
from openline.structures.frame import TH_230
from openline.structures.tower import D_2_D_2018_3_T1
from openline.types import Design
from openline.types.conductors import ACSR, ASTM, Conductor
from openline.types.conductors.astm import B231, B232, B779_AW
from openline.types.conductors.bs import BS_EN50182_AL3
from openline.types.conductors.iec import A1_Syz
from openline.types.structures import Frame, Structure, Tower


def test_of_gives_every_design_of_a_class_and_its_subclasses() -> None:
    assert all(DRAKE in conductors.of(cls) for cls in (B232, ACSR, ASTM, Conductor))


def test_of_gives_conductors_from_the_smallest_up() -> None:
    areas = [conductor.area for conductor in conductors.of(Conductor)]
    assert areas == sorted(areas)


def test_of_gives_structures_by_their_names() -> None:
    names = [structure.name for structure in structures.of(Structure)]
    assert names == sorted(names)


def test_named_finds_every_design_known_by_a_word() -> None:  # ACSR, ACSS, CSA alike
    assert {DRAKE, b856.DRAKE, c61089.DRAKE} <= set(conductors.named("Drake"))


def test_named_finds_a_word_in_any_case() -> None:
    assert structures.named("d-2-d-2018.3 t1") == (D_2_D_2018_3_T1,)


def test_named_finds_only_designs_known_by_the_word() -> None:
    assert all("Drake" in drake.code_words for drake in conductors.named("drake"))
    assert structures.named("drake") == ()


def test_a_design_under_two_names_is_listed_once() -> None:  # Bitteroot, printed Bitterroot too
    assert b231.BITTERROOT is b231.BITTEROOT
    assert conductors.of(B231).count(b231.BITTEROOT) == 1


@pytest.mark.parametrize(
    ("cls", "path"),
    [
        (B232, "conductors.astm.b232"),
        (B779_AW, "conductors.astm.b779_aw"),
        (A1_Syz, "conductors.iec.a1_syz"),
        (BS_EN50182_AL3, "conductors.bs.bs_en50182_al3"),
        (Tower, "structures.tower"),
        (Frame, "structures.frame"),
    ],
    ids=lambda value: getattr(value, "__name__", None),
)
def test_a_class_s_designs_are_at_its_type_s_own_path(cls: type[Design], path: str) -> None:
    assert _designs.path(cls) == path


def test_every_listed_design_is_in_its_class_s_module() -> None:
    listed: tuple[Design, ...] = (*conductors.of(Conductor), *structures.of(Structure))
    astray = [
        design.title
        for design in listed
        if design not in vars(import_module(f"openline.{_designs.path(type(design))}")).values()
    ]
    assert astray == []


def test_a_reference_names_its_design() -> None:
    assert _designs.resolve("conductors.astm.b232.DRAKE") is DRAKE


@pytest.mark.parametrize(
    "reference",
    ["DRAKE", "conductors.astm.b232.NOT_A_DESIGN", "conductors.astm.b232.__name__"],
    ids=["no module", "no such design", "not a design"],
)
def test_a_reference_to_no_design_is_refused(reference: str) -> None:
    with pytest.raises(ValueError, match=re.escape(reference)):
        _designs.resolve(reference)


def test_a_design_prints_its_title_then_its_values_labeled() -> None:
    title, *rows = str(DRAKE).splitlines()
    assert title == DRAKE.title
    assert ["core", str(DRAKE.core)] in [row.split(None, 1) for row in rows]


def test_a_design_prints_no_value_it_is_not_given() -> None:  # TH-230 gives no line angles
    labels = {row.split()[0] for row in str(TH_230).splitlines()[1:]}
    assert TH_230.line_angles == ()
    assert ("voltages" in labels, "line_angles" in labels) == (True, False)
