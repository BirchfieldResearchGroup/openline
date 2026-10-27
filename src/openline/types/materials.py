"""Material properties, represented by classes; grades inherit from their base material.

Metal properties include resistivity at 20 °C, density, specific heat, relative permeability,
elastic modulus, thermal expansion, and, where a wire standard gives them, its wires' least
strengths by diameter. Citations accompany the classes that define values.
Homogeneous copper and aluminum grades share their base metal's resistivity slope under the
adopted Matthiessen approximation (NBS Handbook 100, p. 14), unless their standard specifies
a coefficient. Clad materials require their own documented slope or temperature coefficient."""

from inspect import get_annotations
from typing import TYPE_CHECKING, Any, ClassVar

from . import Missing, Record
from .units import (
    Density,
    Length,
    PerKelvin,
    Resistivity,
    ResistivityPerKelvin,
    SpecificHeat,
    Stress,
    inch,
    j_per_kg_k,
    kg_per_m3,
    ksi,
    mm,
    mpa,
    ohm_cmil_per_ft,
    ohm_mm2_per_m,
    ohm_mm2_per_m_k,
    per_kelvin,
    psi,
)

__all__ = [
    "Aluminum",
    "Aluminum1350H19",
    "Aluminum1350O",
    "Aluminum5005H19",
    "Aluminum6201T81",
    "AluminumA1",
    "AluminumA2",
    "AluminumA3",
    "AluminumAL3",
    "AluminumAlloy",
    "AluminumCladSteel",
    "AluminumCladSteelAW2",
    "AluminumCladSteelAW3",
    "AnnealedAluminum",
    "AnnealedCopper",
    "ByDiameter",
    "CarbonComposite",
    "Ceramic",
    "CoatedSteel",
    "Composite",
    "Concrete",
    "Copper",
    "CopperCladSteel",
    "CopperCladSteel30EHS",
    "CopperCladSteel30HS",
    "CopperCladSteel40HS",
    "Glass",
    "HardDrawnAluminum",
    "HardDrawnCopper",
    "Iron",
    "Material",
    "Metal",
    "MischmetalCoatedSteel",
    "Polymer",
    "Porcelain",
    "SiliconeRubber",
    "Steel",
    "SteelGA2",
    "SteelGA3",
    "SteelGA4",
    "SteelGA5",
    "SteelGC2",
    "SteelMA2",
    "SteelMA3",
    "SteelMA4",
    "SteelMA5",
    "SteelS1A",
    "SteelS1B",
    "SteelS2A",
    "SteelS2B",
    "SteelS3A",
    "Wood",
    "ZincCoatedSteel",
]


# Resistivity at 20 °C of 100% IACS annealed copper, NBS Handbook 100.
# Retain the precision already used for the copper properties in this module.
_IACS_RESISTIVITY_20 = ohm_mm2_per_m(0.017241)


class ByDiameter(Record, kw_only=False):
    """A wire standard's least stress by diameter: ``(least, most, stress)`` in each native
    unit system. The upper bound is included; the lower bound follows ``lower_inclusive``."""

    inch_pound: tuple[tuple[Length, Length, Stress], ...]
    """Its inch-pound table."""
    metric: tuple[tuple[Length, Length, Stress], ...]
    """Its metric table."""
    lower_inclusive: bool = True
    """Whether each range includes its lower bound; false for an 'over ... through' table."""

    def at(self, diameter: Length, metric: bool) -> Stress:
        """Use the conductor designation's unit system. A standard giving only one table uses
        that table for either system; no table is extended beyond its diameter ranges."""
        table = (self.metric or self.inch_pound) if metric else (self.inch_pound or self.metric)
        for least, most, stress in table:
            above = (
                diameter.si >= least.si * (1 - 1e-9)
                if self.lower_inclusive
                else diameter.si > least.si * (1 + 1e-9)
            )
            if above and diameter.si <= most.si * (1 + 1e-9):
                return stress
        raise Missing(f"no range of the table holds a wire of {diameter}")


class _Named(type):
    """A material prints as its name: ``SteelGA2``, not ``<class '...SteelGA2'>``; a constant its
    class declares and no document at hand gives raises ``Missing``."""

    def __repr__(cls) -> str:
        return cls.__name__

    if not TYPE_CHECKING:  # so that the type checker still refuses an undeclared constant

        def __getattr__(cls, name: str) -> Any:
            if not name.startswith("__") and any(name in get_annotations(c) for c in cls.__mro__):
                said = name.replace("_", " ")
                raise Missing(f"no document at hand gives {cls.__name__}'s {said}")
            raise AttributeError(f"type object {cls.__name__!r} has no attribute {name!r}")


class Material(metaclass=_Named):
    """What wires, members and insulators are made of."""

    name: ClassVar[str]
    """Its name as documents give it: ``Aluminum 1350-H19``."""


class Metal(Material):
    """Metal."""

    resistivity: ClassVar[Resistivity]
    """Resistivity at 20 °C."""
    resistivity_rise: ClassVar[ResistivityPerKelvin]
    """Absolute change in resistivity per kelvin.

    Homogeneous copper and aluminum grades share their base metal's slope under the adopted
    Matthiessen approximation unless their standard specifies a coefficient. Clad materials
    require their own documented slope or temperature coefficient."""
    density: ClassVar[Density]
    """Density at 20 °C."""
    specific_heat: ClassVar[SpecificHeat]
    """Heat capacity per mass."""
    relative_permeability: ClassVar[float]
    """Its magnetic permeability over the vacuum's."""
    modulus: ClassVar[Stress]
    """Its modulus of elasticity, a wire's, final."""
    expansion: ClassVar[PerKelvin]
    """Its coefficient of linear thermal expansion."""
    tensile_strength: ClassVar[ByDiameter]
    """Its wires' tensile strength for conductor rating, by diameter; each grade cites its basis
    (a lot average or an individual minimum)."""


class Aluminum(Metal):
    """Aluminum and its alloys: density, and the rise of resistivity, EC-H19's resistivity times
    its temperature coefficient, NBS Handbook 109, p. 13, table 1; specific heat, IEEE 738-2023,
    table 7; relative permeability, Wikipedia, Permeability (electromagnetism)."""

    name = "Aluminum"
    resistivity_rise = ohm_mm2_per_m_k(0.028264 * 0.00403)
    density = kg_per_m3(2703)
    specific_heat = j_per_kg_k(955)
    relative_permeability = 1.000022


class HardDrawnAluminum(Aluminum):
    """Aluminum, hard drawn, of 61.0% IACS: NBS Handbook 109, p. 13, table 1, EC-H19 (aluminum
    1350-H19); alfanar, Overhead Conductors, p. 8, hard drawn aluminum, also for its final
    modulus of elasticity and its expansion."""

    name = "Hard-drawn aluminum"
    resistivity = ohm_mm2_per_m(0.028264)
    modulus = mpa(68_000)
    expansion = per_kelvin(23.0e-6)


class Aluminum1350H19(HardDrawnAluminum):
    """Aluminum 1350-H19, hard drawn, of 61.2% IACS, the most resistive a lot may average: ASTM
    B230-07, table 3; density for calculation, 10.1; least average tensile strength of a lot,
    tables 1 and 2."""

    name = "Aluminum 1350-H19"
    resistivity = ohm_mm2_per_m(0.028172)
    density = kg_per_m3(2705)
    tensile_strength = ByDiameter(
        (
            (inch(0.0105), inch(0.0500), ksi(25.0)),
            (inch(0.0501), inch(0.0600), ksi(29.0)),
            (inch(0.0601), inch(0.0700), ksi(28.5)),
            (inch(0.0701), inch(0.0800), ksi(28.0)),
            (inch(0.0801), inch(0.0900), ksi(27.5)),
            (inch(0.0901), inch(0.1000), ksi(27.0)),
            (inch(0.1001), inch(0.1100), ksi(26.0)),
            (inch(0.1101), inch(0.1200), ksi(25.5)),
            (inch(0.1201), inch(0.1400), ksi(25.0)),
            (inch(0.1401), inch(0.1500), ksi(24.5)),
            (inch(0.1501), inch(0.1800), ksi(24.0)),
            (inch(0.1801), inch(0.2100), ksi(24.0)),
            (inch(0.2101), inch(0.2600), ksi(23.5)),
        ),
        (
            (mm(0.227), mm(1.25), mpa(170.0)),
            (mm(1.26), mm(1.50), mpa(200.0)),
            (mm(1.51), mm(1.75), mpa(195.0)),
            (mm(1.76), mm(2.00), mpa(195.0)),
            (mm(2.01), mm(2.25), mpa(190.0)),
            (mm(2.26), mm(2.50), mpa(185.0)),
            (mm(2.51), mm(2.75), mpa(180.0)),
            (mm(2.76), mm(3.00), mpa(175.0)),
            (mm(3.01), mm(3.50), mpa(170.0)),
            (mm(3.51), mm(3.75), mpa(170.0)),
            (mm(3.76), mm(4.50), mpa(165.0)),
            (mm(4.51), mm(5.25), mpa(165.0)),
            (mm(5.26), mm(6.50), mpa(160.0)),
        ),
    )


class AluminumA1(HardDrawnAluminum):
    """Aluminum A1, hard drawn, of 61.0% IACS: IEC 60889:1987, 2, the resistivity, density,
    expansion and temperature coefficient for calculation its base takes; table I, least tensile
    strength, its wires 1.25 mm to 5.00 mm (1)."""

    name = "Aluminum A1"
    tensile_strength = ByDiameter(
        (),
        (
            (mm(0), mm(1.25), mpa(200)),
            (mm(1.25), mm(1.50), mpa(195)),
            (mm(1.50), mm(1.75), mpa(190)),
            (mm(1.75), mm(2.00), mpa(185)),
            (mm(2.00), mm(2.25), mpa(180)),
            (mm(2.25), mm(2.50), mpa(175)),
            (mm(2.50), mm(3.00), mpa(170)),
            (mm(3.00), mm(3.50), mpa(165)),
            (mm(3.50), mm(5.00), mpa(160)),
        ),
        lower_inclusive=False,
    )


class AnnealedAluminum(Aluminum):
    """Aluminum, annealed."""

    name = "Annealed aluminum"


class Aluminum1350O(AnnealedAluminum):
    """Aluminum 1350-O, annealed: ASTM B856-03, 11.2, resistivity for calculation at 20 C.

    Density for calculation: ASTM B609/B609M-12 (2021), 10.1. Typical bulk modulus and
    expansion: Engineering Transmission Lines with ACCC Conductor, printed p. 74. The
    modulus is the metal's; conductor stiffness accounts for its wires' lay separately.
    Minimum tensile strength: B609/B609M-12 (2016), table 3, over the wire sizes in tables
    1 and 2. Inch-pound and SI requirements are independent (1.2)."""

    name = "Aluminum 1350-O"
    resistivity = ohm_mm2_per_m(0.0279)
    density = kg_per_m3(2705)
    modulus = mpa(69_000)
    expansion = per_kelvin(23.0e-6)
    tensile_strength = ByDiameter(
        ((inch(0.0100), inch(0.7071), ksi(8.5)),),
        ((mm(0.250), mm(18.0), mpa(60)),),
    )


class AluminumAlloy(Aluminum):
    """Aluminum alloy: final modulus of elasticity and expansion, alfanar, Overhead Conductors,
    p. 8, aluminum alloy types A and B alike."""

    name = "Aluminum alloy"
    modulus = mpa(68_000)
    expansion = per_kelvin(23.0e-6)


class Aluminum5005H19(AluminumAlloy):
    """Aluminum alloy 5005-H19, of 53.5% IACS: NBS Handbook 109, table 1; grade-specific density
    from footnote 1 (printed p. 5, PDF p. 13), refining the 2703 kg/m³ calculation convention."""

    name = "Aluminum 5005-H19"
    resistivity = ohm_mm2_per_m(0.032226)
    density = kg_per_m3(2697)


class Aluminum6201T81(AluminumAlloy):
    """Aluminum alloy 6201-T81: ASTM B398/B398M-15 (2021), 9.1, maximum resistivity; 10.1,
    density for calculation; table 2, least average tensile strength of a lot. Its inch-pound
    and SI requirements are independent, not conversions (1.2). Wires a little thicker than its
    largest, to 0.1960 in and 5.00 mm, take the largest's strength: an educated guess."""

    name = "Aluminum 6201-T81"
    resistivity = ohm_mm2_per_m(0.032841)
    density = kg_per_m3(2690)
    tensile_strength = ByDiameter(
        (
            (inch(0.0610), inch(0.1280), ksi(48)),
            (inch(0.1280), inch(0.1878), ksi(46)),
            (inch(0.1878), inch(0.1960), ksi(46)),  # educated guess
        ),
        (
            (mm(1.50), mm(3.25), mpa(330)),
            (mm(3.25), mm(4.75), mpa(315)),
            (mm(4.75), mm(5.00), mpa(315)),  # educated guess
        ),
        lower_inclusive=False,
    )


class AluminumA2(AluminumAlloy):
    """Aluminum alloy A2, IEC 60104:1987 type B, of 53.0% IACS: 2, its resistivity and
    temperature coefficient for calculation; table I, least tensile strength, its wires 1.50 mm
    to 4.50 mm (1)."""

    name = "Aluminum A2"
    resistivity = ohm_mm2_per_m(0.032530)
    resistivity_rise = ohm_mm2_per_m_k(0.032530 * 0.0036)
    tensile_strength = ByDiameter(
        (),
        ((mm(0), mm(3.5), mpa(295)), (mm(3.5), mm(4.50), mpa(295))),
        lower_inclusive=False,
    )


class AluminumA3(AluminumAlloy):
    """Aluminum alloy A3, IEC 60104:1987 type A, of 52.5% IACS: 2, its resistivity and
    temperature coefficient for calculation; table I, least tensile strength, its wires 1.50 mm
    to 4.50 mm (1)."""

    name = "Aluminum A3"
    resistivity = ohm_mm2_per_m(0.032840)
    resistivity_rise = ohm_mm2_per_m_k(0.032840 * 0.0036)
    tensile_strength = ByDiameter(
        (),
        ((mm(0), mm(3.5), mpa(325)), (mm(3.5), mm(4.50), mpa(315))),
        lower_inclusive=False,
    )


class AluminumAL3(AluminumAlloy):
    """Aluminum alloy AL3: EN 50183:2000, table 1, maximum resistivity and minimum wire tensile
    strength; clause 5, density and resistance temperature coefficient for calculation. Its
    modulus and expansion agree with those inherited from AluminumAlloy."""

    name = "Aluminum AL3"
    resistivity = ohm_mm2_per_m(0.032530)
    resistivity_rise = ohm_mm2_per_m_k(0.032530 * 0.0036)
    density = kg_per_m3(2700)
    tensile_strength = ByDiameter(
        (),
        ((mm(1.50), mm(5.00), mpa(295)),),
        lower_inclusive=False,
    )


class Copper(Metal):
    """Copper: the rise of resistivity, annealed copper's resistivity times its temperature
    coefficient, NBS Handbook 100, p. 9; density, p. 10; specific heat, IEEE 738-2023, table 7;
    relative permeability, Wikipedia, Permeability (electromagnetism)."""

    name = "Copper"
    resistivity_rise = ohm_mm2_per_m_k(_IACS_RESISTIVITY_20.to(ohm_mm2_per_m) * 0.00393)
    density = kg_per_m3(8890)
    specific_heat = j_per_kg_k(423)
    relative_permeability = 0.999994


class HardDrawnCopper(Copper):
    """Copper, hard drawn, of 97.0% IACS, its final modulus of elasticity and its expansion:
    alfanar, Overhead Conductors, p. 8."""

    name = "Hard-drawn copper"
    resistivity = ohm_mm2_per_m(0.017770)
    modulus = mpa(122_600)
    expansion = per_kelvin(17.0e-6)


class AnnealedCopper(Copper):
    """Copper, annealed, the International Annealed Copper Standard: NBS Handbook 100, p. 9;
    final modulus of elasticity and expansion, alfanar, Overhead Conductors, p. 8."""

    name = "Annealed copper"
    resistivity = _IACS_RESISTIVITY_20
    modulus = mpa(98_100)
    expansion = per_kelvin(17.0e-6)


class Iron(Metal):
    """Iron, pure: its resistivity at 293 K, and its rise between 273 K and 300 K, CRC Handbook of
    Chemistry and Physics, 97th ed., p. 12-42; relative permeability, iron 99.8% pure, Wikipedia,
    Permeability (electromagnetism)."""

    name = "Iron"
    resistivity = ohm_mm2_per_m(0.0961)
    resistivity_rise = ohm_mm2_per_m_k((0.0998 - 0.0857) / 27)
    relative_permeability = 5000


class Steel(Metal):
    """Steel: relative permeability, carbon steel's at 0.002 T, Wikipedia, Permeability
    (electromagnetism). It varies with the field; a clad steel's is its steel core's."""

    name = "Steel"
    relative_permeability = 100
    extension_stress: ClassVar[ByDiameter]
    """Its wires' least stress at 1% extension, by diameter, as its wire standard gives it."""


class CoatedSteel(Steel):
    """Steel, coated: density for calculation and the typical resistivity, not guaranteed, that
    calculations may take, ASTM B498-08, 13.1 and 13.2, galvanized steel's, which mischmetal-coated
    steel is taken to share; its rise of resistivity, its iron's; specific heat, IEEE 738-2023,
    table 7, galvanized or mischmetal steel; final modulus of elasticity and expansion, alfanar,
    Overhead Conductors, p. 8, galvanized steel's, shared alike."""

    name = "Coated steel"
    resistivity = ohm_mm2_per_m(0.19157)
    resistivity_rise = Iron.resistivity_rise
    density = kg_per_m3(7780)
    specific_heat = j_per_kg_k(476)
    modulus = mpa(207_000)
    expansion = per_kelvin(11.5e-6)


class ZincCoatedSteel(CoatedSteel):
    """Steel, zinc coated."""

    name = "Zinc-coated steel"


class SteelGA2(ZincCoatedSteel):
    """Steel GA2: class A zinc coating, regular strength; minimum ultimate tensile strength
    and stress at 1% extension, ASTM B498-08, tables 2 and 3, class A."""

    name = "Steel GA2"
    tensile_strength = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(210)),
            (inch(0.0900), inch(0.1199), ksi(205)),
            (inch(0.1200), inch(0.1399), ksi(205)),
            (inch(0.1400), inch(0.1900), ksi(200)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1450)),
            (mm(2.29), mm(3.04), mpa(1410)),
            (mm(3.05), mm(3.55), mpa(1410)),
            (mm(3.56), mm(4.82), mpa(1380)),
        ),
    )

    extension_stress = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(190)),
            (inch(0.0900), inch(0.1199), ksi(185)),
            (inch(0.1200), inch(0.1399), ksi(180)),
            (inch(0.1400), inch(0.1900), ksi(170)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1310)),
            (mm(2.29), mm(3.04), mpa(1280)),
            (mm(3.05), mm(3.55), mpa(1240)),
            (mm(3.56), mm(4.82), mpa(1170)),
        ),
    )


class SteelGA3(ZincCoatedSteel):
    """Steel GA3: class A zinc coating, high strength; minimum ultimate tensile strength and
    stress at 1% extension, ASTM B606/B606M-23, tables 2 and 3."""

    name = "Steel GA3"
    tensile_strength = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(235)),
            (inch(0.0900), inch(0.1199), ksi(230)),
            (inch(0.1200), inch(0.1399), ksi(225)),
            (inch(0.1400), inch(0.1900), ksi(220)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1620)),
            (mm(2.29), mm(3.04), mpa(1590)),
            (mm(3.05), mm(3.55), mpa(1550)),
            (mm(3.56), mm(4.82), mpa(1520)),
        ),
    )
    extension_stress = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(210)),
            (inch(0.0900), inch(0.1199), ksi(205)),
            (inch(0.1200), inch(0.1399), ksi(200)),
            (inch(0.1400), inch(0.1900), ksi(195)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1450)),
            (mm(2.29), mm(3.04), mpa(1410)),
            (mm(3.05), mm(3.55), mpa(1380)),
            (mm(3.56), mm(4.82), mpa(1340)),
        ),
    )


class SteelGA4(ZincCoatedSteel):
    """Steel GA4: class A zinc coating, extra-high strength; minimum ultimate tensile strength
    and stress at 1% extension, ASTM B957/B957M-23, tables 2 and 3."""

    name = "Steel GA4"
    tensile_strength = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(265)),
            (inch(0.0900), inch(0.1199), ksi(260)),
            (inch(0.1200), inch(0.1399), ksi(255)),
            (inch(0.1400), inch(0.1900), ksi(250)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1825)),
            (mm(2.29), mm(3.04), mpa(1790)),
            (mm(3.05), mm(3.55), mpa(1760)),
            (mm(3.56), mm(4.82), mpa(1725)),
        ),
    )
    extension_stress = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(225)),
            (inch(0.0900), inch(0.1199), ksi(220)),
            (inch(0.1200), inch(0.1399), ksi(215)),
            (inch(0.1400), inch(0.1900), ksi(210)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1550)),
            (mm(2.29), mm(3.04), mpa(1515)),
            (mm(3.05), mm(3.55), mpa(1480)),
            (mm(3.56), mm(4.82), mpa(1450)),
        ),
    )


class SteelGA5(ZincCoatedSteel):
    """Steel GA5: class A zinc coating, ultra-high strength; minimum ultimate tensile strength
    and stress at 1% extension, ASTM B957/B957M-23, tables 4 and 5."""

    name = "Steel GA5"
    tensile_strength = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(285)),
            (inch(0.0900), inch(0.1199), ksi(275)),
            (inch(0.1200), inch(0.1399), ksi(270)),
            (inch(0.1400), inch(0.1900), ksi(265)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1965)),
            (mm(2.29), mm(3.04), mpa(1900)),
            (mm(3.05), mm(3.55), mpa(1860)),
            (mm(3.56), mm(4.82), mpa(1825)),
        ),
    )
    extension_stress = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(230)),
            (inch(0.0900), inch(0.1199), ksi(225)),
            (inch(0.1200), inch(0.1399), ksi(220)),
            (inch(0.1400), inch(0.1900), ksi(215)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1580)),
            (mm(2.29), mm(3.04), mpa(1550)),
            (mm(3.05), mm(3.55), mpa(1515)),
            (mm(3.56), mm(4.82), mpa(1480)),
        ),
    )


class SteelGC2(ZincCoatedSteel):
    """Steel GC2: class C zinc coating, regular strength; minimum ultimate tensile strength
    and stress at 1% extension, ASTM B498-08, tables 2 and 3, class C."""

    name = "Steel GC2"
    tensile_strength = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(190)),
            (inch(0.0900), inch(0.1199), ksi(185)),
            (inch(0.1200), inch(0.1399), ksi(185)),
            (inch(0.1400), inch(0.1900), ksi(180)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1310)),
            (mm(2.29), mm(3.04), mpa(1280)),
            (mm(3.05), mm(3.55), mpa(1280)),
            (mm(3.56), mm(4.82), mpa(1240)),
        ),
    )

    extension_stress = ByDiameter(
        (
            (inch(0.0500), inch(0.0899), ksi(170)),
            (inch(0.0900), inch(0.1199), ksi(165)),
            (inch(0.1200), inch(0.1399), ksi(160)),
            (inch(0.1400), inch(0.1900), ksi(155)),
        ),
        (
            (mm(1.27), mm(2.28), mpa(1170)),
            (mm(2.29), mm(3.04), mpa(1140)),
            (mm(3.05), mm(3.55), mpa(1100)),
            (mm(3.56), mm(4.82), mpa(1070)),
        ),
    )


# IEC 60888:1987, tables III to V: the nominal diameters, in millimeters, each row is over and
# up to, its wires 1.25 mm to 5.50 mm (1).
_IEC60888 = (1.24, 2.25, 2.75, 3.00, 3.50, 4.25, 4.75, 5.50)


def _iec60888(*stresses: float) -> ByDiameter:
    """A column of IEC 60888's tables, in MPa, a stress for each range of diameter."""
    ranges = zip(_IEC60888[:-1], _IEC60888[1:], stresses, strict=True)
    return ByDiameter((), tuple((mm(a), mm(b), mpa(s)) for a, b, s in ranges), False)


class SteelS1A(ZincCoatedSteel):
    """Steel S1A: regular strength, zinc coating class 1; least stress at 1% extension and
    ultimate tensile stress, IEC 60888:1987, table III, class 1."""

    name = "Steel S1A"
    extension_stress = _iec60888(1170, 1140, 1140, 1100, 1100, 1100, 1100)
    tensile_strength = _iec60888(1340, 1310, 1310, 1290, 1290, 1290, 1290)


class SteelS1B(ZincCoatedSteel):
    """Steel S1B: regular strength, zinc coating class 2; IEC 60888:1987, table III, class 2."""

    name = "Steel S1B"
    extension_stress = _iec60888(1100, 1070, 1070, 1000, 1000, 1000, 1000)
    tensile_strength = _iec60888(1240, 1210, 1210, 1190, 1190, 1190, 1190)


class SteelS2A(ZincCoatedSteel):
    """Steel S2A: high strength, zinc coating class 1; IEC 60888:1987, table IV, class 1."""

    name = "Steel S2A"
    extension_stress = _iec60888(1310, 1280, 1280, 1240, 1170, 1170, 1170)
    tensile_strength = _iec60888(1450, 1410, 1410, 1410, 1380, 1380, 1380)


class SteelS2B(ZincCoatedSteel):
    """Steel S2B: high strength, zinc coating class 2; IEC 60888:1987, table IV, class 2."""

    name = "Steel S2B"
    extension_stress = _iec60888(1240, 1210, 1210, 1170, 1100, 1100, 1100)
    tensile_strength = _iec60888(1380, 1340, 1340, 1340, 1280, 1280, 1280)


class SteelS3A(ZincCoatedSteel):
    """Steel S3A: extra high strength, zinc coating class 1; IEC 60888:1987, table V."""

    name = "Steel S3A"
    extension_stress = _iec60888(1450, 1410, 1410, 1380, 1340, 1340, 1270)
    tensile_strength = _iec60888(1620, 1590, 1590, 1550, 1520, 1520, 1500)


class MischmetalCoatedSteel(CoatedSteel):
    """Steel, coated with zinc-5% aluminum mischmetal alloy."""

    name = "Mischmetal-coated steel"


class SteelMA2(MischmetalCoatedSteel):
    """Steel MA2: class A zinc-5% aluminum mischmetal coating, regular strength. ASTM
    B802/B802M-23, tables 4 and 5, class A, gives the same minimum ultimate tensile strength
    and stress at 1% extension as GA2."""

    name = "Steel MA2"
    tensile_strength = SteelGA2.tensile_strength
    extension_stress = SteelGA2.extension_stress


class SteelMA3(MischmetalCoatedSteel):
    """Steel MA3: class A zinc-5% aluminum mischmetal coating, high strength. ASTM
    B803/B803M-22, tables 2 and 3, gives the same minimum ultimate tensile strength and
    stress at 1% extension as GA3."""

    name = "Steel MA3"
    tensile_strength = SteelGA3.tensile_strength
    extension_stress = SteelGA3.extension_stress


class SteelMA4(MischmetalCoatedSteel):
    """Steel MA4: class A zinc-5% aluminum mischmetal coating, extra-high strength. ASTM
    B958/B958M-23, tables 2 and 3, gives the same minimum ultimate tensile strength and
    stress at 1% extension as GA4."""

    name = "Steel MA4"
    tensile_strength = SteelGA4.tensile_strength
    extension_stress = SteelGA4.extension_stress


class SteelMA5(MischmetalCoatedSteel):
    """Steel MA5: class A zinc-5% aluminum mischmetal coating, ultra-high strength. ASTM
    B958/B958M-23, tables 4 and 5, gives the same minimum ultimate tensile strength and
    stress at 1% extension as GA5."""

    name = "Steel MA5"
    tensile_strength = SteelGA5.tensile_strength
    extension_stress = SteelGA5.extension_stress


class AluminumCladSteel(Steel):
    """Aluminum-clad steel, of 20.3% conductivity: ASTM B415-16, 6.1, its resistivity; table 2,
    its density, its temperature coefficient, of which its own rise of resistivity, for aluminum
    over steel rises as neither does alone, its modulus of elasticity and its expansion; table 1,
    20% column, its least tensile strength, a wire taking the next larger listed diameter's
    (5.2), wires to 0.0700 in its smallest's, an educated guess;
    specific heat, IEEE 738-2023, table 7."""

    name = "Aluminum-clad steel"
    resistivity = ohm_cmil_per_ft(51.01)
    resistivity_rise = ohm_mm2_per_m_k(resistivity.to(ohm_mm2_per_m) * 0.0036)
    density = kg_per_m3(6590)
    specific_heat = j_per_kg_k(534)
    modulus = psi(23.5e6)
    expansion = per_kelvin(0.0000130)
    tensile_strength = ByDiameter(
        (
            (inch(0.0700), inch(0.0808), ksi(195)),  # educated guess
            (inch(0.0808), inch(0.1285), ksi(195)),
            (inch(0.1285), inch(0.1369), ksi(190)),
            (inch(0.1369), inch(0.1443), ksi(185)),
            (inch(0.1443), inch(0.1549), ksi(180)),
            (inch(0.1549), inch(0.1620), ksi(175)),
            (inch(0.1620), inch(0.1729), ksi(170)),
            (inch(0.1729), inch(0.1819), ksi(165)),
            (inch(0.1819), inch(0.1880), ksi(160)),
            (inch(0.1880), inch(0.2043), ksi(155)),
        ),
        (),
    )


class AluminumCladSteelAW2(AluminumCladSteel):
    """Aluminum-clad steel AW2, of normal strength, for cores: least stress at 1% extension and
    ultimate tensile strength, ASTM B502/B502M-23, table 1, in inch-pound units with SI
    alike; wires to 0.0570 in (1.448 mm), its smallest's, an educated guess."""

    name = "Aluminum-clad steel AW2"
    extension_stress = ByDiameter(
        (
            (inch(0.0570), inch(0.0769), psi(175_000)),  # educated guess
            (inch(0.0770), inch(0.1289), psi(175_000)),
            (inch(0.1290), inch(0.1369), psi(170_000)),
            (inch(0.1370), inch(0.1443), psi(165_000)),
            (inch(0.1444), inch(0.1549), psi(160_000)),
            (inch(0.1550), inch(0.1620), psi(160_000)),
            (inch(0.1621), inch(0.1729), psi(155_000)),
            (inch(0.1730), inch(0.1819), psi(150_000)),
            (inch(0.1820), inch(0.1880), psi(145_000)),
        ),
        (
            (mm(1.448), mm(1.955), mpa(1206)),  # educated guess
            (mm(1.956), mm(3.274), mpa(1206)),
            (mm(3.275), mm(3.477), mpa(1172)),
            (mm(3.478), mm(3.665), mpa(1137)),
            (mm(3.666), mm(3.934), mpa(1103)),
            (mm(3.935), mm(4.115), mpa(1103)),
            (mm(4.116), mm(4.392), mpa(1068)),
            (mm(4.393), mm(4.620), mpa(1034)),
            (mm(4.621), mm(4.775), mpa(1000)),
        ),
    )
    tensile_strength = ByDiameter(
        (
            (inch(0.0570), inch(0.0769), psi(195_000)),  # educated guess
            (inch(0.0770), inch(0.1289), psi(195_000)),
            (inch(0.1290), inch(0.1369), psi(190_000)),
            (inch(0.1370), inch(0.1443), psi(185_000)),
            (inch(0.1444), inch(0.1549), psi(180_000)),
            (inch(0.1550), inch(0.1620), psi(175_000)),
            (inch(0.1621), inch(0.1729), psi(170_000)),
            (inch(0.1730), inch(0.1819), psi(165_000)),
            (inch(0.1820), inch(0.1880), psi(160_000)),
        ),
        (
            (mm(1.448), mm(1.955), mpa(1344)),  # educated guess
            (mm(1.956), mm(3.274), mpa(1344)),
            (mm(3.275), mm(3.477), mpa(1310)),
            (mm(3.478), mm(3.665), mpa(1275)),
            (mm(3.666), mm(3.934), mpa(1241)),
            (mm(3.935), mm(4.115), mpa(1206)),
            (mm(4.116), mm(4.392), mpa(1172)),
            (mm(4.393), mm(4.620), mpa(1137)),
            (mm(4.621), mm(4.775), mpa(1103)),
        ),
    )


class AluminumCladSteelAW3(AluminumCladSteel):
    """Aluminum-clad steel AW3, of high strength, for cores: ASTM B502/B502M-23, table 2; wires
    to 0.0570 in (1.448 mm), its smallest's, an educated guess."""

    name = "Aluminum-clad steel AW3"
    extension_stress = ByDiameter(
        (
            (inch(0.0570), inch(0.0769), psi(190_000)),  # educated guess
            (inch(0.0770), inch(0.0899), psi(190_000)),
            (inch(0.0900), inch(0.1199), psi(185_000)),
            (inch(0.1200), inch(0.1399), psi(180_000)),
            (inch(0.1400), inch(0.1880), psi(170_000)),
        ),
        (
            (mm(1.448), mm(1.955), mpa(1310)),  # educated guess
            (mm(1.956), mm(2.283), mpa(1310)),
            (mm(2.284), mm(3.045), mpa(1280)),
            (mm(3.046), mm(3.553), mpa(1240)),
            (mm(3.554), mm(4.775), mpa(1170)),
        ),
    )
    tensile_strength = ByDiameter(
        (
            (inch(0.0570), inch(0.0769), psi(210_000)),  # educated guess
            (inch(0.0770), inch(0.0899), psi(210_000)),
            (inch(0.0900), inch(0.1199), psi(205_000)),
            (inch(0.1200), inch(0.1399), psi(200_000)),
            (inch(0.1400), inch(0.1880), psi(195_000)),
        ),
        (
            (mm(1.448), mm(1.955), mpa(1450)),  # educated guess
            (mm(1.956), mm(2.283), mpa(1450)),
            (mm(2.284), mm(3.045), mpa(1410)),
            (mm(3.046), mm(3.553), mpa(1380)),
            (mm(3.554), mm(4.775), mpa(1340)),
        ),
    )


class CopperCladSteel(Steel):
    """Copper-clad steel, of each grade ASTM B227-70 gives.

    Density for calculation: ASTM B227-70, 7.1, and B228-11a (2021), table 2, alike for every
    grade. Wire modulus and expansion: Copperweld ED1800, pp. 4 and 7; its resistance
    coefficient, 2.1e-3 per °F for 30% and 40% conductivity alike: p. 7 and IEEE 80-2000,
    table 1. Specific heat is an engineering estimate from that table's volumetric thermal
    capacity and this density, not a measured temperature-dependent heat-capacity curve.

    A grade's nominal resistivity at 20 °C is its conductivity's share of the NBS Handbook 100
    annealed-copper reference."""

    name = "Copper-clad steel"
    density = kg_per_m3(8150)
    # IEEE 80's 3.85 MJ/(m³ K) is a short-circuit thermal-capacity approximation.
    specific_heat = j_per_kg_k(3.85e6 / density.si)
    modulus = psi(24e6)  # solid wire; ED1800's 23 Mpsi is for the finished strand
    expansion = per_kelvin(7.2e-6 * 1.8)  # per °F to per K


def _listed(diameter: float, stress: Stress) -> tuple[Length, Length, Stress]:
    """A diameter a table lists to the nearest 0.0001 in, as the range it rounds from."""
    return inch(diameter - 0.00005), inch(diameter + 0.00005), stress


_IACS_30 = ohm_mm2_per_m(_IACS_RESISTIVITY_20.to(ohm_mm2_per_m) / 0.30)
_IACS_40 = ohm_mm2_per_m(_IACS_RESISTIVITY_20.to(ohm_mm2_per_m) / 0.40)


class CopperCladSteel30HS(CopperCladSteel):
    """Copper-clad steel, 30% conductivity, high strength.

    Least tensile strength: ASTM B227-70, table 1, Grade 30 HS, at the diameters it lists, each
    to the nearest 0.0001 in (note 3); it lists none for 0.0808 and 0.0800 in. At 0.0808 in, an
    educated guess: ASTM B228-11a (2021), table 1, rates the 3 No.
    12 strand 1719 lb, which its rating gives a wire of 122 100 psi."""

    name = "Copper-clad steel 30HS"
    resistivity = _IACS_30
    resistivity_rise = ohm_mm2_per_m_k(resistivity.to(ohm_mm2_per_m) * 0.00378)
    tensile_strength = ByDiameter(
        (
            _listed(0.0808, psi(122_100)),  # educated guess
            _listed(0.1019, psi(151_000)),
            _listed(0.1040, psi(151_000)),
            _listed(0.1144, psi(145_000)),
            _listed(0.1280, psi(140_000)),
            _listed(0.1285, psi(140_000)),
            _listed(0.1443, psi(135_000)),
            _listed(0.1620, psi(130_000)),
            _listed(0.1650, psi(130_000)),
            _listed(0.1819, psi(125_000)),
            _listed(0.2043, psi(120_000)),
        ),
        (),
    )


class CopperCladSteel30EHS(CopperCladSteel):
    """Copper-clad steel, 30% conductivity, extra high strength.

    Least tensile strength: ASTM B227-70, table 1, Grade 30 EHS, at the diameters it lists, each
    to the nearest 0.0001 in (note 3); it lists none for 0.0808 in. At 0.0808 in, an educated
    guess: ASTM B228-11a (2021), table 1, rates the 3 No. 12 strand
    2564 lb, which its rating gives a wire of 182 200 psi."""

    name = "Copper-clad steel 30EHS"
    resistivity = _IACS_30
    resistivity_rise = ohm_mm2_per_m_k(resistivity.to(ohm_mm2_per_m) * 0.00378)
    tensile_strength = ByDiameter(
        (
            _listed(0.0800, psi(179_000)),
            _listed(0.0808, psi(182_200)),  # educated guess
            _listed(0.1019, psi(179_000)),
            _listed(0.1040, psi(175_000)),
            _listed(0.1144, psi(174_100)),
            _listed(0.1280, psi(170_000)),
            _listed(0.1285, psi(170_000)),
            _listed(0.1443, psi(164_000)),
            _listed(0.1620, psi(157_500)),
            _listed(0.1650, psi(157_500)),
            _listed(0.1819, psi(150_500)),
            _listed(0.2043, psi(142_500)),
        ),
        (),
    )


class CopperCladSteel40HS(CopperCladSteel):
    """Copper-clad steel, 40% conductivity, high strength.

    Least tensile strength: ASTM B227-70, table 1, Grade 40 HS, at the diameters it lists, each
    to the nearest 0.0001 in (note 3), but 0.0808 and 0.0800 in: its 153 100 and 153 200 psi
    there, ASTM B228-04 and B228-11a (2021), table 1, contradict, whose 3 No. 12 strand, 1715
    and 1647 lb, rates such a wire near 120 000 psi. At 0.0808 in, an educated guess: B228-11a's
    1647 lb, which its rating gives a wire of 117 000 psi."""

    name = "Copper-clad steel 40HS"
    resistivity = _IACS_40
    resistivity_rise = ohm_mm2_per_m_k(resistivity.to(ohm_mm2_per_m) * 0.00378)
    tensile_strength = ByDiameter(
        (
            _listed(0.0808, psi(117_000)),  # educated guess
            _listed(0.1019, psi(138_600)),
            _listed(0.1040, psi(138_600)),
            _listed(0.1144, psi(133_000)),
            _listed(0.1280, psi(128_000)),
            _listed(0.1285, psi(128_000)),
            _listed(0.1443, psi(123_000)),
            _listed(0.1620, psi(118_000)),
            _listed(0.1650, psi(118_000)),
            _listed(0.1819, psi(113_000)),
            _listed(0.2043, psi(108_000)),
        ),
        (),
    )


class Composite(Material):
    """Composite."""

    name = "Composite"


class CarbonComposite(Composite):
    """Carbon fiber composite."""

    name = "Carbon fiber composite"


class Concrete(Material):
    """Concrete."""

    name = "Concrete"


class Ceramic(Material):
    """Ceramic."""

    name = "Ceramic"


class Porcelain(Ceramic):
    """Porcelain."""

    name = "Porcelain"


class Glass(Material):
    """Glass."""

    name = "Glass"


class Polymer(Material):
    """Polymer."""

    name = "Polymer"


class SiliconeRubber(Polymer):
    """Silicone rubber."""

    name = "Silicone rubber"


class Wood(Material):
    """Wood."""

    name = "Wood"
