"""Typed physical quantities stored in SI, with unit conversion functions.

``inch(1.026)`` stores 0.0260604 meters and displays as 26.06 mm.
``awg("4/0")`` returns the diameter of a 4/0 AWG wire."""

import math
from collections.abc import Callable
from typing import Any, ClassVar, Self, overload

from . import Record

__all__ = [
    "EPSILON_0",
    "GRAVITY",
    "MU_0",
    "SYMBOLS",
    "Admittance",
    "Ampere",
    "Angle",
    "Area",
    "Attenuation",
    "CharacteristicAdmittance",
    "Conductance",
    "ConductancePerLength",
    "Current",
    "Density",
    "Duration",
    "Elastance",
    "Force",
    "ForcePerLength",
    "Frequency",
    "HeatCapacityPerLength",
    "HeatFlux",
    "Hertz",
    "Impedance",
    "JoulePerKilogramKelvin",
    "JoulePerMeterKelvin",
    "Kelvin",
    "KilogramPerCubicMeter",
    "KilogramPerMeter",
    "Length",
    "MassPerLength",
    "Meter",
    "MeterPerFarad",
    "MeterPerSecond",
    "Newton",
    "NewtonPerMeter",
    "OhmMeter",
    "OhmMeterPerKelvin",
    "OhmPerMeter",
    "Pascal",
    "PerKelvin",
    "PhaseConstant",
    "PotentialCoefficient",
    "PowerPerLength",
    "PropagationConstant",
    "Quantity",
    "Radian",
    "ReactancePerLength",
    "ReciprocalKelvin",
    "ReciprocalMeter",
    "ResistancePerLength",
    "Resistivity",
    "ResistivityPerKelvin",
    "Second",
    "Siemens",
    "SiemensPerMeter",
    "SpecificHeat",
    "Speed",
    "SquareMeter",
    "Stress",
    "Susceptance",
    "SusceptancePerLength",
    "Temperature",
    "ThermalConductivity",
    "Unit",
    "Volt",
    "Voltage",
    "WattPerMeter",
    "WattPerMeterKelvin",
    "WattPerSquareMeter",
    "amperes",
    "aught",
    "awg",
    "celsius",
    "cm",
    "cmil",
    "dan",
    "degrees",
    "equivalent",
    "ft",
    "ft_in",
    "ft_per_s",
    "gauge_number",
    "gpa",
    "hz",
    "in2",
    "inch",
    "j_per_kg_k",
    "j_per_m_k",
    "kcmil",
    "kg_per_km",
    "kg_per_m",
    "kg_per_m3",
    "klbf",
    "km",
    "km_per_uf",
    "kn",
    "ksi",
    "kv",
    "lb_per_kft",
    "lbf",
    "m",
    "m2",
    "m_per_f",
    "m_per_s",
    "mi",
    "microseconds",
    "mm",
    "mm2",
    "mpa",
    "n",
    "n_per_m",
    "ohm_cmil_per_ft",
    "ohm_m",
    "ohm_mm2_per_m",
    "ohm_mm2_per_m_k",
    "ohm_per_kft",
    "ohm_per_km",
    "ohm_per_m",
    "ohm_per_mi",
    "per_kelvin",
    "per_km",
    "per_m",
    "psi",
    "s_per_m",
    "seconds",
    "siemens",
    "symbol",
    "us_per_km",
    "w_per_ft2",
    "w_per_m",
    "w_per_m2",
    "w_per_m_k",
]

_INCH, _FOOT, _MILE, _POUND = 0.0254, 0.3048, 1609.344, 0.45359237  # exact
GRAVITY = 9.80665  # m/s2: standard gravity, exact
MU_0 = 1.25663706127e-6  # N/A2: the vacuum's magnetic permeability, CODATA 2022 (NIST)
_LIGHT = 299_792_458.0  # m/s: the speed of light in vacuum, exact
EPSILON_0 = 1 / (MU_0 * _LIGHT**2)  # F/m: the vacuum's electric permittivity
_CIRCULAR_MIL = math.pi / 4 * (_INCH / 1000) ** 2


class Unit:
    """An SI unit shared by compatible quantity types, and its symbol.

    Types can share conversions while remaining distinct: resistance and reactance cannot be
    added directly."""

    symbol: ClassVar[str]
    """Its symbol: ``Ω/m``."""


class Meter(Unit):
    """The meter."""

    symbol = "m"


class SquareMeter(Unit):
    """The square meter."""

    symbol = "m²"


class KilogramPerMeter(Unit):
    """The kilogram per meter."""

    symbol = "kg/m"


class NewtonPerMeter(Unit):
    """The newton per meter."""

    symbol = "N/m"


class Newton(Unit):
    """The newton."""

    symbol = "N"


class OhmPerMeter(Unit):
    """The ohm per meter."""

    symbol = "Ω/m"


class OhmMeter(Unit):
    """The ohm meter."""

    symbol = "Ω·m"


class OhmMeterPerKelvin(Unit):
    """The ohm meter per kelvin."""

    symbol = "Ω·m/K"


class ReciprocalKelvin(Unit):
    """The reciprocal kelvin."""

    symbol = "1/K"


class Pascal(Unit):
    """The pascal."""

    symbol = "Pa"


class SiemensPerMeter(Unit):
    """The siemens per meter."""

    symbol = "S/m"


class Siemens(Unit):
    """The siemens."""

    symbol = "S"


class ReciprocalMeter(Unit):
    """The reciprocal meter."""

    symbol = "1/m"


class Second(Unit):
    """The second."""

    symbol = "s"


class MeterPerFarad(Unit):
    """The meter per farad."""

    symbol = "m/F"


class Kelvin(Unit):
    """The kelvin."""

    symbol = "K"


class Hertz(Unit):
    """The hertz."""

    symbol = "Hz"


class Ampere(Unit):
    """The ampere."""

    symbol = "A"


class Volt(Unit):
    """The volt."""

    symbol = "V"


class MeterPerSecond(Unit):
    """The meter per second."""

    symbol = "m/s"


class Radian(Unit):
    """The radian."""

    symbol = "rad"


class WattPerSquareMeter(Unit):
    """The watt per square meter."""

    symbol = "W/m²"


class WattPerMeter(Unit):
    """The watt per meter."""

    symbol = "W/m"


class KilogramPerCubicMeter(Unit):
    """The kilogram per cubic meter."""

    symbol = "kg/m³"


class JoulePerKilogramKelvin(Unit):
    """The joule per kilogram kelvin."""

    symbol = "J/(kg·K)"


class JoulePerMeterKelvin(Unit):
    """The joule per meter kelvin."""

    symbol = "J/(m·K)"


class WattPerMeterKelvin(Unit):
    """The watt per meter kelvin."""

    symbol = "W/(m·K)"


class Quantity[U: Unit](Record, kw_only=False):
    """A quantity in SI, of one kind, measured in the SI unit ``U``: it adds to and compares with
    its own kind, scales by a number, and divided by its own kind gives a number. It prints in a
    unit that fits it, ``28.14 mm``, takes a format for that number, ``f"{d:.1f}"`` is
    ``28.1 mm``, and reads in any unit of ``U``: ``d.to(inch)``, and a reactance in
    ``ohm_per_kft`` as a resistance does."""

    si: float
    """The value in SI."""

    def to(self, unit: Callable[[float], "Quantity[U]"]) -> float:
        """The quantity in a unit: ``DRAKE.diameter.to(inch)`` is 1.108."""
        return self._in(unit)

    @classmethod
    def of(cls, other: "Quantity[U]") -> Self:
        """A value of another kind in the same SI unit, taken as this kind:
        ``ReactancePerLength.of(ohm_per_kft(0.0756))``."""
        return cls(other.si)

    def _in(self, unit: Callable[[float], "Quantity[Any]"]) -> float:  # quoted: Python 3.12
        """The quantity's number in a unit, one that may start from other than zero, as
        ``celsius`` does."""
        zero = unit(0).si
        return (self.si - zero) / (unit(1).si - zero)

    def _of(self, other: Self) -> float:
        """Another quantity's value, if it is of this kind."""
        if type(other) is not type(self):
            raise TypeError(f"{type(other).__name__} is not {type(self).__name__}")
        return other.si

    def _shown(self) -> Callable[[float], "Quantity[Any]"]:  # quoted: Python 3.12
        """The unit it prints in."""
        raise NotImplementedError

    def __add__(self, other: Self) -> Self:
        return type(self)(self.si + self._of(other))

    def __sub__(self, other: Self) -> Self:
        return type(self)(self.si - self._of(other))

    def __mul__(self, factor: float) -> Self:
        if isinstance(factor, Quantity):
            raise TypeError(f"{type(self).__name__} scales only by a number")
        return type(self)(self.si * factor)

    __rmul__ = __mul__

    @overload
    def __truediv__(self, other: Self) -> float: ...
    @overload
    def __truediv__(self, other: float) -> Self: ...
    def __truediv__(self, other: Self | float) -> Self | float:
        if isinstance(other, Quantity):
            return self.si / self._of(other)
        return type(self)(self.si / other)

    def __neg__(self) -> Self:
        return type(self)(-self.si)

    def __abs__(self) -> Self:
        return type(self)(abs(self.si))

    def __lt__(self, other: Self) -> bool:
        return self.si < self._of(other)

    def __le__(self, other: Self) -> bool:
        return self.si <= self._of(other)

    def __gt__(self, other: Self) -> bool:
        return self.si > self._of(other)

    def __ge__(self, other: Self) -> bool:
        return self.si >= self._of(other)

    def __format__(self, spec: str) -> str:
        """Its number, then its unit's symbol: after a space, but a degree of angle's, which SI
        writes against the number, ``90°``."""
        unit = self._shown()
        text = symbol(unit)
        return f"{format(self._in(unit), spec or '.4g')}{'' if text == '°' else ' '}{text}"

    def __str__(self) -> str:
        return format(self, "")

    def __repr__(self) -> str:
        unit = self._shown()
        return f"{unit.__name__}({self._in(unit):.6g})"


class Length(Quantity[Meter]):
    """A length: 28.14 mm, or from a meter on, 300 m."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return mm if 0 < abs(self.si) < 1 else m


def m(value: float) -> Length:
    """Meters."""
    return Length(value)


def km(value: float) -> Length:
    """Kilometers."""
    return Length(value * 1000)


def mi(value: float) -> Length:
    """Miles."""
    return Length(value * _MILE)


def cm(value: float) -> Length:
    """Centimeters."""
    return Length(value * 1e-2)


def mm(value: float) -> Length:
    """Millimeters."""
    return Length(value * 1e-3)


def inch(value: float) -> Length:
    """Inches."""
    return Length(value * _INCH)


def ft(value: float) -> Length:
    """Feet."""
    return Length(value * _FOOT)


def ft_in(feet: float, inches: float) -> Length:
    """A length given in feet and inches, 12'-6": ``ft_in(12, 6)``."""
    return Length(feet * _FOOT + inches * _INCH)


def awg(gauge: str) -> Length:
    """The diameter an AWG gauge defines (ASTM B258): ``awg("4")``, ``awg("4/0")``."""
    diameter = 0.127e-3 * math.pow(92, (36 - gauge_number(gauge)) / 39)
    return Length(diameter)


def gauge_number(text: str) -> int:
    """An AWG gauge as a number: 6, or 4/0, which is -3."""
    zeros = text.removesuffix("/0")
    return int(text) if zeros == text else 1 - int(zeros)


def aught(gauge: int) -> str:
    """An AWG gauge as written: -3 is 4/0."""
    return f"{1 - gauge}/0" if gauge < 1 else str(gauge)


class Area(Quantity[SquareMeter]):
    """An area: 468.6 mm²."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return mm2


def m2(value: float) -> Area:
    """Square meters."""
    return Area(value)


def mm2(value: float) -> Area:
    """Square millimeters."""
    return Area(value * 1e-6)


def in2(value: float) -> Area:
    """Square inches."""
    return Area(value * _INCH**2)


def cmil(value: float) -> Area:
    """Circular mils."""
    return Area(value * _CIRCULAR_MIL)


def kcmil(value: float) -> Area:
    """Thousands of circular mils."""
    return Area(value * 1000 * _CIRCULAR_MIL)


def equivalent(area: Area, count: int) -> Length:
    """The diameter of a round wire of one of ``count`` wires' share of ``area``: a formed wire's
    equivalent diameter (IEC 62219, 3.5)."""
    return Length(math.sqrt(4 * area.si / (math.pi * count)))


class MassPerLength(Quantity[KilogramPerMeter]):
    """A mass per length: 1.627 kg/m."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return kg_per_m


def kg_per_m(value: float) -> MassPerLength:
    """Kilograms per meter."""
    return MassPerLength(value)


def kg_per_km(value: float) -> MassPerLength:
    """Kilograms per kilometer."""
    return MassPerLength(value * 1e-3)


def lb_per_kft(value: float) -> MassPerLength:
    """Pounds per thousand feet."""
    return MassPerLength(value * _POUND / (1000 * _FOOT))


class ForcePerLength(Quantity[NewtonPerMeter]):
    """A force per length, such as a weight: 15.95 N/m."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return n_per_m


def n_per_m(value: float) -> ForcePerLength:
    """Newtons per meter."""
    return ForcePerLength(value)


class Force(Quantity[Newton]):
    """A force: 140.1 kN."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return kn


def n(value: float) -> Force:
    """Newtons."""
    return Force(value)


def dan(value: float) -> Force:
    """Decanewtons."""
    return Force(value * 10)


def kn(value: float) -> Force:
    """Kilonewtons."""
    return Force(value * 1e3)


def lbf(value: float) -> Force:
    """Pounds-force, under standard gravity."""
    return Force(value * _POUND * GRAVITY)


def klbf(value: float) -> Force:
    """Thousands of pounds-force, under standard gravity."""
    return Force(value * 1000 * _POUND * GRAVITY)


class Stress(Quantity[Pascal]):
    """A stress, or a modulus of elasticity: 68 GPa."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return gpa


def mpa(value: float) -> Stress:
    """Megapascals, newtons per square millimeter."""
    return Stress(value * 1e6)


def gpa(value: float) -> Stress:
    """Gigapascals."""
    return Stress(value * 1e9)


def psi(value: float) -> Stress:
    """Pounds-force per square inch, under standard gravity."""
    return Stress(value * _POUND * GRAVITY / _INCH**2)


def ksi(value: float) -> Stress:
    """Thousands of pounds-force per square inch."""
    return psi(1000 * value)


class ResistancePerLength(Quantity[OhmPerMeter]):
    """A resistance per length: 0.07015 Ω/km."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return ohm_per_km


def ohm_per_m(value: float) -> ResistancePerLength:
    """Ohms per meter."""
    return ResistancePerLength(value)


def ohm_per_km(value: float) -> ResistancePerLength:
    """Ohms per kilometer."""
    return ResistancePerLength(value * 1e-3)


def ohm_per_kft(value: float) -> ResistancePerLength:
    """Ohms per thousand feet."""
    return ResistancePerLength(value / (1000 * _FOOT))


def ohm_per_mi(value: float) -> ResistancePerLength:
    """Ohms per mile."""
    return ResistancePerLength(value / _MILE)


class ReactancePerLength(Quantity[OhmPerMeter]):
    """A reactance per length: 0.2483 Ω/km. It reads in the units of a resistance per length:
    ``x.to(ohm_per_kft)``."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return ohm_per_km


class Impedance(Record, kw_only=False):
    r"""An impedance per length, :math:`z`: its resistance, :math:`\mathrm{Re}\,z`, and its
    reactance, :math:`\mathrm{Im}\,z`. It prints as ``0.08559 + j0.01744 Ω/km``."""

    resistance: ResistancePerLength
    """The resistance."""
    reactance: ReactancePerLength
    """The reactance."""

    def to(self, unit: Callable[[float], Quantity[OhmPerMeter]]) -> complex:
        """Complex impedance per length in the requested unit."""
        return complex(self.resistance.to(unit), self.reactance.to(unit))

    def __str__(self) -> str:
        r, x = self.resistance.to(ohm_per_km), self.reactance.to(ohm_per_km)
        return _complex(r, x, ohm_per_km)


class ConductancePerLength(Quantity[SiemensPerMeter]):
    """A conductance per length: 0.01 µS/km."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return us_per_km


def s_per_m(value: float) -> ConductancePerLength:
    """Siemens per meter."""
    return ConductancePerLength(value)


def us_per_km(value: float) -> ConductancePerLength:
    """Microsiemens per kilometer."""
    return ConductancePerLength(value * 1e-9)


class SusceptancePerLength(Quantity[SiemensPerMeter]):
    """A susceptance per length: 3.315 µS/km. It reads in the units of a conductance per length:
    ``b.to(us_per_km)``."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return us_per_km


class Admittance(Record, kw_only=False):
    r"""An admittance per length, :math:`y`: its conductance, :math:`\mathrm{Re}\,y`, and its
    susceptance, :math:`\mathrm{Im}\,y`. It prints as ``0 + j3.315 µS/km``."""

    conductance: ConductancePerLength
    """The conductance."""
    susceptance: SusceptancePerLength
    """The susceptance."""

    def to(self, unit: Callable[[float], Quantity[SiemensPerMeter]]) -> complex:
        """Complex admittance per length in the requested unit."""
        return complex(self.conductance.to(unit), self.susceptance.to(unit))

    def __str__(self) -> str:
        g, b = self.conductance.to(us_per_km), self.susceptance.to(us_per_km)
        return _complex(g, b, us_per_km)


class Conductance(Quantity[Siemens]):
    """Conductance in siemens."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return siemens


def siemens(value: float) -> Conductance:
    """Siemens."""
    return Conductance(value)


class Susceptance(Quantity[Siemens]):
    """Susceptance in siemens."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return siemens


class CharacteristicAdmittance(Record, kw_only=False):
    """Complex characteristic admittance, in siemens."""

    conductance: Conductance
    """Real part."""
    susceptance: Susceptance
    """Imaginary part."""

    def to(self, unit: Callable[[float], Quantity[Siemens]]) -> complex:
        """Complex characteristic admittance in the requested unit."""
        return complex(self.conductance.to(unit), self.susceptance.to(unit))

    def __str__(self) -> str:
        return _complex(self.conductance.si, self.susceptance.si, siemens)


class Attenuation(Quantity[ReciprocalMeter]):
    """Modal attenuation in nepers per meter."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return per_km


def per_m(value: float) -> Attenuation:
    """Per meter."""
    return Attenuation(value)


def per_km(value: float) -> Attenuation:
    """Per kilometer."""
    return Attenuation(value / 1000)


class PhaseConstant(Quantity[ReciprocalMeter]):
    """Modal phase constant in radians per meter."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return per_km


class PropagationConstant(Record, kw_only=False):
    """Modal propagation constant: attenuation plus j times phase constant."""

    attenuation: Attenuation
    """Real part, in nepers per unit length."""
    phase: PhaseConstant
    """Imaginary part, in radians per unit length."""

    def to(self, unit: Callable[[float], Quantity[ReciprocalMeter]]) -> complex:
        """Complex propagation constant in the requested reciprocal-length unit."""
        return complex(self.attenuation.to(unit), self.phase.to(unit))

    def __str__(self) -> str:
        return _complex(self.attenuation.to(per_km), self.phase.to(per_km), per_km)


class Duration(Quantity[Second]):
    """Elapsed seconds stored as a float, including submicrosecond delays."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return microseconds


def seconds(value: float) -> Duration:
    """Seconds."""
    return Duration(value)


def microseconds(value: float) -> Duration:
    """Microseconds."""
    return Duration(value * 1e-6)


class Elastance(Quantity[MeterPerFarad]):
    """An elastance: the voltage a charge per length gives, a capacitance per length's
    reciprocal: 145.2 km/µF."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return km_per_uf


def m_per_f(value: float) -> Elastance:
    """Meters per farad."""
    return Elastance(value)


def km_per_uf(value: float) -> Elastance:
    """Kilometers per microfarad."""
    return Elastance(value * 1e9)


class PotentialCoefficient(Record, kw_only=False):
    r"""A potential coefficient, :math:`p`: the voltage on a wire per charge per length on another,
    or on itself, its part in phase with the charge, :math:`\mathrm{Re}\,p`, and its part in
    quadrature, :math:`\mathrm{Im}\,p`, of the earth's losses. It prints as
    ``145.2 + j0 km/µF``."""

    real: Elastance
    """The part in phase."""
    imaginary: Elastance
    """The part in quadrature."""

    def to(self, unit: Callable[[float], Quantity[MeterPerFarad]]) -> complex:
        """Complex potential coefficient in the requested unit."""
        return complex(self.real.to(unit), self.imaginary.to(unit))

    def __str__(self) -> str:
        p, q = self.real.to(km_per_uf), self.imaginary.to(km_per_uf)
        return _complex(p, q, km_per_uf)


class Resistivity(Quantity[OhmMeter]):
    """A resistivity: a metal's 0.02826 Ω·mm²/m, or from an ohm meter on, the earth's
    100 Ω·m."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return ohm_mm2_per_m if abs(self.si) < 1 else ohm_m


def ohm_m(value: float) -> Resistivity:
    """Ohm meters."""
    return Resistivity(value)


def ohm_cmil_per_ft(value: float) -> Resistivity:
    """Ohm circular mils per foot."""
    return Resistivity(value * _CIRCULAR_MIL / _FOOT)


def ohm_mm2_per_m(value: float) -> Resistivity:
    """Ohm square millimeters per meter."""
    return Resistivity(value * 1e-6)


class ResistivityPerKelvin(Quantity[OhmMeterPerKelvin]):
    """How much a resistivity rises per kelvin: 0.0001139 Ω·mm²/(m·K)."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return ohm_mm2_per_m_k


def ohm_mm2_per_m_k(value: float) -> ResistivityPerKelvin:
    """Ohm square millimeters per meter, per kelvin."""
    return ResistivityPerKelvin(value * 1e-6)


class PerKelvin(Quantity[ReciprocalKelvin]):
    """A rate of change with temperature, such as a temperature coefficient: 0.00403 1/K."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return per_kelvin


def per_kelvin(value: float) -> PerKelvin:
    """Per kelvin."""
    return PerKelvin(value)


class Temperature(Quantity[Kelvin]):
    """A temperature: 75 °C. Temperatures compare, but neither add nor subtract: their scale
    starts from absolute zero, not from 0 °C."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return celsius

    def __add__(self, other: Self) -> Self:
        raise TypeError("temperatures don't add")

    def __sub__(self, other: Self) -> Self:
        raise TypeError("temperatures don't subtract; read each in celsius")


def celsius(value: float) -> Temperature:
    """Degrees Celsius."""
    return Temperature(value + 273.15)


class Frequency(Quantity[Hertz]):
    """A frequency: 60 Hz."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return hz


def hz(value: float) -> Frequency:
    """Hertz."""
    return Frequency(value)


class Current(Quantity[Ampere]):
    """An electric current: 1025 A."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return amperes


def amperes(value: float) -> Current:
    """Amperes."""
    return Current(value)


class Voltage(Quantity[Volt]):
    """A voltage, such as a line's between phases: 380 kV."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return kv


def kv(value: float) -> Voltage:
    """Kilovolts."""
    return Voltage(value * 1e3)


class Speed(Quantity[MeterPerSecond]):
    """A speed, such as the wind's: 0.61 m/s."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return m_per_s


def m_per_s(value: float) -> Speed:
    """Meters per second."""
    return Speed(value)


def ft_per_s(value: float) -> Speed:
    """Feet per second."""
    return Speed(value * _FOOT)


class Angle(Quantity[Radian]):
    """An angle: 90°."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return degrees


def degrees(value: float) -> Angle:
    """Degrees."""
    return Angle(math.radians(value))


class HeatFlux(Quantity[WattPerSquareMeter]):
    """A heat flux, such as the sun's on a surface: 1000 W/m²."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return w_per_m2


def w_per_m2(value: float) -> HeatFlux:
    """Watts per square meter."""
    return HeatFlux(value)


def w_per_ft2(value: float) -> HeatFlux:
    """Watts per square foot."""
    return HeatFlux(value / _FOOT**2)


class PowerPerLength(Quantity[WattPerMeter]):
    """A power per length, such as a conductor's heat gain or loss: 39.1 W/m."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return w_per_m


def w_per_m(value: float) -> PowerPerLength:
    """Watts per meter."""
    return PowerPerLength(value)


class Density(Quantity[KilogramPerCubicMeter]):
    """A density: 2703 kg/m³."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return kg_per_m3


def kg_per_m3(value: float) -> Density:
    """Kilograms per cubic meter."""
    return Density(value)


class SpecificHeat(Quantity[JoulePerKilogramKelvin]):
    """A heat capacity per mass: 955 J/(kg·K)."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return j_per_kg_k


def j_per_kg_k(value: float) -> SpecificHeat:
    """Joules per kilogram kelvin."""
    return SpecificHeat(value)


class HeatCapacityPerLength(Quantity[JoulePerMeterKelvin]):
    """A heat capacity per length, a conductor's: 1310 J/(m·K)."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return j_per_m_k


def j_per_m_k(value: float) -> HeatCapacityPerLength:
    """Joules per meter kelvin."""
    return HeatCapacityPerLength(value)


class ThermalConductivity(Quantity[WattPerMeterKelvin]):
    """A thermal conductivity, such as a conductor's across its strands: 1 W/(m·K)."""

    def _shown(self) -> Callable[[float], Quantity[Any]]:
        return w_per_m_k


def w_per_m_k(value: float) -> ThermalConductivity:
    """Watts per meter kelvin."""
    return ThermalConductivity(value)


SYMBOLS: dict[str, Callable[[float], Quantity[Any]]] = {
    "m": m, "km": km, "mi": mi, "cm": cm, "mm": mm, "in": inch, "ft": ft,
    "m²": m2, "mm²": mm2, "in²": in2, "cmil": cmil, "kcmil": kcmil,
    "kg/m": kg_per_m, "kg/km": kg_per_km, "lb/kft": lb_per_kft,
    "N/m": n_per_m,
    "N": n, "daN": dan, "kN": kn, "lbf": lbf, "klbf": klbf,
    "MPa": mpa, "GPa": gpa, "psi": psi, "ksi": ksi,
    "Ω/m": ohm_per_m, "Ω/km": ohm_per_km, "Ω/kft": ohm_per_kft, "Ω/mi": ohm_per_mi,
    "S/m": s_per_m, "µS/km": us_per_km, "S": siemens,
    "1/m": per_m, "1/km": per_km,
    "s": seconds, "µs": microseconds,
    "m/F": m_per_f, "km/µF": km_per_uf,
    "Ω·m": ohm_m, "Ω·cmil/ft": ohm_cmil_per_ft, "Ω·mm²/m": ohm_mm2_per_m,
    "Ω·mm²/(m·K)": ohm_mm2_per_m_k,
    "1/K": per_kelvin,
    "°C": celsius,
    "Hz": hz,
    "A": amperes,
    "kV": kv,
    "m/s": m_per_s, "ft/s": ft_per_s,
    "°": degrees,
    "W/m²": w_per_m2, "W/ft²": w_per_ft2, "W/m": w_per_m,
    "kg/m³": kg_per_m3, "J/(kg·K)": j_per_kg_k, "J/(m·K)": j_per_m_k, "W/(m·K)": w_per_m_k,
}  # fmt: skip
"""Each unit by its symbol, as openline prints it and its sources write it: ``SYMBOLS["Ω/km"]``
is ``ohm_per_km``."""
_SYMBOL_OF = {unit: name for name, unit in SYMBOLS.items()}


def symbol(unit: Callable[[float], Quantity[Any]]) -> str:
    """A unit's symbol: ``symbol(ohm_per_km)`` is ``Ω/km``."""
    return _SYMBOL_OF[unit]


def _complex(real: float, imaginary: float, unit: Callable[[float], Quantity[Any]]) -> str:
    """A complex value in a unit, ``0.08559 + j0.01744 Ω/km``: four figures of its larger
    part, and the smaller to the same place."""
    larger = max(abs(real), abs(imaginary))
    if larger:
        place = 3 - math.floor(math.log10(larger))
        real, imaginary = round(real, place) + 0.0, round(imaginary, place) + 0.0
    return f"{real:.4g} {'-' if imaginary < 0 else '+'} j{abs(imaginary):.4g} {symbol(unit)}"
