"""openline.types.units: quantities stored in SI, each of one kind. A quantity keeps to its kind,
prints as a number and its unit's symbol, and reads in any unit of its kind; temperatures neither
add nor subtract. Every unit has one symbol, ``SYMBOLS``; the inch-pound units keep their exact
definitions, and AWG gauges their diameters."""

import inspect
from collections import Counter
from collections.abc import Callable
from typing import Any

import pytest

from openline import units as u

type UnitFunction = Callable[[float], u.Quantity[Any]]


def is_unit(value: object) -> bool:
    """Whether ``value`` is a unit: a function of a number, ``value``, giving a quantity."""
    return inspect.isfunction(value) and list(inspect.signature(value).parameters) == ["value"]


UNITS: list[UnitFunction] = [f for name in u.__all__ if is_unit(f := getattr(u, name))]
SI: list[type[u.Unit]] = [
    unit
    for name in u.__all__
    if isinstance(unit := getattr(u, name), type)
    and issubclass(unit, u.Unit)
    and unit is not u.Unit
]


def read(text: str) -> u.Quantity[Any]:
    """A printed quantity read back: its number in the unit its symbol names, after a space, but
    a degree of angle's, against the number."""
    number, symbol = (text[:-1], "°") if text.endswith("°") else text.split(" ", 1)
    return u.SYMBOLS[symbol](float(number))


def test_every_unit_has_exactly_one_symbol() -> None:
    named = Counter(unit.__name__ for unit in u.SYMBOLS.values())
    assert named == Counter(unit.__name__ for unit in UNITS)


def test_a_unit_s_symbol_names_it() -> None:
    assert [unit.__name__ for unit in UNITS if u.SYMBOLS[u.symbol(unit)] is not unit] == []


def test_no_two_si_units_share_a_symbol() -> None:
    assert len({unit.symbol for unit in SI}) == len(SI)


def test_an_si_unit_s_symbol_names_the_unit_that_measures_in_it() -> None:  # "Ω·m": ohm_m
    named = [unit for unit in SI if unit.symbol in u.SYMBOLS]
    one = [(u.SYMBOLS[unit.symbol](0).si, u.SYMBOLS[unit.symbol](1).si) for unit in named]
    assert one == [(0, 1)] * len(named)


def test_a_quantity_prints_as_a_number_and_its_unit_s_symbol() -> None:
    printed = {unit.__name__: str(unit(1.234)) for unit in UNITS}
    unread = {
        name: text
        for (name, text), unit in zip(printed.items(), UNITS, strict=True)
        if read(text).si != pytest.approx(unit(1.234).si, rel=5e-4, abs=0)  # four figures
    }
    assert unread == {}


def test_a_degree_of_angle_prints_against_its_number() -> None:  # as SI writes it, unlike °C
    assert (str(u.degrees(90)), str(u.celsius(75))) == ("90°", "75 °C")


def test_a_length_prints_in_millimeters_below_a_meter() -> None:
    assert (str(u.inch(1.108)), str(u.m(300))) == ("28.14 mm", "300 m")


def test_a_quantity_takes_a_format_for_its_number() -> None:
    assert f"{u.inch(1.108):.1f}" == "28.1 mm"


def test_a_quantity_reads_in_any_unit_of_its_kind() -> None:
    assert u.mm(28.1432).to(u.inch) == pytest.approx(1.108)


def test_a_temperature_reads_from_its_unit_s_own_zero() -> None:
    assert (u.celsius(75).si, u.Temperature(348.15).to(u.celsius)) == pytest.approx((348.15, 75))


def test_a_reactance_reads_in_a_resistance_s_units() -> None:
    reactance = u.ReactancePerLength.of(u.ohm_per_kft(0.0756))
    assert reactance.to(u.ohm_per_kft) == pytest.approx(0.0756)


@pytest.mark.parametrize(
    ("unit", "si"),
    [  # NIST SP 811, appendix B: each exact, or of exact factors and standard gravity
        (u.inch, 0.0254),
        (u.ft, 0.3048),
        (u.mi, 1609.344),
        (u.cmil, 5.067074790974977e-10),
        (u.lb_per_kft, 0.45359237 / 304.8),
        (u.lbf, 4.4482216152605),
        (u.psi, 6894.757293168361),
        (u.ohm_per_kft, 1 / 304.8),
        (u.ft_per_s, 0.3048),
        (u.w_per_ft2, 1 / 0.3048**2),
    ],
    ids=lambda value: getattr(value, "__name__", None),
)
def test_an_inch_pound_unit_keeps_its_exact_definition(unit: UnitFunction, si: float) -> None:
    assert unit(1).si == pytest.approx(si, rel=1e-12, abs=0)


@pytest.mark.parametrize(
    ("gauge", "diameter"),  # ASTM B258, table 1, in inches to four decimals
    [("4/0", 0.4600), ("1/0", 0.3249), ("4", 0.2043), ("10", 0.1019), ("12", 0.0808)],
)
def test_an_awg_gauge_is_astm_b258_s_diameter(gauge: str, diameter: float) -> None:
    assert u.awg(gauge).to(u.inch) == pytest.approx(diameter, abs=5e-5)


def test_a_quantity_scales_by_a_number() -> None:
    assert 0.2 * u.kn(140) == u.kn(28)


def test_quantities_of_one_kind_divide_to_a_number() -> None:
    assert u.mm(10) / u.mm(20) == 0.5


def test_quantities_of_different_kinds_do_not_add() -> None:
    with pytest.raises(TypeError):
        u.mm(10) + u.mm2(10)  # type: ignore[operator]


def test_a_resistance_and_a_reactance_do_not_add_though_they_share_a_unit() -> None:
    with pytest.raises(TypeError):
        u.ohm_per_km(1) + u.ReactancePerLength(1)  # type: ignore[operator]


def test_a_quantity_scales_only_by_a_number() -> None:
    with pytest.raises(TypeError, match="only by a number"):
        u.kn(1) * u.kn(1)  # type: ignore[operator]


def test_a_quantity_compares_only_with_its_kind() -> None:
    with pytest.raises(TypeError):
        u.mm2(1) <= 0.07  # type: ignore[operator]  # noqa: B015


def test_a_temperature_neither_adds_nor_subtracts() -> None:  # its scale starts from 0 K
    with pytest.raises(TypeError, match="don't add"):
        u.celsius(75) + u.celsius(20)
    with pytest.raises(TypeError, match="don't subtract"):
        u.celsius(75) - u.celsius(20)


def test_a_complex_quantity_reads_in_a_unit_as_a_complex_number() -> None:
    z = u.Impedance(u.ohm_per_km(0.1), u.ReactancePerLength.of(u.ohm_per_km(0.4)))
    y = u.Admittance(u.us_per_km(0.01), u.SusceptancePerLength.of(u.us_per_km(3.3)))
    p = u.PotentialCoefficient(u.km_per_uf(145), u.Elastance(0))
    gamma = u.PropagationConstant(u.per_km(0.1), u.PhaseConstant.of(u.per_km(2)))
    yc = u.CharacteristicAdmittance(u.siemens(0.003), u.Susceptance(-0.001))
    read = (z.to(u.ohm_per_km), y.to(u.us_per_km), p.to(u.km_per_uf), gamma.to(u.per_km))
    assert (*read, yc.to(u.siemens)) == pytest.approx(
        (0.1 + 0.4j, 0.01 + 3.3j, 145, 0.1 + 2j, 0.003 - 0.001j)
    )


def test_a_complex_quantity_prints_both_parts_in_one_unit() -> None:
    impedance = u.Impedance(u.ohm_per_km(0.08559), u.ReactancePerLength.of(u.ohm_per_km(0.01744)))
    admittance = u.Admittance(u.us_per_km(0), u.SusceptancePerLength.of(u.us_per_km(-3.315)))
    assert (str(impedance), str(admittance)) == ("0.08559 + j0.01744 Ω/km", "0 - j3.315 µS/km")
