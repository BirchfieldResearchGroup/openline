"""openline.mechanical: a conductor's mass against its standard's tables; its modulus and
expansion from its wires and their lay against alfanar's for ACSR; its rated strength by its
standard's rules against the standards' tables; and a level span strung with it, its tension and
sag at a temperature from how it was strung, its core alone holding it once its aluminum goes
slack."""

import math
from dataclasses import replace

import pytest

from openline.conductors import iec
from openline.conductors.astm import b778, b779, b856
from openline.conductors.astm.b231 import ARBUTUS, LILAC
from openline.conductors.astm.b232 import (
    BANTAM,
    CARDINAL,
    DRAKE,
    EAGLE,
    FALCON,
    MALLARD,
    PIGEON,
)
from openline.conductors.astm.b399 import AKRON, ALLIANCE, AMES, FLINT, KCMIL_1750_61
from openline.conductors.astm.b524 import KCMIL_30_58_4_3, KCMIL_3000_72_19
from openline.conductors.bs.bs_en50182_al3 import BOX
from openline.conductors.csa import c49
from openline.mechanical import expansion, mass, modulus, sag, stiffness, strength, tension, weight
from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.conductors.astm import B231, B399, B779
from openline.types.lines import Strung
from openline.types.materials import (
    AluminumAlloy,
    Steel,
    SteelGA2,
    SteelGA3,
    SteelGA4,
    SteelGA5,
    SteelGC2,
    SteelMA2,
    SteelMA3,
    SteelMA4,
    SteelMA5,
    SteelS1A,
    SteelS3A,
)
from openline.types.units import (
    GRAVITY,
    celsius,
    kg_per_km,
    kn,
    lb_per_kft,
    lbf,
    m,
)

STRUNG = Strung(kn(28), celsius(15))
SPAN = m(300)
ALFANAR = {  # Overhead Conductors, p. 19: ACSR's final modulus, in MPa, and expansion, in 1e-6/K
    PIGEON: (79_000, 19.1),
    DRAKE: (74_200, 18.9),
    EAGLE: (80_000, 17.8),
    MALLARD: (78_500, 18.0),
    CARDINAL: (67_100, 19.3),
    FALCON: (69_700, 19.5),
}
NAMES = [conductor.code_words[0] for conductor in ALFANAR]


def test_drake_weighs_b232_s_1093_lb_per_kft() -> None:  # table 1
    assert weight(DRAKE).si == pytest.approx(lb_per_kft(1093).si * GRAVITY, rel=0.005)


def test_aac_tw_weighs_b778_s_315_3_lb_per_kft() -> None:  # ASTM B778-22, table 1, Tulip/TW
    assert mass(b778.TULIP).to(lb_per_kft) == pytest.approx(315.3, rel=0.005)


def test_al3_weighs_alfanar_s_51_4_kg_per_km() -> None:  # Overhead Conductors, p. 19, Box
    assert mass(BOX).to(kg_per_km) == pytest.approx(51.4, rel=0.001)


@pytest.mark.parametrize("conductor", [ARBUTUS, FLINT], ids=lambda c: c.title)
def test_class_aa_lengthens_its_wires_within_its_standard_s_2_percent(
    conductor: Conductor,
) -> None:  # B231 and B399, 7.1: 37 wires at 13.5, the tabulated mass approximate to 2%
    straight = sum(strand.area.si * strand.material.density.si for strand in conductor.strands)
    assert 1.015 < mass(conductor).si / straight < 1.02


def test_a_conductor_s_mass_takes_its_lay_and_not_its_direction(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    turned = mass(b779.DRAKE)
    monkeypatch.setattr(B779, "hand", None)
    assert mass(replace(b779.DRAKE)) == turned  # a design lays its wires once: lay it again


def test_a_conductor_whose_rings_have_no_lay_has_no_mass() -> None:  # 3/4: aluminum and steel
    with pytest.raises(Missing, match="lay"):
        mass(BANTAM)


@pytest.mark.parametrize(("conductor", "given"), ALFANAR.items(), ids=NAMES)
def test_expansion_is_alfanar_s(conductor: Conductor, given: tuple[float, float]) -> None:
    assert expansion(conductor).si == pytest.approx(given[1] * 1e-6, rel=0.02)


@pytest.mark.parametrize(("conductor", "given"), ALFANAR.items(), ids=NAMES)
def test_modulus_is_7_to_19_percent_above_alfanar_s(
    conductor: Conductor, given: tuple[float, float]
) -> None:  # the wires' own moduli along their helices, which leave out how a stranded
    # conductor's wires settle into one another as it is first pulled
    assert 1.07 < modulus(conductor).si / (given[0] * 1e6) < 1.19


def test_a_metal_without_its_modulus_has_no_stiffness(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delattr(AluminumAlloy, "modulus")  # as though no document gave it
    with pytest.raises(Missing, match="modulus"):
        stiffness(BOX)


def test_at_its_stringing_temperature_a_span_holds_its_strung_tension() -> None:
    held = tension(DRAKE, span=SPAN, strung=STRUNG, temperature=celsius(15))
    assert held.si == pytest.approx(STRUNG.tension.si, rel=1e-9)


def test_a_taut_span_sags_as_a_parabola() -> None:  # w S² / 8H
    parabola = weight(DRAKE).si * SPAN.si**2 / (8 * STRUNG.tension.si)
    drop = sag(DRAKE, span=SPAN, strung=STRUNG, temperature=celsius(15))
    assert drop.si == pytest.approx(parabola, rel=0.001)


def test_a_span_does_not_sag_at_its_supports() -> None:
    drop = sag(DRAKE, at=0, span=SPAN, strung=STRUNG, temperature=celsius(15))
    assert drop.si == pytest.approx(0, abs=1e-9)


def test_a_span_sags_alike_either_side_of_its_middle() -> None:
    quarter, three = (
        sag(DRAKE, at=a, span=SPAN, strung=STRUNG, temperature=celsius(15)).si for a in (0.25, 0.75)
    )
    assert math.isclose(quarter, three, rel_tol=1e-12)


def test_a_span_sags_more_as_it_warms() -> None:
    sags = [
        sag(DRAKE, span=SPAN, strung=STRUNG, temperature=celsius(t))
        for t in (-20, 15, 50, 75, 100, 150, 200)
    ]
    assert sags == sorted(sags)


def test_above_its_knee_its_core_alone_holds_it() -> None:  # its aluminum slack, its steel not
    w, s = weight(DRAKE).si, SPAN.si

    def length(h: float) -> float:
        return 2 * h / w * math.sinh(s * w / (2 * h))

    def mean(h: float) -> float:
        return h * (s + h / w * math.sinh(s * w / h)) / (2 * length(h))

    parts = [
        (k.si, strand.material.expansion.si)
        for k, strand in zip(stiffness(DRAKE), DRAKE.strands, strict=True)
    ]
    held = STRUNG.tension.si
    unstressed = length(held) / (1 + mean(held) / sum(k for k, _ in parts))
    hot = tension(DRAKE, span=SPAN, strung=STRUNG, temperature=celsius(200)).si
    (aluminum, k_a), (steel, k_s) = (
        (length(hot) / (unstressed * (1 + a * 185)) - 1, k) for k, a in parts
    )
    assert aluminum < 0 < steel
    assert k_s * steel == pytest.approx(mean(hot), rel=1e-9)
    assert k_a > k_s


@pytest.mark.parametrize(
    ("conductor", "core", "rated"),
    [  # ASTM B232, table 1, class C coating; ASTM B231, table 1, class AA and class A
        (DRAKE, SteelGC2, 29_600),
        (ARBUTUS, None, 13_900),
        (LILAC, None, 14_300),
        # B399, tables 1 and 2: class A; upper wire-diameter boundary; 37 and 61 wires
        (AKRON, None, 1_110),
        (ALLIANCE, None, 8_560),
        (FLINT, None, 24_400),
        (KCMIL_1750_61, None, 56_900),
        # B524, table 7: its 6201 wires at 95% of their tensile strength (8.1)
        (KCMIL_3000_72_19, None, 60_700),
        (KCMIL_30_58_4_3, None, 826),
    ],
    ids=lambda value: value.title if isinstance(value, Conductor) else None,
)
def test_rated_strength_is_its_standard_s(
    conductor: Conductor, core: type[Steel] | None, rated: float
) -> None:  # ASTM B232, 10.1 and 10.2; ASTM B231, 9; ASTM B399, 9.3; ASTM B524, 8.1
    assert strength(conductor, core=core).to(lbf) == pytest.approx(rated)


GRADES = [  # Drake: B232-17, table 1, and B856-22, table 1, in pounds-force
    (SteelGA2, 31_500, 25_900),
    (SteelMA2, 31_500, 25_900),
    (SteelGA3, 33_500, 28_000),
    (SteelMA3, 33_500, 28_000),
    (SteelGA4, 34_900, 31_000),
    (SteelMA4, 34_900, 31_000),
    (SteelGA5, 35_400, 32_600),
    (SteelMA5, 35_400, 32_600),
]


@pytest.mark.parametrize(
    ("core", "rated"),
    [(core, acsr) for core, acsr, _ in GRADES],
    ids=lambda v: getattr(v, "name", None),
)
def test_acsr_rates_its_core_at_its_stress_at_1_percent_extension(
    core: type[Steel], rated: float
) -> None:
    assert strength(DRAKE, core=core).to(lbf) == pytest.approx(rated)


@pytest.mark.parametrize(
    ("core", "rated"),
    [(core, acss) for core, _, acss in GRADES],
    ids=lambda v: getattr(v, "name", None),
)
def test_acss_rates_its_core_at_its_tensile_strength(core: type[Steel], rated: float) -> None:
    assert strength(b856.DRAKE, core=core).to(lbf) == pytest.approx(rated)


@pytest.mark.parametrize(
    ("conductor", "core", "rated"),
    [  # IEC 61089:1991, annex D, tables D.1, D.4, D.8, D.15
        (iec.a1.CODE_500_37, None, 80.00),
        (iec.a1_syz.CODE_500_45_7, SteelS1A, 119.41),
        (iec.a1_syz.CODE_500_45_7, SteelS3A, 128.74),
        (iec.a1_a2.CODE_250_12_7, None, 53.92),
    ],
    ids=["A1", "A1/S1A", "A1/S3A", "A1/A2"],
)
def test_iec_rates_its_wires_within_annex_d_s_half_percent(
    conductor: Conductor, core: type[Steel] | None, rated: float
) -> None:  # 5.7: annex D's areas are nominal, the catalog's of its wires' printed diameters
    assert strength(conductor, core=core).to(kn) == pytest.approx(rated, rel=0.005)


def test_al3_is_rated_at_alfanar_s_5_55_kn() -> None:  # Overhead Conductors, p. 19, Box
    assert strength(BOX).to(kn) == pytest.approx(5.55)


@pytest.mark.parametrize("conductor", [ARBUTUS, AMES], ids=lambda c: c.title)
def test_a_conductor_s_class_leaves_its_rated_strength(conductor: B231 | B399) -> None:
    classes = (("A",), ("AA",), ("A", "AA"))
    rated = {strength(replace(conductor, classes=each)) for each in classes}
    assert rated == {strength(conductor)}


@pytest.mark.parametrize(
    ("conductor", "missing"),
    [(DRAKE, "CoatedSteel's extension stress"), (b856.DRAKE, "CoatedSteel's tensile strength")],
    ids=["ACSR", "ACSS"],
)
def test_a_core_whose_grade_its_design_leaves_open_is_rated_only_at_a_grade(
    conductor: Conductor, missing: str
) -> None:
    with pytest.raises(Missing, match=missing):
        strength(conductor)


@pytest.mark.parametrize(
    ("conductor", "core"),
    [(ARBUTUS, SteelGA2), (DRAKE, SteelS1A), (c49.MALLARD, SteelGA2)],  # no core; IEC's; CSA's
    ids=["ASTM B231", "ASTM B232", "CSA C49"],
)
def test_a_core_of_a_grade_its_standard_does_not_name_is_refused(
    conductor: Conductor, core: type[Steel]
) -> None:
    with pytest.raises(ValueError, match=f"names no core of {core.__name__}"):
        strength(conductor, core=core)


def test_a_conductor_without_its_rating_factors_has_no_strength() -> None:  # 3/4, off B232's
    with pytest.raises(Missing, match="rating factors"):
        strength(BANTAM, core=SteelGA2)
