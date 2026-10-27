"""openline.electrical: a conductor's impedance by the one model of its wires, against closed forms
(Bessel's tables, a solid wire's limits, seven wires' GMR, a ring's solenoid) and documents, with
temperature and frequency; and a line's impedance and admittance between phases, against ATP's
for the IEEE PSRC's 230 kV line, as its wires sag, bundle, shield and hang, over a lossy earth
and at DC. The earth's integrals are test_earth's, propagation test_propagation's, and the
ratings, with IEEE 738, test_ratings's."""

import cmath
import math
from collections.abc import Iterable
from dataclasses import replace
from functools import cache

import pytest

from openline import conductors
from openline.conductors.astm import b779
from openline.conductors.astm.b231 import ARBUTUS
from openline.conductors.astm.b232 import BLUEBIRD, CARDINAL, DRAKE, TURKEY
from openline.conductors.bs.bs_en50182_al3 import BOX
from openline.conductors.csa import c49
from openline.electrical import (
    _bessel,
    _wires,
    admittance,
    gmr,
    impedance,
    internal_impedance,
    magnetized,
    parameters,
    resistance,
    resistivity,
    series,
    shunt,
)
from openline.mechanical import tension, weight
from openline.types import Missing
from openline.types.conductors import Conductor, Homogeneous
from openline.types.conductors.astm import B779
from openline.types.conductors.designations import Mm2
from openline.types.conductors.strands import Helix, Round
from openline.types.environment import Earth
from openline.types.lines import (
    Bundle,
    Circuit,
    Line,
    Phase,
    Phases,
    Placed,
    Shield,
    Strung,
    Suspended,
)
from openline.types.materials import Aluminum1350H19, Iron, Metal, Steel
from openline.types.parameters import Parameters
from openline.types.structures import Ground, Pole
from openline.types.structures.attachments import Hold, Mount, Wire
from openline.types.structures.geometry import Point
from openline.types.units import (
    MU_0,
    Admittance,
    Impedance,
    Temperature,
    celsius,
    ft,
    hz,
    inch,
    kn,
    kv,
    m,
    m_per_f,
    mm,
    ohm_m,
    ohm_per_km,
    ohm_per_m,
    s_per_m,
)


class Solid(Homogeneous[Round[Metal]]):
    """A conductor of one round wire."""

    standard = "one wire"


SOLID = Solid(code_words=(), designation=Mm2(314), wires=Round(Aluminum1350H19, 1, mm(20)))
# Modified Bessel functions, by order and argument: Abramowitz and Stegun, table 9.8.
I_TABLE = [(0, 1, 1.266065878), (1, 1, 0.565159104), (0, 5, 27.23987182)]
MEETING = _bessel.LARGE * cmath.exp(1j * math.pi / 4)  # where I's series meets its expansion


def skin(x: float) -> float:
    r"""The solid wire's resistance over its DC resistance at :math:`x = a\sqrt{\omega\mu/\rho}`,
    its radius :math:`a` over :math:`\sqrt 2` skin depths."""
    rho = resistivity(Aluminum1350H19, temperature=celsius(20)).si
    mu = MU_0 * Aluminum1350H19.relative_permeability
    frequency = (x / 0.01) ** 2 * rho / (2 * math.pi * mu)
    ac, dc = (
        internal_impedance(SOLID, temperature=celsius(20), frequency=hz(f)).resistance
        for f in (frequency, 0)
    )
    return ac / dc


def parallel(paths: list[_wires.Wire | _wires.Laid], frequency: float) -> complex:
    """Paths' impedance in parallel, in ohm/m."""
    ((z,),) = _wires.reduced(_wires.matrix(paths, frequency), [range(len(paths))])
    return z


def straight(x: float, y: float, radius: float) -> _wires.Wire:
    """A straight aluminum wire, its place and radius in millimeters."""
    rho, mu = Aluminum1350H19.resistivity.si, Aluminum1350H19.relative_permeability
    return _wires.Wire(x * 1e-3, y * 1e-3, radius * 1e-3, rho, mu)


MILE = 1609.344
# EMTP Reference Models for Transmission Line Relay Testing, p. 40, table 4: each conductor's
# height at the tower and at mid-span, in feet; B.7, L3_Full_Line.pch: the phase resistances and
# reactances of a 15-mile section, in ohm, and its capacitances, in uF, by row and column.
HEIGHTS = ((100.0, 73.0), (83.5, 56.5), (67.0, 40.0))
REPORTED = {
    (0, 0): (2.74694761, 19.8137317, 0.182160275),
    (1, 0): (1.32550570, 8.82314492, -0.0454680689),
    (1, 1): (2.76787292, 19.7886069, 0.193775227),
    (2, 0): (1.33607442, 7.54892738, -0.0215476823),
    (2, 1): (1.34686707, 8.79786722, -0.0413213989),
    (2, 2): (2.78969566, 19.7631744, 0.191971527),
}
RADIUS = inch(1.216) / 2  # Marigold's, from the diameter the benchmark reports
STRUNG = 28.0  # kN, at 15 °C
TAUT = 1e9  # kN: a line strung so tight it does not sag
CARSON = Earth(ohm_m(50), 1.0)  # conduction alone, for the series impedance
EARTH = Earth(ohm_m(50), 10.0)
LOSSY, PERFECT = Earth(ohm_m(1000), 10.0), Earth(ohm_m(1e-9), 1.0)
TWIN = Bundle(conductor=DRAKE, count=2, spacing=m(0.457))


def psrc() -> list[Placed]:
    """The PSRC's conductors at their mean height, a third of their sag above mid-span."""
    return [
        Placed(RADIUS, Point(ft(0), ft(0), ft(top - 2 / 3 * (top - middle))))
        for top, middle in HEIGHTS
    ]


def flat(rows: Iterable[Iterable[complex]]) -> list[complex]:
    """A matrix's entries, row by row."""
    return [value for row in rows for value in row]


def tower(hold: Hold = Hold.STRAIN, lower: float = 0) -> Pole[Steel, Ground]:
    """A pole holding three phases one above another, as the PSRC's line, ``lower`` meters below
    its tower heights, and a shield wire."""
    shield = Mount(Wire.SHIELD, Point(ft(0), ft(0), ft(115)), Hold.CLAMP)
    tops = (Point(ft(0), ft(0), ft(top) - m(lower)) for top, _ in HEIGHTS)
    phases = (Mount(Wire.PHASE, point, hold) for point in tops)
    return Pole(
        name="PSRC 230 kV",
        datum=Ground((m(0),)),
        voltages=(kv(230),),
        line_angles=(),
        attachments=(shield, *phases),
        material=Steel,
        crossarms=(),
    )


def line(
    structure: Pole[Steel, Ground] | None = None,
    conductor: Conductor | Bundle = DRAKE,
    shields: bool = False,
    tension: float = STRUNG,
    earth: Earth = EARTH,
) -> Line:
    """A line of three phases on ``structure``, 300 m spans, each wire strung to ``tension`` kN
    at 15 °C, over ``earth``."""
    structure = structure or tower()
    strung = Strung(kn(tension), celsius(15))
    phases = tuple(
        Phase(conductor=conductor, attachments=(a,), strung=strung) for a in structure.phases
    )
    shield = (Shield(conductor=DRAKE, attachment=a, strung=strung) for a in structure.shields)
    return Line(
        structure=structure,
        height=m(0),
        span=m(300),
        circuits=(Circuit(phases=phases),),
        shields=tuple(shield) if shields else (),
        earth=earth,
    )


@cache
def z(given: Line, at: float = 75, frequency: float = 60) -> Phases[Impedance]:
    """A line's impedance at ``at`` °C and ``frequency`` Hz, found once."""
    return impedance(given, temperature=celsius(at), frequency=hz(frequency))


@cache
def y(given: Line, at: float = 75, frequency: float = 60) -> Phases[Admittance]:
    """A line's admittance at ``at`` °C and ``frequency`` Hz, found once."""
    return admittance(given, temperature=celsius(at), frequency=hz(frequency))


def at_mean_height() -> Line:
    """The line strung taut at its mean catenary height at 75 °C, integrated analytically."""
    horizontal = tension(
        DRAKE, span=m(300), strung=Strung(kn(STRUNG), celsius(15)), temperature=celsius(75)
    )
    c = horizontal.si / weight(DRAKE).si
    a = 300 / (2 * c)
    drop = c * (math.cosh(a) - math.sinh(a) / a)
    return line(tower(lower=drop), tension=TAUT)


@pytest.mark.parametrize(("order", "x", "value"), I_TABLE)
def test_i_meets_its_table(order: int, x: float, value: float) -> None:
    assert (_bessel.i(order, x) * cmath.exp(x)).real == pytest.approx(value, rel=1e-8)


@pytest.mark.parametrize("order", [0, 1])
def test_i_s_series_and_expansion_agree_where_they_meet(order: int) -> None:
    near = _bessel.i(order, MEETING * 0.999999)
    far = _bessel.i(order, MEETING)
    assert abs(near / far - 1) < 1e-6


def test_a_solid_wire_s_resistance_rises_as_x4_over_192_at_low_frequency() -> None:
    assert skin(0.5) - 1 == pytest.approx(0.5**4 / 192, rel=1e-3)


def test_a_solid_wire_s_resistance_follows_its_skin_depth_at_high_frequency() -> None:
    assert skin(100) == pytest.approx(100 / (2 * math.sqrt(2)) + 0.25, rel=1e-3)


def test_a_solid_wire_s_gmr_is_its_radius_times_e_to_the_minus_a_quarter() -> None:
    radius = gmr(SOLID, temperature=celsius(20), frequency=hz(1))
    quarter = math.exp(-Aluminum1350H19.relative_permeability / 4)
    assert radius.si == pytest.approx(0.01 * quarter, rel=1e-6)


def test_seven_wires_have_the_classical_gmr() -> None:  # 2.1767 times a wire's radius
    ring = [
        straight(2 * math.cos(k * math.pi / 3), 2 * math.sin(k * math.pi / 3), 1) for k in range(6)
    ]
    within = parallel([straight(0, 0, 1), *ring], 1.0)
    assert math.exp(-within.imag / MU_0) / 1e-3 == pytest.approx(2.1767, abs=2e-4)


def test_a_ring_is_a_solenoid() -> None:  # mu_0 pi R^2 / lay^2, its wires' field lengthened by m
    radius, lay, count = 0.01, 0.3, 12
    helix = Helix(
        radius=m(radius),
        wires=(Round(Aluminum1350H19, count, mm(2)),) * count,
        lay=m(lay),
        hand=None,
    )
    places = [
        (radius * math.cos(2 * math.pi * k / count), radius * math.sin(2 * math.pi * k / count))
        for k in range(count)
    ]
    rho, mu = Aluminum1350H19.resistivity.si, 1.0
    unturned: list[_wires.Wire | _wires.Laid] = [
        _wires.Wire(x, y, 1e-3, rho, mu) for x, y in places
    ]
    laid: list[_wires.Wire | _wires.Laid] = [
        _wires.Laid(_wires.Wire(x, y, 1e-3, rho, mu), radius, lay, 1, helix.factor)
        for x, y in places
    ]
    frequency = 0.01
    turning, still = (parallel(p, frequency) for p in (laid, unturned))
    added = (turning.imag - still.imag) / (2 * math.pi * frequency)
    within = (helix.factor - 1) * MU_0 / (8 * math.pi) / count
    assert added == pytest.approx(MU_0 * math.pi * radius**2 / lay**2 + within, rel=1e-3)


def test_gmr_nears_the_outside_radius_as_frequency_rises() -> None:  # current crowds outward
    low, high = (gmr(DRAKE, temperature=celsius(75), frequency=hz(f)) for f in (60, 1000))
    assert low < high < DRAKE.diameter / 2


def test_gmr_needs_a_positive_frequency() -> None:
    with pytest.raises(ValueError, match="positive frequency"):
        gmr(DRAKE, temperature=celsius(75), frequency=hz(0))


def test_a_conductor_s_resistance_is_its_internal_impedance_s_real_part() -> None:
    at, frequency = celsius(75), hz(60)
    own = internal_impedance(DRAKE, temperature=at, frequency=frequency)
    assert resistance(DRAKE, temperature=at, frequency=frequency) == own.resistance


@pytest.mark.parametrize(
    ("conductor", "magnetic"),
    [  # IEEE 738-2023, 4.4.6.3
        (DRAKE, False),  # 26/7: two layers of aluminum
        (CARDINAL, True),  # 54/7: three
        (TURKEY, True),  # 6/1: one
        (BLUEBIRD, False),  # 84/19: four
        (ARBUTUS, False),  # no steel core
    ],
    ids=lambda value: value.title if isinstance(value, Conductor) else None,
)
def test_a_steel_core_under_an_odd_number_of_aluminum_layers_is_magnetized(
    conductor: Conductor, magnetic: bool
) -> None:
    assert magnetized(conductor) is magnetic


def test_trapezoidal_layers_magnetize_a_core_as_rings_do() -> None:  # B779's tables' layers
    astray = [
        c.title
        for c in conductors.of(B779)
        if c.outer.layers is not None and magnetized(c) != (c.outer.layers % 2 == 1)
    ]
    assert astray == []


def test_a_core_under_layers_no_document_gives_is_taken_as_magnetized() -> None:
    unlayered = replace(b779.DRAKE.outer, layers=None, outside_diameter=None)
    assert magnetized(replace(b779.DRAKE, outer=unlayered))


def test_a_conductor_whose_standard_gives_no_direction_of_lay_has_no_impedance(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(B779, "hand", None)
    unturned = replace(b779.DRAKE, code_words=())  # a design of its own: Drake's impedance is kept
    with pytest.raises(Missing, match="direction of lay"):
        internal_impedance(unturned, temperature=celsius(20), frequency=hz(60))


def test_a_conductor_whose_rings_have_no_lay_has_no_impedance() -> None:  # 3/4: Al and steel
    with pytest.raises(Missing, match="lay"):
        internal_impedance(c49.BANTAM, temperature=celsius(75), frequency=hz(60))


@pytest.mark.parametrize(("kelvin", "given"), [(273, 8.57e-8), (300, 9.98e-8)])
def test_iron_s_resistivity_is_the_crc_handbook_s(kelvin: float, given: float) -> None:
    # 97th ed., p. 12-42, its 293 K taken as 20 °C, and linear from there
    assert resistivity(Iron, temperature=Temperature(kelvin)).si == pytest.approx(given, rel=2e-3)


def test_al3_s_dc_resistance_is_alfanar_s() -> None:  # Overhead Conductors, p. 19, Box
    dc = internal_impedance(BOX, temperature=celsius(20), frequency=hz(0)).resistance
    assert dc.to(ohm_per_km) == pytest.approx(1.748, rel=0.001)


def test_al3_s_dc_resistance_rises_36_percent_in_100_k() -> None:  # EN 50183, clause 5: 0.0036
    cold, hot = (
        internal_impedance(BOX, temperature=celsius(t), frequency=hz(0)).resistance
        for t in (20, 120)
    )
    assert hot / cold == pytest.approx(1.36)


def test_the_psrc_line_s_impedance_is_atp_s() -> None:  # ATP's feet and miles: US survey's, 2e-6
    radius = RADIUS.si
    rho = 0.09222 / MILE * math.pi * radius**2  # solid, of its DC resistance at 50 °C
    own = _wires.own(_wires.Wire(0.0, 0.0, radius, rho, 1.0), 60.0)
    placed = psrc()
    matrix = [
        [
            (own if a == b else 0)
            + series.external(a, b, frequency=hz(60)).to(ohm_per_m)
            + series.earth(a, b, frequency=hz(60), earth=CARSON).to(ohm_per_m)
            for b in placed
        ]
        for a in placed
    ]
    phases = _wires.reduced(matrix, [[0], [1], [2]])
    for (i, k), (r, x, _) in REPORTED.items():
        section = phases[i][k] * 15 * MILE
        assert (section.real, section.imag) == pytest.approx((r, x), rel=1e-5)


def test_the_psrc_line_s_capacitance_is_atp_s() -> None:
    placed = psrc()
    p = [[shunt.external(a, b).to(m_per_f) for b in placed] for a in placed]
    c = _wires.collected(p, [[0], [1], [2]])
    for (i, k), (_, _, capacitance) in REPORTED.items():
        assert c[i][k].real * 15 * MILE * 1e6 == pytest.approx(capacitance, rel=1e-5)


def test_a_taut_line_s_impedance_is_its_wires_and_their_fields_at_its_attachments() -> None:
    own = internal_impedance(DRAKE, temperature=celsius(75), frequency=hz(60)).to(ohm_per_m)
    placed = [Placed(DRAKE.diameter / 2, a.point) for a in tower().phases]
    expected = [
        [
            series.external(a, b, frequency=hz(60)).to(ohm_per_m)
            + series.earth(a, b, frequency=hz(60), earth=EARTH).to(ohm_per_m)
            + (own if a == b else 0)
            for b in placed
        ]
        for a in placed
    ]
    assert flat(z(line(tension=TAUT)).to(ohm_per_m)) == pytest.approx(flat(expected), rel=1e-6)


def test_a_taut_line_s_admittance_is_its_capacitance_at_its_attachments() -> None:
    placed = [Placed(DRAKE.diameter / 2, a.point) for a in tower().phases]
    p = [
        [
            shunt.external(a, b).to(m_per_f)
            + shunt.earth(a, b, frequency=hz(60), earth=EARTH).to(m_per_f)
            for b in placed
        ]
        for a in placed
    ]
    expected = [2j * math.pi * 60 * each for each in flat(_wires.collected(p, [[0], [1], [2]]))]
    assert flat(y(line(tension=TAUT)).to(s_per_m)) == pytest.approx(expected, rel=1e-9, abs=0)


def test_a_phase_s_own_susceptance_is_positive_and_its_mutual_negative() -> None:
    admittances = y(line())
    assert admittances[0][0].susceptance.si > 0 > admittances[0][1].susceptance.si


def test_a_line_s_impedance_is_reciprocal() -> None:
    rows = z(line()).to(ohm_per_m)
    assert flat(rows) == pytest.approx(flat(zip(*rows, strict=True)), rel=1e-12)


def test_a_line_s_admittance_is_reciprocal() -> None:
    rows = y(line()).to(s_per_m)
    assert flat(rows) == pytest.approx(flat(zip(*rows, strict=True)), rel=1e-12, abs=0)


def test_the_earth_adds_to_a_phase_s_own_resistance() -> None:
    own = internal_impedance(DRAKE, temperature=celsius(75), frequency=hz(60))
    assert z(line())[0][0].resistance > own.resistance


def test_a_sagging_line_s_impedance_is_at_its_mean_catenary_height() -> None:
    sagging, mean = z(line()), z(at_mean_height())
    assert flat(sagging.to(ohm_per_m)) == pytest.approx(flat(mean.to(ohm_per_m)), rel=1e-9, abs=0)


def test_a_sagging_line_s_admittance_is_at_its_mean_catenary_height() -> None:
    sagging, mean = y(line()), y(at_mean_height())
    assert flat(sagging.to(s_per_m)) == pytest.approx(flat(mean.to(s_per_m)), rel=1e-9, abs=0)


def test_a_warmer_line_sags_lower_its_mutual_reactance_less() -> None:
    assert z(line(), at=150)[0][1].reactance < z(line(), at=15)[0][1].reactance


def test_a_warmer_line_sags_nearer_the_earth_its_own_susceptance_more() -> None:
    assert y(line(), at=150)[0][0].susceptance > y(line(), at=15)[0][0].susceptance


def test_a_bundle_shares_its_phase_s_current() -> None:
    single, bundled = (z(given)[0][0] for given in (line(), line(conductor=TWIN)))
    assert bundled.resistance < single.resistance
    assert bundled.reactance < single.reactance


def test_a_bundle_holds_more_charge() -> None:
    assert y(line(conductor=TWIN))[0][0].susceptance > y(line())[0][0].susceptance


def test_a_shield_wire_s_return_current_lowers_the_phases_mutual_reactance() -> None:
    assert z(line(shields=True))[0][1].reactance < z(line())[0][1].reactance


def test_a_grounded_shield_wire_draws_charge() -> None:
    assert y(line(shields=True))[0][0].susceptance > y(line())[0][0].susceptance


def test_at_dc_a_line_s_impedance_is_its_conductors_resistance_alone() -> None:
    dc = z(line(), at=20, frequency=0)
    own = internal_impedance(DRAKE, temperature=celsius(20), frequency=hz(0))
    assert dc[0][0].resistance.si == pytest.approx(own.resistance.si, rel=1e-12)
    assert abs(dc[0][1].to(ohm_per_m)) < 1e-15  # no field couples them, nor the earth


def test_at_dc_a_line_has_no_admittance() -> None:
    dc = y(line(), at=20, frequency=0)
    assert {(each.conductance.si, each.susceptance.si) for row in dc for each in row} == {(0, 0)}


def test_a_suspended_phase_hangs_its_drop_below_its_mounts() -> None:
    hung = tower(Hold.SUSPENSION)
    strung = Strung(kn(STRUNG), celsius(15))
    phases = tuple(
        Suspended(conductor=DRAKE, attachments=(a,), strung=strung, drop=m(2)) for a in hung.phases
    )
    suspended = replace(line(), structure=hung, circuits=(Circuit(phases=phases),))
    assert z(suspended) == z(line(tower(lower=2)))


def test_a_line_whose_wires_sag_to_the_earth_has_no_impedance() -> None:
    slack = replace(line(tension=5), span=m(2000))
    with pytest.raises(ValueError, match="sags to the earth"):
        impedance(slack, temperature=celsius(75), frequency=hz(60))


def test_at_power_frequency_a_lossy_earth_holds_charge_as_a_perfect_one() -> None:
    lossy, perfect = (y(line(earth=earth))[0][0] for earth in (LOSSY, PERFECT))
    assert lossy.susceptance.si == pytest.approx(perfect.susceptance.si, rel=1e-5, abs=0)


def test_at_high_frequency_a_lossy_earth_takes_charge_through_its_losses() -> None:
    assert y(line(earth=LOSSY), frequency=1e6)[0][0].conductance.si > 0


def test_at_high_frequency_a_lossy_earth_holds_less_charge_than_a_perfect_one() -> None:
    lossy, perfect = (y(line(earth=earth), frequency=1e6)[0][0] for earth in (LOSSY, PERFECT))
    assert lossy.susceptance < perfect.susceptance


def test_a_line_s_parameters_are_its_impedance_and_admittance() -> None:
    found = parameters(line(), temperature=celsius(75), frequency=hz(60))
    assert found == Parameters(impedance=z(line()), admittance=y(line()))
