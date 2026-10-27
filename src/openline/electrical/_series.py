r"""Series impedance from internal, external, and earth-return contributions."""

import math
from functools import lru_cache

from ..types import Missing
from ..types.conductors import Conductor, SteelCored
from ..types.conductors.strands import Center, Hand, HelicalBand, Helix
from ..types.environment import Earth
from ..types.lines import Line, Phases, Placed
from ..types.materials import Metal
from ..types.units import (
    MU_0,
    Frequency,
    Impedance,
    Length,
    PerKelvin,
    ReactancePerLength,
    ResistancePerLength,
    Resistivity,
    Temperature,
    celsius,
    per_kelvin,
)
from . import _earth, _line, _wires

__all__ = [
    "earth",
    "external",
    "gmr",
    "impedance",
    "internal_impedance",
    "magnetized",
    "resistance",
    "resistivity",
    "temperature_coefficient",
]


def impedance(line: Line, *, temperature: Temperature, frequency: Frequency) -> Phases[Impedance]:
    r"""Return the phase impedance matrix per unit length, ordered by circuit and phase.

    Each wire pair contributes internal, external, and earth-return impedance:

    .. math::  Z_{ik} = \delta_{ik}\,z_i
               + j\frac{\omega\mu_0}{2\pi}\left[\ln\frac{D_{ik}}{d_{ik}} + 2J_{ik}\right]

    Wires are placed at their mean catenary heights at ``temperature`` (``mechanical.sag``),
    using the same uniform geometry as shunt admittance. Bundle conductors share a voltage;
    shield wires are grounded. The wire matrix is reduced to phases by ``_wires.reduced``:

    .. math::  \mathbf Z_\phi = \left(\mathbf B^\mathsf T\mathbf Z^{-1}\mathbf B\right)^{-1}

    Here :math:`B_{i\phi}` is one when wire :math:`i` belongs to phase :math:`\phi`, else zero.
    Temperature sets the sag of both phase and shield wires. Stringing tension is per
    subconductor; the conductor model uses fixed permeability independent of current."""
    wires = _line.hanging(line, temperature)
    placed = _line.mean_positions(line, wires, temperature)
    own = []
    for wire in wires:
        own.append(
            _complex(
                internal_impedance(wire.conductor, temperature=temperature, frequency=frequency)
            )
        )
    pairs = [(i, k) for i in range(len(wires)) for k in range(i + 1)]

    z = [[0j] * len(wires) for _ in wires]
    for i, k in pairs:
        air = external(placed[i], placed[k], frequency=frequency)
        returned = earth(placed[i], placed[k], frequency=frequency, earth=line.earth)
        z[i][k] = z[k][i] = _complex(air) + _complex(returned)
    for i, value in enumerate(own):
        z[i][i] += value
    rows = _wires.reduced(z, _line.groups(wires))
    return Phases(tuple(tuple(map(_impedance, row)) for row in rows), line.labels)


def internal_impedance(
    conductor: Conductor,
    *,
    temperature: Temperature,
    frequency: Frequency,
) -> Impedance:
    r"""Return conductor internal impedance per unit length; zero frequency gives DC resistance.

    Combine parallel wire impedances and mutual coupling (``_wires.matrix``), then subtract
    the external field contribution:

    .. math::  z = \left(\mathbf 1^\mathsf T\mathbf Z^{-1}\mathbf 1\right)^{-1}
               - j\frac{\omega\mu_0}{2\pi}\ln\frac{1}{r}

    Here :math:`\mathbf Z` is the wire impedance matrix and :math:`r` the conductor radius.
    All wires conduct, including coated-steel cores (ASTM B232, 12.2). Material resistivity
    varies with temperature; relative permeability is fixed, independent of current.
    Missing lay or direction of lay raises ``Missing``."""
    within = _internal(conductor, temperature, frequency)
    outside = frequency.si * MU_0 * math.log(2 / conductor.diameter.si)
    return _impedance(within - 1j * outside)


def resistance(
    conductor: Conductor, *, temperature: Temperature, frequency: Frequency
) -> ResistancePerLength:
    """Conductor resistance per length at temperature and frequency; use zero Hz for DC."""
    return internal_impedance(conductor, temperature=temperature, frequency=frequency).resistance


def external(a: Placed, b: Placed, *, frequency: Frequency) -> Impedance:
    r"""Return external impedance per unit length above a perfectly conducting earth.

    The image method uses wire separation :math:`d_{ik}` and the distance :math:`D_{ik}`
    from one wire to the other's image:

    .. math::  z = j\frac{\omega\mu_0}{2\pi}\ln\frac{D_{ik}}{d_{ik}}

    For self-impedance, :math:`d_{ii} = r_i` and :math:`D_{ii} = 2h_i`.
    The result is purely reactive."""
    near, image = _line.images(a, b)
    reactance = ReactancePerLength(_earth.external(near, image, frequency.si))
    return Impedance(ResistancePerLength(0), reactance)


def earth(a: Placed, b: Placed, *, frequency: Frequency, earth: Earth) -> Impedance:
    r"""Return earth-return impedance per unit length using the quasi-TEM model (Wise, 1948).

    For wires at heights :math:`h_i`, :math:`h_k` and horizontal separation :math:`x_{ik}`,
    above earth with conductivity :math:`\sigma` and relative permittivity
    :math:`\varepsilon_r`:

    .. math::  z = j\frac{\omega\mu_0}{\pi}\,J_{ik}, \qquad
               m^2 = j\omega\mu_0\bigl[\sigma + j\omega\varepsilon_0(\varepsilon_r - 1)\bigr]

    :math:`J_{ik}` is the full Carson integral (``_earth.carson``):

    .. math::  J_{ik} = \int_0^\infty
               \frac{e^{-(h_i+h_k)\xi}\cos(x_{ik}\xi)}{\xi+\sqrt{\xi^2+m^2}}\,d\xi

    Evaluate its Struve-Bessel closed form to floating-point precision. Setting
    :math:`\varepsilon_r = 1` gives :math:`m^2 = j\omega\mu_0\sigma` and recovers Carson's
    (1926) conduction-only series impedance. This does not remove the finite-conductivity
    correction from the shunt model."""
    above = a.point.height.si + b.point.height.si
    apart = abs(a.point.across.si - b.point.across.si)
    resistivity, permittivity = earth.resistivity.si, earth.relative_permittivity
    z = _earth.earth(above, apart, frequency.si, resistivity, permittivity)
    return _impedance(z)


def gmr(conductor: Conductor, *, temperature: Temperature, frequency: Frequency) -> Length:
    r"""Return geometric mean radius from internal inductance at a positive frequency:

    .. math::  \mathrm{GMR} = r\,e^{-2\pi\,\mathrm{Im}\,z/\omega\mu_0}

    Here :math:`r` is the conductor radius and :math:`z` its internal impedance
    (``internal_impedance``).
    GMR approaches :math:`r` as frequency increases and current crowds toward the surface."""
    if frequency.si <= 0:
        raise ValueError("GMR requires a positive frequency")
    reactance = internal_impedance(
        conductor, temperature=temperature, frequency=frequency
    ).reactance.si
    return conductor.diameter / 2 * math.exp(-reactance / (frequency.si * MU_0))


def resistivity(metal: type[Metal], *, temperature: Temperature) -> Resistivity:
    r"""Return resistivity using a linear temperature correction from 20 °C.

    Grades and alloys share their base metal's resistivity slope (NBS Handbook 100, p. 14,
    Matthiessen's rule):

    .. math::  \rho(T) = \rho_{20} + \frac{d\rho}{dT}\,(T - 20\ ^\circ\mathrm{C})"""
    rise = temperature.to(celsius) - 20
    rho = metal.resistivity.si + metal.resistivity_rise.si * rise
    return Resistivity(rho)


def temperature_coefficient(metal: type[Metal]) -> PerKelvin:
    r"""Return the resistance temperature coefficient at 20 °C and constant mass:
    :math:`(d\rho/dT)/\rho_{20}`."""
    return per_kelvin(metal.resistivity_rise.si / metal.resistivity.si)


def magnetized(conductor: Conductor) -> bool:
    """Flag steel cores with an odd number of aluminum layers, rings or bands (IEEE 738-2023,
    4.4.6.3), and any whose layers are not known."""
    if not isinstance(conductor, SteelCored):
        return False
    try:
        layers = conductor.layers
    except Missing:
        return True
    return sum(conductor.outer in layer.wires for layer in layers) % 2 == 1


@lru_cache(maxsize=4096)
def _internal(conductor: Conductor, temperature: Temperature, frequency: Frequency) -> complex:
    """Calculate the wires' impedance in parallel."""
    paths = _wires_of(conductor, temperature)
    z = _wires.matrix(paths, frequency.si)
    ((within,),) = _wires.reduced(z, [range(len(paths))])
    return within


def _wires_of(conductor: Conductor, temperature: Temperature) -> list[_wires.Wire | _wires.Laid]:
    """Build wire paths with layer geometry, resistivity, and material permeability."""
    found: list[_wires.Wire | _wires.Laid] = []
    for layer in conductor.layers:
        for place, strand in enumerate(layer.wires):
            radius = strand.diameter.si / 2
            rho = resistivity(strand.material, temperature=temperature).si
            mu = strand.material.relative_permeability
            match layer:
                case Helix() | HelicalBand() if layer.hand is None:
                    raise Missing(
                        f"{conductor.title}: openline does not have {conductor.standard}'s "
                        "direction of lay"
                    )
                case Helix() | HelicalBand():
                    angle = 2 * math.pi * place / len(layer.wires)
                    x, y = layer.radius.si * math.cos(angle), layer.radius.si * math.sin(angle)
                    turn = 1 if layer.hand is Hand.RIGHT else -1
                    wire = _wires.Wire(x, y, radius, rho, mu)
                    found.append(
                        _wires.Laid(wire, layer.radius.si, layer.lay.si, turn, layer.factor)
                    )
                case Center():
                    found.append(_wires.Wire(0.0, 0.0, radius, rho, mu))
                case _:
                    raise Missing(
                        f"{conductor.title}: openline does not have {conductor.standard}'s lay "
                        "for its rings"
                    )
    return found


def _complex(value: Impedance) -> complex:
    return complex(value.resistance.si, value.reactance.si)


def _impedance(value: complex) -> Impedance:
    return Impedance(ResistancePerLength(value.real), ReactancePerLength(value.imag))
