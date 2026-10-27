r"""Shunt admittance from external and earth potential coefficients.

Bare conductor surfaces are equipotential; there is no internal contribution.
"""

import math

from ..types.environment import Earth
from ..types.lines import Line, Phases, Placed
from ..types.units import (
    EPSILON_0,
    Admittance,
    ConductancePerLength,
    Elastance,
    Frequency,
    PotentialCoefficient,
    SusceptancePerLength,
    Temperature,
)
from . import _earth, _line, _wires

__all__ = ["admittance", "earth", "external"]


def admittance(line: Line, *, temperature: Temperature, frequency: Frequency) -> Phases[Admittance]:
    r"""Return the phase admittance matrix per unit length, ordered by circuit and phase.

    Each wire pair has external and earth potential coefficients:

    .. math::  P_{ik} = \frac{1}{2\pi\varepsilon_0}\left[\ln\frac{D_{ik}}{d_{ik}} + 2W_{ik}\right]

    Wires are placed at their mean catenary heights at ``temperature`` (``mechanical.sag``),
    using the same uniform geometry as series impedance. Bundle conductors share a voltage
    and shield wires are grounded:

    .. math::  \mathbf Y_\phi = j\omega\,\mathbf B^\mathsf T\mathbf P^{-1}\mathbf B

    Here :math:`B_{i\phi}` is one when wire :math:`i` belongs to phase :math:`\phi`, else zero
    (``_wires.collected``)."""
    wires = _line.hanging(line, temperature)
    placed = _line.mean_positions(line, wires, temperature)
    groups = _line.groups(wires)
    pairs = [(i, k) for i in range(len(wires)) for k in range(i + 1)]
    resistivity, permittivity = line.earth.resistivity.si, line.earth.relative_permittivity
    between = [_between(placed[i], placed[k]) for i, k in pairs]
    held = _earth.potentials(between, frequency.si, resistivity, permittivity)
    p = [[0j] * len(wires) for _ in wires]
    for (i, k), value in zip(pairs, held, strict=True):
        air = _complex(external(placed[i], placed[k]))
        p[i][k] = p[k][i] = air + value
    c = _wires.collected(p, groups)
    omega = 2 * math.pi * frequency.si
    rows = tuple(tuple(_admittance(1j * omega * value) for value in row) for row in c)
    return Phases(rows, line.labels)


def external(a: Placed, b: Placed) -> PotentialCoefficient:
    r"""Return the potential coefficient above a perfectly conducting earth.

    The image method uses wire separation :math:`d_{ik}` and the distance :math:`D_{ik}`
    from one wire to the other's image:

    .. math::  p = \frac{1}{2\pi\varepsilon_0}\ln\frac{D_{ik}}{d_{ik}}

    For a self-coefficient, :math:`d_{ii} = r_i` and :math:`D_{ii} = 2h_i`.
    The result is real."""
    near, image = _line.images(a, b)
    real = Elastance(math.log(image / near) / (2 * math.pi * EPSILON_0))
    return PotentialCoefficient(real, Elastance(0))


def earth(a: Placed, b: Placed, *, frequency: Frequency, earth: Earth) -> PotentialCoefficient:
    r"""Return the earth potential coefficient using the quasi-TEM model (Wise, 1948).

    The earth has conductivity :math:`\sigma` and relative permittivity :math:`\varepsilon_r`:

    .. math::  p = \frac{1}{\pi\varepsilon_0}\,W_{ik}, \qquad
               n^2 = \varepsilon_r - j\frac{\sigma}{\omega\varepsilon_0}

    :math:`W_{ik}` is Wise's integral (``_earth.wise``), using the constants from
    ``_earth._constants``. The propagation constant :math:`m` is shared with ``series.earth``.
    The correction vanishes for a perfectly conducting earth and is zero at DC."""
    resistivity, permittivity = earth.resistivity.si, earth.relative_permittivity
    (value,) = _earth.potentials([_between(a, b)], frequency.si, resistivity, permittivity)
    return PotentialCoefficient(Elastance(value.real), Elastance(value.imag))


def _between(a: Placed, b: Placed) -> tuple[float, float]:
    """Return the sum of wire heights and horizontal separation, in meters."""
    return a.point.height.si + b.point.height.si, abs(a.point.across.si - b.point.across.si)


def _complex(value: PotentialCoefficient) -> complex:
    return complex(value.real.si, value.imaginary.si)


def _admittance(value: complex) -> Admittance:
    """Convert to admittance and normalize signed zeros."""
    return Admittance(
        ConductancePerLength(value.real + 0.0), SusceptancePerLength(value.imag + 0.0)
    )
