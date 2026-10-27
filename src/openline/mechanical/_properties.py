r"""Conductor mass, weight, elastic modulus, thermal expansion, and rated strength, calculated
from wire geometry, materials, and the rules of the conductor's standard."""

from collections.abc import Callable
from decimal import ROUND_HALF_EVEN, Decimal

from ..types import Missing
from ..types.conductors import Conductor
from ..types.conductors.strands import Center, Helical, Layer, Strand
from ..types.materials import Metal, Steel
from ..types.units import (
    GRAVITY,
    Force,
    ForcePerLength,
    MassPerLength,
    PerKelvin,
    Stress,
    kg_per_m,
    kn,
    lbf,
    n,
    n_per_m,
    per_kelvin,
)

__all__ = ["expansion", "mass", "masses", "modulus", "stiffness", "strength", "weight"]


def mass(conductor: Conductor) -> MassPerLength:
    r"""Return mass per meter from each wire's area, density, and stranding factor:

    .. math::  m = \sum_i \rho_i A_i \sec\theta_i"""
    return kg_per_m(sum(each.si for each in masses(conductor)))


def masses(conductor: Conductor) -> tuple[MassPerLength, ...]:
    """Return each strand's mass per meter, in conductor strand order (``mass``)."""
    found = dict.fromkeys(conductor.strands, 0.0)
    for layer in conductor.layers:
        factor = _factor(conductor, layer)
        for wire in layer.wires:
            found[wire] += wire.material.density.si * wire.area.si / wire.count * factor
    return tuple(kg_per_m(total) for total in found.values())


def weight(conductor: Conductor) -> ForcePerLength:
    """Weight per meter, under standard gravity."""
    return n_per_m(mass(conductor).si * GRAVITY)


def modulus(conductor: Conductor) -> Stress:
    r"""Return axial elastic modulus from strand stiffness and total cross-sectional area:

    .. math::  E = \frac{1}{A}\sum_s k_s"""
    return Stress(sum(k.si for k in stiffness(conductor)) / conductor.area.si)


def expansion(conductor: Conductor) -> PerKelvin:
    r"""Return the thermal expansion coefficient, weighted by axial strand stiffness:

    .. math::  \alpha = \frac{\sum_s \alpha_s k_s}{\sum_s k_s}"""
    parts = zip(stiffness(conductor), conductor.strands, strict=True)
    weighted = [(k.si, strand.material.expansion.si) for k, strand in parts]
    return per_kelvin(sum(k * a for k, a in weighted) / sum(k for k, _ in weighted))


def stiffness(conductor: Conductor) -> tuple[Force, ...]:
    r"""Return axial stiffness for each strand, in conductor strand order:

    .. math::  k_s = \sum_{i \in s} E_i A_i \cos^3\theta_i

    Each wire has modulus :math:`E_i`, area :math:`A_i`, and lay angle :math:`\theta_i`
    (zero for a straight wire). The stranding factor is :math:`\sec\theta_i`.
    Axial conductor strain produces wire strain :math:`\varepsilon\cos^2\theta`; the axial
    component of wire tension contributes another :math:`\cos\theta`. Bending and torsion
    are neglected. Missing lay or modulus raises ``Missing``."""
    found = []
    for strand in conductor.strands:
        metal = strand.material
        total = 0.0
        for layer in conductor.layers:
            turned = _factor(conductor, layer) ** -3
            wires = sum(1 for wire in layer.wires if wire == strand)
            total += wires * metal.modulus.si * strand.area.si / strand.count * turned
        found.append(n(total))
    return tuple(found)


def strength(conductor: Conductor, *, core: type[Steel] | None = None) -> Force:
    r"""Return rated breaking strength: each strand's wires, at their nominal diameter
    :math:`d_s`, take the stress :math:`\sigma_s` the conductor's standard rates them at
    (``Conductor.stress``), times its rating factor :math:`f_s`,

    .. math::  S = \sum_s f_s\,\sigma_s(d_s)\,A_s

    to three significant figures, in pounds-force or, sized in SI units, newtons (ASTM B231, 9;
    ASTM B232, 10; ASTM B399, 9.3; ASTM B524, 8; ASTM B856, 9; Practice E29). Aluminum takes
    its grade's tensile strength for conductor rating: a lot average for ASTM B230/B398/B609,
    an individual minimum for EN 50183. ``core`` is the grade of a core its design leaves open,
    one its standard names (``Conductor.grades``): ``strength(DRAKE, core=SteelGA2)``.
    Missing rating factors or stresses raise ``Missing``."""
    given = conductor.stranding or ()
    factors = [rule.rating_factor for rule in given if rule.rating_factor is not None]
    if not given or len(factors) != len(given):
        raise Missing(
            f"{conductor.title}: openline does not have {conductor.standard}'s rating factors"
        )
    if core is not None and core not in conductor.grades:
        raise ValueError(f"{conductor.standard} names no core of {core}")
    metric = conductor.designation.metric
    total = 0.0
    for strand, factor in zip(conductor.strands, factors, strict=True):
        metal = core if core is not None and issubclass(core, strand.material) else strand.material
        total += factor * conductor.stress(metal, strand.diameter, metric).si * strand.area.si
    return _three_figures(n(total), kn if metric else lbf)


def _three_figures(force: Force, unit: Callable[[float], Force]) -> Force:
    """A force rounded to three significant figures in ``unit``, half to even (Practice E29)."""
    value = Decimal(repr(force.to(unit)))
    step = Decimal(1).scaleb(value.adjusted() - 2)
    return unit(float(value.quantize(step, rounding=ROUND_HALF_EVEN)))


def _factor(conductor: Conductor, layer: Layer[Strand[Metal]]) -> float:
    """A layer's stranding factor: its helix's or helical band's, or one on the axis. A ring or
    band without lay raises ``Missing``."""
    match layer:
        case Helical():
            return layer.factor
        case Center():
            return 1.0
        case _:
            raise Missing(
                f"{conductor.title}: openline does not have {conductor.standard}'s lay for its "
                "rings"
            )
