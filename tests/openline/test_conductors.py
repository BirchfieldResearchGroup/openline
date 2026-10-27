"""openline.types.conductors and the conductors openline.conductors lists: how each standard lays
its wires, in rings or in trapezoidal bands, at its lay ratios and the way each turns; how a
conductor is sized and named, and its designation written; and that every listed conductor names
its standard. Their impedance is test_electrical's, their mass and strength test_mechanical's."""

import math
from dataclasses import replace

import pytest

from openline import conductors
from openline.conductors import iec
from openline.conductors.astm import a460_30hs, b416, b778, b856
from openline.conductors.astm.b231 import ARBUTUS
from openline.conductors.astm.b232 import DRAKE
from openline.conductors.astm.b399 import AMES, FLINT
from openline.conductors.astm.b524 import MM2_250_24_13
from openline.types import Missing
from openline.types.conductors import Conductor, Stranding
from openline.types.conductors.astm import B231, B232, B399, B856
from openline.types.conductors.designations import Code, Designation, Gauge, Kcmil, Mm2, WireGauge
from openline.types.conductors.strands import (
    Band,
    Center,
    Hand,
    Helical,
    HelicalBand,
    Helix,
    LayRatio,
    Ring,
    Round,
    Trapezoidal,
    layout,
)
from openline.types.materials import Aluminum1350H19
from openline.types.units import equivalent, inch, kcmil, mm


def ratios(conductor: Conductor) -> list[float]:
    """Each laid layer's lay over its outside diameter, from the center out."""
    return [
        layer.lay / (2 * layer.outer_radius)
        for layer in conductor.layers
        if isinstance(layer, Helix | HelicalBand)
    ]


def tulip() -> Trapezoidal[Aluminum1350H19]:
    """ASTM B778-22, table 1, Tulip/TW: 17 wires of 336.4 kcmil in 2 layers, 0.612 in across."""
    return Trapezoidal(
        Aluminum1350H19, 17, equivalent(kcmil(336.4), 17), layers=2, outside_diameter=inch(0.612)
    )


def test_26_7_lies_as_a_center_wire_and_rings_of_6_10_and_16() -> None:  # ASTM B232, table 1
    assert [(type(layer), len(layer.wires)) for layer in DRAKE.layers] == [
        (Center, 1),
        (Helix, 6),
        (Helix, 10),
        (Helix, 16),
    ]


def test_drake_takes_b232_s_stranding_for_26_7() -> None:  # table 6; table 5, class AA rows
    aluminum = Stranding((LayRatio(10, 13), LayRatio(10, 16)), 0.025, 0.93)
    assert DRAKE.stranding == (aluminum, Stranding((LayRatio(16, 26),), 0.004, 0.96))


def test_drake_s_aluminum_lies_at_b232_s_2_5_percent_increment() -> None:  # note 6
    aluminum = [layer for layer in DRAKE.layers if isinstance(layer, Helix)][1:]
    stretched = sum(len(helix.wires) * helix.factor for helix in aluminum) / 26
    assert stretched == pytest.approx(1.025, abs=1e-9)


@pytest.mark.parametrize(
    ("conductor", "hand"),
    [
        (DRAKE, Hand.RIGHT),  # ASTM B232, 8.3
        (ARBUTUS, Hand.RIGHT),  # ASTM B231, 7.4
        (MM2_250_24_13, Hand.RIGHT),  # ASTM B524, 6.2
        (b778.TULIP, Hand.RIGHT),  # ASTM B778-19, 6.5
        (b856.THRASHER, Hand.RIGHT),  # ASTM B856, 7.2
        (a460_30hs.NO_10_19, Hand.LEFT),  # ASTM B228, 6.3
        (b416.NO_10_19, Hand.LEFT),  # ASTM B416, 4.1.3
    ],
    ids=lambda value: value.title if isinstance(value, Conductor) else None,
)
def test_the_outer_layer_turns_its_standard_s_way_and_each_within_the_other(
    conductor: Conductor, hand: Hand
) -> None:
    laid = [layer for layer in reversed(conductor.layers) if isinstance(layer, Helical)]
    assert [layer.hand for layer in laid] == [
        hand.opposite if i % 2 else hand for i in range(len(laid))
    ]


@pytest.mark.parametrize("conductor", [ARBUTUS, FLINT], ids=lambda c: c.title)
def test_class_aa_lies_at_its_preferred_lay_ratio(conductor: Conductor) -> None:
    assert ratios(conductor) == pytest.approx([13.5, 13.5, 13.5])  # B231 and B399, 7.1


@pytest.mark.parametrize("conductor", [ARBUTUS, AMES], ids=lambda c: c.title)
def test_class_a_lies_at_the_middle_of_its_range(conductor: B231 | B399) -> None:
    # 7.2: 8 to 16, no preference; the middle, and the inner layers alike, an educated guess.
    covered = replace(conductor, classes=("A",))
    assert ratios(covered) == pytest.approx([12] * len(ratios(covered)))


def test_a_conductor_of_both_classes_lies_as_class_aa() -> None:
    assert replace(ARBUTUS, classes=("A", "AA")).layers == ARBUTUS.layers


@pytest.mark.parametrize(
    ("conductor", "outside_in"),
    [  # B856-03, table 2: 13.5, the middle of 10 to 17, on the inner aluminum layers is ours
        (b856.COCHIN, [12.5, 25]),
        (b856.BRAHMA, [12.5, 20, 25]),
        (b856.DRAKE, [11, 13, 25]),
        (b856.FALCON, [11, 13, 13.5, 20, 25]),
        (b856.THRASHER, [11, 13, 13.5, 13.5, 20, 25]),
    ],
    ids=lambda value: value.title if isinstance(value, Conductor) else None,
)
def test_acss_lies_at_its_preferred_lays_and_elsewhere_at_its_ranges_middles(
    conductor: Conductor, outside_in: list[float]
) -> None:
    assert ratios(conductor)[::-1] == pytest.approx(outside_in)


def test_an_increment_sets_the_lays_a_partial_preference_leaves_open(
    monkeypatch: pytest.MonkeyPatch,
) -> None:  # neither discarding the preference nor taking the increment from free rings alone
    assert DRAKE.stranding is not None
    preferred = Stranding((LayRatio(10, 13, 11), LayRatio(10, 16)), 0.025, 0.93)
    monkeypatch.setattr(B232, "strandings", {(26, 7): (preferred, DRAKE.stranding[1])})
    drake = replace(DRAKE)  # a design lays its wires once: this one under the patched table
    inner, outer = [layer for layer in drake.layers if isinstance(layer, Helix)][1:]
    assert outer.lay / (2 * outer.outer_radius) == pytest.approx(11)
    assert 10 <= inner.lay / (2 * inner.outer_radius) <= 16
    assert (16 * outer.factor + 10 * inner.factor) / 26 == pytest.approx(1.025, abs=1e-12)


@pytest.mark.parametrize(
    ("conductor", "row"),
    [(b856.MACAW, (45, 7)), (b856.SPOONBILL, (26, 7))],
    ids=lambda value: value.title if isinstance(value, Conductor) else None,
)
def test_acss_off_its_tables_takes_the_row_of_as_many_layers(
    conductor: Conductor, row: tuple[int, int]
) -> None:  # educated guess: 42/7 has table 3's factors alone, 22/7 neither table's
    assert conductor.stranding == B856.strandings[row]


def test_a_ring_of_two_metals_takes_one_lay() -> None:  # ASTM B524, 6.1, 6.2; table 6, note A
    helices = [layer for layer in MM2_250_24_13.layers if isinstance(layer, Helix)]
    assert [len(set(helix.wires)) for helix in helices] == [1, 2, 1]
    assert ratios(MM2_250_24_13) == pytest.approx([13.5, 13.5, 13.5])


def test_iec_lays_each_layer_at_the_mean_of_its_lay_ratios() -> None:  # 5.4.4, 5.4.5, 5.6.2
    # the core's 16 to 26, then the aluminium's 10 to 16 within and 10 to 14 outside
    assert ratios(iec.a1_syz.CODE_500_54_7) == pytest.approx([21, 13, 13, 12])


def test_iec_lays_a1_and_a2_wires_in_one_layer() -> None:  # 4/3: 4 of A1 and 3 of A2 about none
    (layer,) = [layer for layer in iec.a1_a2.CODE_16_4_3.layers if isinstance(layer, Helix)]
    assert len(set(layer.wires)) == 2


def test_aac_tw_lies_at_the_middles_of_its_ranges() -> None:  # ASTM B778-22, 6.1, 6.2
    assert ratios(b778.TULIP) == pytest.approx([13, 12])  # 10 to 16 within, 10 to 14 outside


def test_trapezoidal_wires_fill_their_layers_about_a_central_wire() -> None:  # B778, note 1
    center, *bands = layout((tulip(),))
    assert (type(center), [len(band.wires) for band in bands]) == (Center, [5, 11])


def test_trapezoidal_wires_reach_their_outside_diameter() -> None:
    *_, outer = layout((tulip(),))
    assert outer.outer_radius.si == pytest.approx(inch(0.306).si)


def test_trapezoidal_wires_fill_every_band_alike() -> None:  # IEC 62219, 3.7: one fill ratio
    wires = tulip()
    _, *bands = layout((wires,))
    fills = []
    for band in bands:
        assert isinstance(band, Band)
        held = math.pi * (band.outer.si**2 - band.inner.si**2)
        fills.append(len(band.wires) * wires.area.si / wires.count / held)
    assert fills == pytest.approx([fills[0]] * len(fills))


def test_a_thin_band_turns_as_a_ring() -> None:  # the area average tends to the secant
    ring = Ring(radius=mm(10), wires=())
    band = Band(inner=mm(9.999), outer=mm(10.001), wires=())
    assert band.factor_at(mm(200)) == pytest.approx(ring.factor_at(mm(200)), rel=1e-9)


def test_trapezoidal_wires_without_their_layers_lie_nowhere() -> None:
    with pytest.raises(Missing, match="layers"):
        layout((Trapezoidal(Aluminum1350H19, 17, equivalent(kcmil(336.4), 17)),))


def test_trapezoidal_wires_lie_outside_all_others() -> None:
    within = (Round(Aluminum1350H19, 6, mm(3)), tulip())  # strands run outside in
    with pytest.raises(ValueError, match="outside all others"):
        layout(within)


def test_round_wires_that_make_no_rings_lie_nowhere() -> None:  # 1, 7, 19 ... about a center
    with pytest.raises(Missing, match="no rings"):
        layout((Round(Aluminum1350H19, 5, mm(3)),))


def test_drake_is_b232_s_1_108_in_across() -> None:  # table 1, across its wires
    assert DRAKE.diameter.to(inch) == pytest.approx(1.108, abs=5e-4)


def test_drake_s_core_is_b232_s_0_408_in_across() -> None:  # table 1
    assert DRAKE.core_diameter.to(inch) == pytest.approx(0.408, abs=5e-4)


@pytest.mark.parametrize(
    ("conductor", "title"),
    [
        (DRAKE, "Drake, 795 kcmil, 26/7 (ASTM B232)"),
        (iec.a1.CODE_500_37, "500, 37 (IEC 61089, A1)"),  # no code word
    ],
    ids=["named", "unnamed"],
)
def test_a_title_is_code_words_size_wires_and_standard(conductor: Conductor, title: str) -> None:
    assert conductor.title == title


def test_every_listed_conductor_names_its_standard() -> None:
    unnamed = [c.title for c in conductors.of(Conductor) if not c.title.endswith(f"({c.standard})")]
    assert unnamed == []


DESIGNATIONS = [
    (Kcmil(795), "795 kcmil"),
    (Mm2(240), "240 mm²"),
    (Gauge(-3), "4/0 AWG"),
    (WireGauge(6), "No. 6"),
    (Code(250), "250"),
]


@pytest.mark.parametrize(("designation", "text"), DESIGNATIONS, ids=str)
def test_a_designation_prints_as_its_standard_writes_it(
    designation: Designation, text: str
) -> None:
    assert str(designation) == text


@pytest.mark.parametrize(("designation", "text"), DESIGNATIONS, ids=str)
def test_a_designation_reads_as_it_prints(designation: Designation, text: str) -> None:
    assert type(designation).parse(text) == designation


@pytest.mark.parametrize(
    ("designation", "text", "written"),
    [
        (Kcmil(30.58), "30.6 kcmil", True),  # rounded half up to the decimals written
        (Kcmil(795), "800 kcmil", False),  # written whole, so not rounded at all
        (Kcmil(795), "795 mm²", False),  # in another unit
    ],
    ids=str,
)
def test_a_designation_is_written_with_its_numbers_rounded_half_up(
    designation: Designation, text: str, written: bool
) -> None:
    assert designation.written_as(text) is written
