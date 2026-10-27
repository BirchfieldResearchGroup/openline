"""Forward current-wave propagation and modal phase delays."""

from collections.abc import Iterator
from typing import overload

from . import Record
from .lines import Phases
from .units import CharacteristicAdmittance, Duration, Frequency, Length, PropagationConstant

__all__ = ["Propagation", "PropagationMode", "PropagationSweep"]


class PropagationMode(Record):
    """One current mode; its index is tracked across a frequency sweep."""

    constant: PropagationConstant
    """Attenuation plus j times phase constant, per unit length."""
    function: complex
    """Forward modal propagation factor exp(-constant * length)."""
    characteristic_admittance: CharacteristicAdmittance
    """Admittance in S, with unit-norm current modes and voltage scaled to preserve
    each mode's complex power. For current eigenvector q: Yc = gamma (qᴴq) / (qᴴZq).
    """
    phase_delay: Duration
    """Length times phase constant divided by angular frequency."""


class Propagation(Record):
    """Forward current propagation over a uniform line's specified length."""

    frequency: Frequency
    """Calculation frequency."""
    length: Length
    """Propagation distance, independent of the line's support span."""
    function: Phases[complex]
    """Dimensionless H: I+(x + length) = H I+(x)."""
    characteristic_admittance: Phases[CharacteristicAdmittance]
    """Full phase matrix Yc in siemens: I+ = Yc V+."""
    modes: tuple[PropagationMode, ...]
    """Modes sorted by phase constant initially, then tracked over a sweep."""


class PropagationSweep(Record):
    """Samples in increasing frequency order, with corresponding modal indices.

    Exactly repeated modes have no unique individual identity. The full phase matrices
    remain defined; refining the grid helps resolve nearby distinct modes.
    """

    samples: tuple[Propagation, ...]
    """Single-frequency results with modes tracked between adjacent samples."""

    def minimum_delays(self, *, magnitude_cutoff: float = 1e-5) -> tuple[Duration, ...]:
        """Estimate modal delays after accounting for attenuation's phase.

        Extract at each mode's first sample with ``|H| <= magnitude_cutoff``, or the
        last sample if no crossing occurs. Bode phase reconstruction uses the entire
        supplied sweep, including magnitudes below the cutoff; samples are retained.
        Requires at least three frequencies. For convergence, include magnitude data
        at least two decades either side of the extraction frequency. Estimates near
        a sweep boundary depend on the missing magnitude tails. This assumes a
        minimum-phase response after delay removal; it does not establish passivity.
        """
        from ..electrical._propagation import minimum_delays

        return minimum_delays(self, magnitude_cutoff=magnitude_cutoff)

    @overload
    def __getitem__(self, index: int) -> Propagation: ...
    @overload
    def __getitem__(self, index: slice) -> tuple[Propagation, ...]: ...
    def __getitem__(self, index: int | slice) -> Propagation | tuple[Propagation, ...]:
        return self.samples[index]

    def __iter__(self) -> Iterator[Propagation]:
        return iter(self.samples)

    def __len__(self) -> int:
        return len(self.samples)
