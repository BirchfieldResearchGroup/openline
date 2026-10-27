r"""Wire impedance matrices, magnetic coupling, and phase reduction in SI units."""

import cmath
import math
from collections.abc import Sequence
from typing import NamedTuple

from ..types.units import MU_0
from . import _bessel

__all__ = ["Laid", "Wire", "collected", "matrix", "own", "reduced", "solve"]


class Wire(NamedTuple):
    """A solid round wire of one metal."""

    x: float
    """Across, from the conductor's axis, in meters."""
    y: float
    """Up, from the conductor's axis, in meters."""
    radius: float
    """Its radius, in meters."""
    resistivity: float
    """Its resistivity, in ohm meters."""
    permeability: float
    """Its relative permeability."""


class Laid(NamedTuple):
    """A wire following a helical path around the conductor axis."""

    wire: Wire
    """The wire."""
    ring: float
    """The radius of its ring, in meters."""
    lay: float
    """The length along the conductor of one turn, in meters."""
    turn: int
    """The way it turns: 1 right-hand, -1 left-hand."""
    factor: float
    """How much longer it is than the conductor: its ring's stranding factor."""


def matrix(paths: Sequence[Wire | Laid], frequency: float) -> list[list[complex]]:
    r"""The wires' impedances per meter: with currents :math:`\mathbf I` along them, their
    voltages per length are :math:`\mathbf V = \mathbf Z\,\mathbf I`, against a return a meter
    away,

    .. math::

        Z_{ii} = z_i + j\frac{\omega\mu_0}{2\pi}\ln\frac{1}{r_i} + j\omega M_{ii}, \qquad
        Z_{ik} = j\frac{\omega\mu_0}{2\pi}\ln\frac{1}{d_{ik}} + j\omega M_{ik}

    with :math:`z_i` a wire's own impedance (``own``), :math:`r_i` its radius and :math:`d_{ik}`
    the distance between wires. A ring turns about the others along the span, and over a turn the
    mean log of the distance from a wire to another ring's wire is the log of the outer of their
    rings' radii, by the mean value of the logarithm over a circle,
    :math:`\overline{\ln d_{ik}} = \ln\max(a_i, a_k)`; within a ring the wires keep their places.
    A ring's current turns once in each lay :math:`\lambda`, so a ring is a solenoid, its field
    along the axis its current over its lay within it, and through another ring it links

    .. math::

        M_{ik} = \pm\frac{1}{\lambda_i\lambda_k}\,\Lambda\bigl(\min(a_i, a_k)\bigr), \qquad
        \Lambda(a) = \mu_0\Bigl[\pi a^2 + \sum_k (\mu_k - 1)\,A_k(a)\Bigr]

    plus where their rings turn the same way, the sum over every wire :math:`k`, :math:`A_k(a)`
    the part of its cross-section within the circle of radius :math:`a`. Along a wire of radius
    :math:`r_k`, the alternating field drives eddy currents that screen its middle, its
    permeability to the field

    .. math::

        \mu_k = \mu_r\,\frac{2 I_1(\kappa r_k)}{\kappa r_k\,I_0(\kappa r_k)}, \qquad
        \kappa = \sqrt{\frac{j\omega\mu_0\mu_r}{\rho}}

    which at DC is :math:`\mu_r`."""
    omega = 2 * math.pi * frequency
    wires = [_wire(path) for path in paths]
    rings = {path.ring for path in paths if isinstance(path, Laid)}
    permeance = {radius: _permeance(wires, radius, frequency) for radius in rings}
    found = []
    for i, a in enumerate(paths):
        row = []
        for b in paths:
            value = -1j * omega * MU_0 / (2 * math.pi) * math.log(_apart(a, b))
            if isinstance(a, Laid) and isinstance(b, Laid):
                inner = permeance[min(a.ring, b.ring)]
                value += 1j * omega * a.turn * b.turn * inner / (a.lay * b.lay)
            row.append(value)
        row[i] += own(a, frequency)
        found.append(row)
    return found


def own(path: Wire | Laid, frequency: float) -> complex:
    r"""A wire's own impedance per meter, of the field within it, Schelkunoff's (1934) in
    modified Bessel functions of the first kind,

    .. math::

        z = \frac{\kappa\rho}{2\pi r}\,\frac{I_0(\kappa r)}{I_1(\kappa r)}, \qquad
        \kappa = \sqrt{\frac{j\omega\mu_0\mu_r}{\rho}}

    with :math:`r` its radius, :math:`\rho` its resistivity and :math:`\mu_r` its relative
    permeability: at DC, :math:`\rho/\pi r^2`, and at low frequency
    :math:`\mathrm{Im}\,z = \omega\mu_0\mu_r/8\pi`. A wire laid at :math:`\theta` is longer than
    the conductor by its stranding factor :math:`\sec\theta`, and its impedance per length of
    conductor is :math:`\sec\theta` times a straight wire's."""
    if isinstance(path, Laid):
        return path.factor * _straight(path.wire, frequency)
    return _straight(path, frequency)


def reduced(z: list[list[complex]], groups: Sequence[Sequence[int]]) -> list[list[complex]]:
    r"""The impedance between groups of paths, each group's in parallel at one voltage, a phase's,
    and a path in no group at none, a grounded shield wire:

    .. math::  \left(\mathbf B^\mathsf T\,\mathbf Z^{-1}\mathbf B\right)^{-1}

    (``collected``)."""
    width = range(len(groups))
    identity = [[1 + 0j if g == h else 0j for h in width] for g in width]
    return solve(collected(z, groups), identity)


def collected(matrix: list[list[complex]], groups: Sequence[Sequence[int]]) -> list[list[complex]]:
    r"""What flows into each group of paths per volt of each group's voltage, each group's paths
    at its voltage, a phase's, and a path in no group at none: of impedances, the admittance
    between the groups, :math:`\mathbf B^\mathsf T\,\mathbf Z^{-1}\mathbf B`; of potential
    coefficients, their capacitance, :math:`\mathbf B^\mathsf T\,\mathbf P^{-1}\mathbf B`; with
    :math:`B_{i\phi}` one where path :math:`i` is of group :math:`\phi`, else zero."""
    width = range(len(groups))
    columns = [[1 + 0j if i in group else 0j for group in groups] for i in range(len(matrix))]
    shares = solve(matrix, columns)
    return [[sum(shares[i][h] for i in group) for h in width] for group in groups]


def solve(matrix: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    """Solve ``matrix @ X = right`` by Gaussian elimination with partial pivoting."""
    size, width = len(matrix), len(right[0])
    rows = [[*row, *values] for row, values in zip(matrix, right, strict=True)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda r: abs(rows[r][column]))
        rows[column], rows[pivot] = rows[pivot], rows[column]
        top = rows[column]
        for row in rows[column + 1 :]:
            factor = row[column] / top[column]
            if factor:
                for k in range(column, size + width):
                    row[k] -= factor * top[k]
    found = [[0j] * width for _ in range(size)]
    for r in reversed(range(size)):
        for c in range(width):
            known = sum(rows[r][k] * found[k][c] for k in range(r + 1, size))
            found[r][c] = (rows[r][size + c] - known) / rows[r][r]
    return found


def _wire(path: Wire | Laid) -> Wire:
    return path.wire if isinstance(path, Laid) else path


def _apart(a: Wire | Laid, b: Wire | Laid) -> float:
    """Return effective path separation in meters.

    Use wire radius for self-terms, outer radius between rings, and center distance otherwise."""
    if a is b:
        return _wire(a).radius
    if isinstance(a, Laid) and isinstance(b, Laid) and a.ring != b.ring:
        return max(a.ring, b.ring)
    p, q = _wire(a), _wire(b)
    return math.hypot(p.x - q.x, p.y - q.y)


def _permeance(wires: Sequence[Wire], radius: float, frequency: float) -> complex:
    """The axial flux per ampere-turn per meter through the circle of ``radius`` about the axis,
    in H m."""
    within: complex = math.pi * radius**2
    for wire in wires:
        part = _overlap(radius, math.hypot(wire.x, wire.y), wire.radius)
        within += (_axial(wire, frequency) - 1) * part
    return MU_0 * within


def _axial(wire: Wire, frequency: float) -> complex:
    """A wire's permeability to a field along it, eddy currents screening it."""
    if frequency == 0:
        return complex(wire.permeability)
    kappa = cmath.sqrt(2j * math.pi * frequency * MU_0 * wire.permeability / wire.resistivity)
    ratio = _bessel.i(1, kappa * wire.radius) / _bessel.i(0, kappa * wire.radius)
    return wire.permeability * 2 * ratio / (kappa * wire.radius)


def _overlap(radius: float, distance: float, wire: float) -> float:
    """The area common to a circle of ``radius`` about the axis and a wire's cross-section, of
    radius ``wire`` about a point ``distance`` from the axis, in square meters."""
    if distance + wire <= radius:
        return math.pi * wire**2
    if distance >= radius + wire:
        return 0.0
    if distance + radius <= wire:
        return math.pi * radius**2
    a = math.acos((distance**2 + wire**2 - radius**2) / (2 * distance * wire))
    b = math.acos((distance**2 + radius**2 - wire**2) / (2 * distance * radius))
    kite = (-distance + wire + radius) * (distance + wire - radius)
    kite *= (distance - wire + radius) * (distance + wire + radius)
    return wire**2 * a + radius**2 * b - math.sqrt(kite) / 2


def _straight(wire: Wire, frequency: float) -> complex:
    """A straight wire's own impedance per meter: ``own``'s equation."""
    if frequency == 0:
        return complex(wire.resistivity / (math.pi * wire.radius**2))
    kappa = cmath.sqrt(2j * math.pi * frequency * MU_0 * wire.permeability / wire.resistivity)
    ratio = _bessel.i(0, kappa * wire.radius) / _bessel.i(1, kappa * wire.radius)
    return kappa * wire.resistivity / (2 * math.pi * wire.radius) * ratio
