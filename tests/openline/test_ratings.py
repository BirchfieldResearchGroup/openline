"""openline.ratings, by IEEE Std 738-2023 (openline.electrical.ieee738), and the records it takes
(openline.types.ratings): its own sample calculations (4.6) and annex C, for Drake 26/7 ACSR at
100 °C in 40 °C air, a 0.61 m/s crosswind, and the sun at 11:00 on June 10 at 30° north, on a
line running east-west, in clear air at sea level. The samples state Drake's diameter, its AC
resistance, 7.283e-5 Ω/m at 25 °C and 8.688e-5 Ω/m at 75 °C (4.6.1.1), and its heat capacity,
1310 J/(m·°C) (4.6.3), so each is rated as they state it; then a schedule's temperatures, and
what a rating takes and refuses."""

from dataclasses import replace
from datetime import datetime, timedelta

import pytest

from openline import ratings
from openline.conductors.astm import b232
from openline.electrical.ieee738 import IEEE738
from openline.ratings import (
    ampacity,
    core_temperature,
    heat_capacity,
    temperature,
    temperature_profile,
)
from openline.types import Missing
from openline.types.conductors import Surface
from openline.types.environment import Atmosphere, Environment, Sun
from openline.types.ratings import Interval, Thermal
from openline.types.units import (
    Current,
    ResistancePerLength,
    Temperature,
    amperes,
    celsius,
    degrees,
    hz,
    j_per_m_k,
    m,
    m_per_s,
    mm,
    ohm_per_km,
    w_per_m2,
    w_per_m_k,
)

AC = hz(60)
STATED = {celsius(25): ohm_per_km(0.07283), celsius(75): ohm_per_km(0.08688)}
DRAKE = Thermal.from_resistances(
    frequency=AC,
    diameter=mm(28.14),
    resistances=STATED,
    heat_capacity=j_per_m_k(1310),
    core_diameter=b232.DRAKE.core_diameter,
)
# 4.6.3 b): "assume that the increase in resistance is linear past 100 °C"
HOTTER = Thermal.from_resistances(
    diameter=DRAKE.diameter,
    frequency=AC,
    resistances={**STATED, celsius(200): ohm_per_km(0.1220)},
    heat_capacity=DRAKE.heat_capacity,
    core_diameter=DRAKE.core_diameter,
)
SUN = Sun(
    latitude=degrees(30),
    azimuth=degrees(90),
    when=datetime(2026, 6, 10, 11),
    atmosphere=Atmosphere.CLEAR,
)
ENVIRONMENT = Environment(
    air=celsius(40),
    wind=m_per_s(0.61),
    wind_angle=degrees(90),
    sun=SUN,
    elevation=m(0),
)
NIGHT = replace(  # 4.6.5: at 50 °C in 25 °C air, a 2.1 m/s wind at 62°, no sun
    ENVIRONMENT, air=celsius(25), wind=m_per_s(2.1), wind_angle=degrees(62), sun=w_per_m2(0)
)
SURFACE = Surface(emissivity=0.8, absorptivity=0.8)
HOUR = timedelta(hours=1)


def test_ieee_738_s_drake_loses_82_10_w_per_m_by_convection() -> None:  # 4.6.1
    assert IEEE738.convection(DRAKE, celsius(100), ENVIRONMENT).si == pytest.approx(82.10, rel=1e-3)


def test_ieee_738_s_drake_loses_39_11_w_per_m_by_radiation() -> None:  # 4.6.1
    radiated = IEEE738.radiation(DRAKE, celsius(100), ENVIRONMENT, surface=SURFACE)
    assert radiated.si == pytest.approx(39.11, rel=1e-3)


def test_ieee_738_s_drake_gains_22_45_w_per_m_from_the_sun() -> None:  # 4.6.1
    solar = SURFACE.absorptivity * IEEE738.flux(SUN, m(0)).si * DRAKE.diameter.si
    assert solar == pytest.approx(22.45, rel=1e-3)


def test_ieee_738_s_drake_resists_9_391e_5_ohm_per_m_at_100_c() -> None:  # 4.6.1, equation 33
    assert IEEE738.resistance(DRAKE, celsius(100), amperes(1025)).si == pytest.approx(
        9.391e-5, rel=1e-3
    )


def test_ieee_738_s_drake_is_rated_1025_a() -> None:  # 4.6.1
    rated = ampacity(DRAKE, surface=SURFACE, temperature=celsius(100), environment=ENVIRONMENT)
    assert rated.si == pytest.approx(1025, abs=1)


def test_ieee_738_s_drake_is_held_at_97_5_c_by_1000_a() -> None:  # 4.6.2
    held = temperature(DRAKE, surface=SURFACE, current=amperes(1000), environment=ENVIRONMENT)
    assert held.to(celsius) == pytest.approx(97.5, abs=0.05)


def test_ieee_738_s_drake_warms_0_28_c_in_10_s_at_1200_a() -> None:  # 4.6.3
    reached = temperature(
        HOTTER,
        surface=SURFACE,
        current=amperes(1200),
        environment=ENVIRONMENT,
        duration=timedelta(seconds=10),
        initial_temperature=celsius(100),
    )
    assert reached.to(celsius) == pytest.approx(100.28, abs=0.01)


def test_ieee_738_s_drake_settles_at_119_6_c_at_1200_a() -> None:  # 4.6.3
    reached = temperature(
        HOTTER,
        surface=SURFACE,
        current=amperes(1200),
        environment=ENVIRONMENT,
        duration=5 * HOUR,
        initial_temperature=celsius(100),
    )
    assert reached.to(celsius) == pytest.approx(119.6, abs=0.1)


def test_ieee_738_s_drake_reaches_125_c_in_15_min_at_1312_a() -> None:  # 4.6.4
    current = ampacity(
        HOTTER,
        surface=SURFACE,
        temperature=celsius(125),
        environment=ENVIRONMENT,
        duration=timedelta(minutes=15),
        initial_temperature=celsius(100),
    )
    assert current.si == pytest.approx(1312, abs=3)


def test_ieee_738_s_drake_loses_63_31_w_per_m_by_convection_at_night() -> None:  # 4.6.5
    assert IEEE738.convection(DRAKE, celsius(50), NIGHT).si == pytest.approx(63.31, rel=1e-3)


def test_ieee_738_s_drake_loses_12_01_w_per_m_by_radiation_at_night() -> None:  # 4.6.5
    radiated = IEEE738.radiation(DRAKE, celsius(50), NIGHT, surface=SURFACE)
    assert radiated.si == pytest.approx(12.01, rel=2e-3)


def test_ieee_738_s_drake_resists_7_986e_5_ohm_per_m_at_50_c() -> None:  # 4.6.5
    assert IEEE738.resistance(DRAKE, celsius(50), amperes(678)).si == pytest.approx(
        7.986e-5, rel=1e-3
    )


def test_ieee_738_s_drake_cools_1_77_c_in_a_minute_at_night() -> None:  # 4.6.5: one 60 s step
    interval = Interval(current=amperes(678), environment=NIGHT, duration=timedelta(minutes=1))
    after = temperature_profile(
        DRAKE, [interval], initial_temperature=celsius(50), surface=SURFACE
    ).temperatures[-1]
    assert after.to(celsius) == pytest.approx(48.23, abs=0.1)


def test_ieee_738_s_drake_s_core_is_105_4_c() -> None:  # annex C, k_th 1 W/(m·°C)
    core = core_temperature(
        DRAKE,
        conductivity=w_per_m_k(1),
        current=amperes(1025),
        surface_temperature=celsius(100),
    )
    assert core.to(celsius) == pytest.approx(105.4, abs=0.1)


def test_drake_s_wires_hold_ieee_738_s_1310_j_per_m_k() -> None:  # 4.6.3, by its wires
    assert heat_capacity(b232.DRAKE).si == pytest.approx(1310, rel=0.01)


def test_drake_s_wires_carry_ieee_738_s_1025_a_without_a_heat_capacity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:  # a steady rating takes none
    def unavailable(_: object) -> None:
        raise AssertionError("a steady rating took a heat capacity")

    monkeypatch.setattr(ratings, "heat_capacity", unavailable)
    rated = ampacity(
        b232.DRAKE, frequency=AC, surface=SURFACE, temperature=celsius(100), environment=ENVIRONMENT
    )
    assert rated.si == pytest.approx(1025, rel=0.01)


def test_the_sun_gives_no_heat_at_night() -> None:
    assert IEEE738.flux(replace(SUN, when=datetime(2026, 6, 10, 23)), m(0)) == w_per_m2(0)


def test_a_current_too_great_holds_no_steady_temperature() -> None:
    with pytest.raises(ValueError, match="above"):
        temperature(DRAKE, surface=SURFACE, current=amperes(10000), environment=ENVIRONMENT)


def test_a_transient_from_a_steady_state_climbs_toward_the_new_one() -> None:
    held = temperature(DRAKE, surface=SURFACE, current=amperes(1000), environment=ENVIRONMENT)
    reached = temperature(
        DRAKE,
        surface=SURFACE,
        current=amperes(1200),
        environment=ENVIRONMENT,
        duration=timedelta(minutes=15),
        initial_temperature=held,
    )
    forever = temperature(DRAKE, surface=SURFACE, current=amperes(1200), environment=ENVIRONMENT)
    assert held < reached < forever


def test_a_conductor_already_at_a_temperature_has_no_current_to_reach_it() -> None:
    with pytest.raises(ValueError, match="already"):
        ampacity(
            DRAKE,
            surface=SURFACE,
            temperature=celsius(90),
            environment=ENVIRONMENT,
            duration=timedelta(minutes=15),
            initial_temperature=celsius(100),
        )


@pytest.mark.parametrize(
    "surface",
    [replace(SURFACE, emissivity=0.9), replace(SURFACE, absorptivity=0.4)],
    ids=["more emissive", "less absorptive"],
)
def test_a_cooler_surface_carries_more_current(surface: Surface) -> None:
    base, cooler = (
        ampacity(DRAKE, surface=each, temperature=celsius(100), environment=ENVIRONMENT)
        for each in (SURFACE, surface)
    )
    assert base < cooler


def test_a_rating_s_current_holds_its_temperature() -> None:
    surface = Surface(emissivity=0.9, absorptivity=0.4)
    rated = ampacity(DRAKE, surface=surface, temperature=celsius(100), environment=ENVIRONMENT)
    held = temperature(DRAKE, surface=surface, current=rated, environment=ENVIRONMENT)
    assert held.to(celsius) == pytest.approx(100, abs=0.01)


@pytest.mark.parametrize("surface", [SURFACE, Surface(emissivity=0.6, absorptivity=0.3)])
def test_a_schedule_s_temperatures_are_its_intervals_in_turn(surface: Surface) -> None:
    duration, current = timedelta(minutes=2), amperes(1100)
    night = replace(ENVIRONMENT, air=celsius(25), sun=w_per_m2(0))
    intervals = [
        Interval(current=current, environment=weather, duration=duration)
        for weather in (ENVIRONMENT, night)
    ]
    profile = temperature_profile(
        DRAKE, intervals, surface=surface, initial_temperature=celsius(80)
    )
    expected = [celsius(80)]
    for interval in intervals:
        expected.append(
            temperature(
                DRAKE,
                surface=surface,
                current=current,
                environment=interval.environment,
                duration=duration,
                initial_temperature=expected[-1],
            )
        )
    assert [t.si for t in profile.temperatures] == pytest.approx(
        [t.si for t in expected], abs=1e-10
    )


SCHEDULE = (
    Interval(current=amperes(1200), environment=ENVIRONMENT, duration=timedelta(seconds=125)),
    Interval(current=amperes(600), environment=ENVIRONMENT, duration=timedelta(seconds=83)),
)


@pytest.mark.parametrize("every", [7, 60], ids=lambda s: f"{s} s")
def test_sampling_a_schedule_leaves_its_temperatures_at_each_interval_s_end(every: int) -> None:
    def profile(sample: timedelta | None) -> dict[timedelta, Temperature]:
        found = temperature_profile(
            DRAKE,
            SCHEDULE,
            surface=SURFACE,
            initial_temperature=celsius(75),
            sample_every=sample,
        )
        return dict(zip(found.elapsed, found.temperatures, strict=True))

    ends, sampled = profile(None), profile(timedelta(seconds=every))
    assert [sampled[at].si for at in ends] == pytest.approx(
        [t.si for t in ends.values()], abs=1e-10
    )


def test_a_schedule_starts_at_its_initial_temperature() -> None:
    profile = temperature_profile(DRAKE, SCHEDULE, surface=SURFACE, initial_temperature=celsius(75))
    assert (profile.elapsed[0], profile.temperatures[0]) == (timedelta(0), celsius(75))


def test_an_empty_schedule_is_its_initial_temperature_alone() -> None:
    profile = temperature_profile(DRAKE, (), surface=SURFACE, initial_temperature=celsius(75))
    assert (profile.elapsed, profile.temperatures) == ((timedelta(0),), (celsius(75),))


def test_a_schedule_is_sampled_at_a_positive_step() -> None:
    with pytest.raises(ValueError, match="positive"):
        temperature_profile(
            DRAKE,
            SCHEDULE,
            surface=SURFACE,
            initial_temperature=celsius(75),
            sample_every=timedelta(0),
        )


def test_an_interval_lasts() -> None:
    with pytest.raises(ValueError, match="positive duration"):
        Interval(current=amperes(1000), environment=ENVIRONMENT, duration=timedelta(0))


def test_stated_resistances_run_straight_between_and_beyond_their_temperatures() -> None:
    at = {t: DRAKE.resistance(celsius(t), amperes(0)).to(ohm_per_km) for t in (50, 100)}
    assert at == pytest.approx({50: (0.07283 + 0.08688) / 2, 100: 0.08688 + 0.5 * 0.01405})


def test_a_stated_resistance_takes_two_temperatures() -> None:
    with pytest.raises(ValueError, match="two temperatures"):
        Thermal.from_resistances(
            diameter=mm(28.14), frequency=AC, resistances={celsius(25): ohm_per_km(0.07283)}
        )


def test_a_supplied_resistance_is_asked_at_the_rating_s_current() -> None:
    asked: list[float] = []

    def resistance(at: Temperature, current: Current) -> ResistancePerLength:
        asked.append(current.si)
        return ohm_per_km(0.08 * (1 + current.si * 1e-5))

    supplied = Thermal(diameter=mm(28.14), resistance=resistance, frequency=AC)
    ampacity(supplied, surface=SURFACE, temperature=celsius(100), environment=ENVIRONMENT)
    assert max(asked) > 0


def test_supplied_thermal_data_takes_no_frequency() -> None:  # its resistances have their own
    with pytest.raises(TypeError, match="omit frequency"):
        ampacity(
            DRAKE,
            frequency=hz(50),
            surface=SURFACE,
            temperature=celsius(100),
            environment=ENVIRONMENT,
        )


def test_a_conductor_s_rating_takes_a_frequency() -> None:
    with pytest.raises(TypeError, match="requires frequency"):
        ampacity(b232.DRAKE, surface=SURFACE, temperature=celsius(100), environment=ENVIRONMENT)


@pytest.mark.parametrize(
    ("duration", "initial"), [(HOUR, None), (None, celsius(75))], ids=["duration", "initial"]
)
def test_a_transient_rating_takes_both_its_duration_and_its_initial_temperature(
    duration: timedelta | None, initial: Temperature | None
) -> None:
    with pytest.raises(TypeError, match="both duration and initial_temperature"):
        temperature(
            DRAKE,
            surface=SURFACE,
            current=amperes(1000),
            environment=ENVIRONMENT,
            duration=duration,
            initial_temperature=initial,
        )


def test_a_transient_rating_takes_a_heat_capacity() -> None:
    without = replace(DRAKE, heat_capacity=None)
    with pytest.raises(Missing, match="heat capacity"):
        temperature(
            without,
            surface=SURFACE,
            current=amperes(1000),
            environment=ENVIRONMENT,
            duration=HOUR,
            initial_temperature=celsius(75),
        )
