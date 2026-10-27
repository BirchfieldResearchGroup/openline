"""openline.types.materials: each metal's constants against the documents that give them, a
constant no document gives raising ``Missing``, and a wire standard's least strengths by
diameter, each table read in its own units and never past its ranges. Every metal the listed
conductors are made of gives what physics takes of it."""

import math

import pytest

from openline import conductors
from openline.electrical import temperature_coefficient
from openline.types import Missing
from openline.types.conductors import Conductor
from openline.types.materials import (
    Aluminum1350H19,
    Aluminum1350O,
    Aluminum5005H19,
    Aluminum6201T81,
    AluminumAL3,
    AluminumAlloy,
    CoatedSteel,
    CopperCladSteel,
    CopperCladSteel30HS,
    HardDrawnCopper,
    Iron,
    Metal,
    SteelGA2,
    SteelGA3,
    SteelGA5,
)
from openline.types.units import (
    Length,
    Stress,
    inch,
    ksi,
    lb_per_kft,
    lbf,
    mm,
    mpa,
    ohm_per_kft,
)

CONSTANTS = ("resistivity", "resistivity_rise", "density", "specific_heat", "modulus", "expansion")
NO_4 = math.pi / 4 * inch(0.2043).si ** 2  # m²: Copperweld ED1800's No. 4 solid wire


def test_a_material_prints_as_its_name() -> None:
    assert (repr(SteelGA2), str(CoatedSteel)) == ("SteelGA2", "CoatedSteel")


def test_a_constant_no_document_gives_is_missing() -> None:  # each alloy grade gives its own
    with pytest.raises(Missing, match="AluminumAlloy's resistivity"):
        _ = AluminumAlloy.resistivity


def test_a_constant_no_metal_has_is_no_attribute() -> None:
    with pytest.raises(AttributeError):
        _ = AluminumAlloy.resistance  # type: ignore[attr-defined]


def test_every_listed_conductor_s_metals_give_what_physics_takes() -> None:
    metals = {strand.material for c in conductors.of(Conductor) for strand in c.strands}

    def gives(metal: type[Metal], name: str) -> bool:
        try:
            getattr(metal, name)
        except Missing:
            return False
        return True

    missing = {(m.__name__, name) for m in metals for name in CONSTANTS if not gives(m, name)}
    assert missing == set()


@pytest.mark.parametrize(
    ("metal", "given"),
    [  # NBS Handbook 109, table 1; NBS Handbook 100, p. 14
        (Aluminum1350O, 0.00408),
        (Aluminum5005H19, 0.00353),
        (Aluminum6201T81, 0.00347),
        (HardDrawnCopper, 0.97 * 0.00393),
        (CopperCladSteel30HS, 0.00378),  # IEEE 80-2000, table 1; ED1800, p. 4
    ],
)
def test_a_temperature_coefficient_is_its_document_s(metal: type[Metal], given: float) -> None:
    assert temperature_coefficient(metal).si == pytest.approx(given, abs=0.000005)


def test_coated_steel_s_resistivity_rises_as_its_iron_s() -> None:  # CRC Handbook, p. 12-42
    assert CoatedSteel.resistivity_rise == Iron.resistivity_rise


def test_copper_clad_steel_weighs_ed1800_s_solid_wire() -> None:  # pp. 4 and 7: 115.8 lb/kft
    assert CopperCladSteel30HS.density.si * NO_4 == pytest.approx(lb_per_kft(115.8).si, rel=1e-3)


def test_copper_clad_steel_conducts_as_ed1800_s_solid_wire() -> None:  # 0.8283 Ω/kft at 20 °C
    resistance = CopperCladSteel30HS.resistivity.si / NO_4
    assert resistance == pytest.approx(ohm_per_kft(0.8283).si, rel=1e-3)


def test_copper_clad_steel_stretches_as_ed1800_s_solid_wire() -> None:  # E·A, 786 700 lbf
    assert CopperCladSteel30HS.modulus.si * NO_4 == pytest.approx(lbf(786_700).si, rel=1e-3)


def test_copper_clad_steel_expands_as_ed1800_s_solid_wire() -> None:  # 7.2e-6 per °F
    assert CopperCladSteel.expansion.si == pytest.approx(7.2e-6 * 1.8)


def test_copper_clad_steel_holds_ieee_80_s_heat_per_volume() -> None:  # table 1: 3.85 J/(cm³·K)
    held = CopperCladSteel.density.si * CopperCladSteel.specific_heat.si
    assert held == pytest.approx(3.85e6)


@pytest.mark.parametrize(
    ("metal", "diameter", "metric", "expected"),
    [
        # B398 table 2: 'over ... through', in two independent unit systems.
        (Aluminum6201T81, mm(1.5001), True, mpa(330)),
        (Aluminum6201T81, mm(3.25), True, mpa(330)),
        (Aluminum6201T81, mm(3.2501), True, mpa(315)),
        (Aluminum6201T81, mm(4.75), True, mpa(315)),
        (Aluminum6201T81, inch(0.0611), False, ksi(48)),
        (Aluminum6201T81, inch(0.1280), False, ksi(48)),
        (Aluminum6201T81, inch(0.1281), False, ksi(46)),
        (Aluminum6201T81, inch(0.1878), False, ksi(46)),
        # The designation chooses the table, not the unit a diameter was given in.
        (Aluminum6201T81, mm(4.77012), False, ksi(46)),
        (Aluminum6201T81, inch(3.25 / 25.4), True, mpa(330)),
        # EN 50183 has only an SI table; either designation reads it.
        (AluminumAL3, mm(1.5001), True, mpa(295)),
        (AluminumAL3, mm(5), True, mpa(295)),
        (AluminumAL3, inch(5 / 25.4), False, mpa(295)),
        # B230 includes both ends of each printed range.
        (Aluminum1350H19, mm(1.26), True, mpa(200)),
        (Aluminum1350H19, inch(0.0501), False, ksi(29)),
        # B609 table 3: independent minima, over the sizes in tables 1 and 2.
        (Aluminum1350O, inch(0.0100), False, ksi(8.5)),
        (Aluminum1350O, inch(0.7071), False, ksi(8.5)),
        (Aluminum1350O, mm(0.250), True, mpa(60)),
        (Aluminum1350O, mm(18.0), True, mpa(60)),
        # B606 and B957 keep their inclusive bands and independently rounded SI values.
        (SteelGA3, inch(0.0899), False, ksi(235)),
        (SteelGA3, inch(0.0900), False, ksi(230)),
        (SteelGA5, mm(2.28), True, mpa(1965)),
        (SteelGA5, mm(2.29), True, mpa(1900)),
    ],
)
def test_a_strength_table_reads_in_its_designation_s_units(
    metal: type[Metal], diameter: Length, metric: bool, expected: Stress
) -> None:
    assert metal.tensile_strength.at(diameter, metric).si == pytest.approx(expected.si)


@pytest.mark.parametrize(
    ("metal", "diameter", "metric"),
    [
        (Aluminum6201T81, mm(1.50), True),
        (Aluminum6201T81, inch(0.0610), False),
        (Aluminum6201T81, mm(5.0001), True),  # past B398's 4.75 mm, guessed to 5.00 mm
        (Aluminum6201T81, inch(0.1961), False),
        (Aluminum6201T81, inch(0.1970), True),  # 5.004 mm, past the SI table's guess
        (AluminumAL3, mm(1.50), True),
        (AluminumAL3, inch(1.5 / 25.4), False),
        (AluminumAL3, mm(5.0001), True),
        (AluminumAL3, mm(5.0001), False),
        (Aluminum1350H19, mm(1.255), True),  # between B230's printed ranges
        (Aluminum1350O, inch(0.0099), False),
        (Aluminum1350O, mm(18.01), True),
        (SteelGA3, inch(0.08995), False),
        (SteelGA5, mm(2.285), True),
        (SteelGA5, mm(4.83), True),
    ],
)
def test_a_strength_table_extends_no_range(
    metal: type[Metal], diameter: Length, metric: bool
) -> None:
    with pytest.raises(Missing, match="no range"):
        metal.tensile_strength.at(diameter, metric)
