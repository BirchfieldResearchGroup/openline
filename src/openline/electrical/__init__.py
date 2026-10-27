"""Conductor resistance, named line parameters, and current-wave propagation.

The ``series`` and ``shunt`` modules expose individual physical contributions for advanced work.
"""

import math
from collections.abc import Iterable
from itertools import pairwise

from ..types.lines import Line
from ..types.parameters import Parameters
from ..types.propagation import Propagation, PropagationSweep
from ..types.units import Frequency, Length, Temperature
from . import series, shunt
from ._series import (
    gmr,
    impedance,
    internal_impedance,
    magnetized,
    resistance,
    resistivity,
    temperature_coefficient,
)
from ._shunt import admittance

__all__ = [
    "admittance",
    "gmr",
    "impedance",
    "internal_impedance",
    "magnetized",
    "parameters",
    "propagation",
    "propagation_sweep",
    "resistance",
    "resistivity",
    "series",
    "shunt",
    "temperature_coefficient",
]


def parameters(line: Line, *, temperature: Temperature, frequency: Frequency) -> Parameters:
    """Both named line matrices per unit length, ready for sequence conversion."""
    return Parameters(
        impedance=impedance(line, temperature=temperature, frequency=frequency),
        admittance=admittance(line, temperature=temperature, frequency=frequency),
    )


def propagation(
    line: Line, *, temperature: Temperature, frequency: Frequency, length: Length
) -> Propagation:
    """Forward current propagation and characteristic admittance at one frequency.

    ``length`` is the transmission distance; ``line.span`` sets support geometry.
    Uses full coupled phase matrices, with Gamma = sqrt(YZ), H = exp(-length*Gamma),
    and Yc = solve(Gamma, Y). Requires the ``openline[propagation]`` extra.
    """
    return propagation_sweep(
        line, temperature=temperature, frequencies=(frequency,), length=length
    )[0]


def propagation_sweep(
    line: Line, *, temperature: Temperature, frequencies: Iterable[Frequency], length: Length
) -> PropagationSweep:
    """Current propagation at positive, strictly increasing frequencies.

    Modes are matched between adjacent samples by eigenvector overlap. Repeated modes
    have no unique individual identity. ``minimum_delays(magnitude_cutoff=1e-5)``
    estimates modal delays using magnitude-based cutoff and Bode phase reconstruction.
    It uses the supplied samples without additional line-parameter calculations.
    Requires the ``openline[propagation]`` extra.
    """
    sampled = tuple(frequencies)
    if not sampled or any(not math.isfinite(f.si) or f.si <= 0 for f in sampled):
        raise ValueError("propagation requires positive, finite frequencies")
    if any(a.si >= b.si for a, b in pairwise(sampled)):
        raise ValueError("propagation frequencies must be strictly increasing")
    if not math.isfinite(length.si) or length.si < 0:
        raise ValueError("propagation length must be finite and nonnegative")
    try:
        from ._propagation import calculate
    except ModuleNotFoundError as error:
        if error.name not in {"numpy", "scipy"}:
            raise
        raise ImportError("install 'openline[propagation]' for propagation calculations") from error
    return calculate(line, temperature=temperature, frequencies=sampled, length=length)
