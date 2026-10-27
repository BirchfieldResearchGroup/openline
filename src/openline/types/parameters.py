"""Line parameters in phase or sequence coordinates, always per unit length."""

import cmath
from collections.abc import Callable
from typing import Literal

from . import Record
from .lines import Phases
from .units import (
    Admittance,
    ConductancePerLength,
    Impedance,
    ReactancePerLength,
    ResistancePerLength,
    SusceptancePerLength,
    ohm_per_m,
    s_per_m,
)

__all__ = ["Parameters", "Sequence"]


class Sequence(Record):
    """One diagonal sequence entry of a single circuit; coupling remains in the full matrices."""

    impedance: Impedance
    """Diagonal series impedance per length."""
    admittance: Admittance
    """Diagonal shunt admittance per length."""


class Parameters(Record):
    """Named series and shunt matrices in phase coordinates, or after ``sequence()``.

    Sequence order is zero, positive, negative for each ABC circuit. All circuit-to-circuit
    and sequence-to-sequence coupling is retained. Temperature and span assumptions are
    those of the line calculation that produced these per-length values.
    """

    impedance: Phases[Impedance]
    """Series impedance per length."""
    admittance: Phases[Admittance]
    """Shunt admittance per length."""
    basis: Literal["phase", "sequence"] = "phase"
    """Coordinate system of both matrices."""

    def sequence(self) -> "Parameters":
        """Transform every ABC circuit block using A inverse times M times A.

        This changes coordinates, not the physical line. It does not assume transposition.
        """
        self._phase_circuits()
        a = cmath.exp(2j * cmath.pi / 3)
        transform = ((1, 1, 1), (1, a * a, a), (1, a, a * a))
        inverse = tuple(tuple(transform[k][i].conjugate() / 3 for k in range(3)) for i in range(3))

        def convert(matrix: tuple[tuple[complex, ...], ...]) -> tuple[tuple[complex, ...], ...]:
            size = len(matrix)
            return tuple(
                tuple(
                    sum(
                        inverse[i % 3][r]
                        * matrix[i // 3 * 3 + r][k // 3 * 3 + c]
                        * transform[c][k % 3]
                        for r in range(3)
                        for c in range(3)
                    )
                    for k in range(size)
                )
                for i in range(size)
            )

        labels = tuple(
            f"{label.rsplit('.', 1)[0]}.{i % 3}" for i, label in enumerate(self.impedance.labels)
        )
        return self._converted(convert, labels, "sequence")

    def transposed(self) -> "Parameters":
        """Ideal phase averaging of a single ABC circuit, before sequence conversion.

        Multiple circuits require a specified transposition scheme and are not inferred.
        """
        self._phase_circuits()
        if len(self.impedance) != 3:
            raise ValueError("ideal transposition requires one three-phase circuit")

        def average(matrix: tuple[tuple[complex, ...], ...]) -> tuple[tuple[complex, ...], ...]:
            # Average the three cyclic phase placements; preserve both off-diagonal directions.
            return tuple(
                tuple(sum(matrix[(i + n) % 3][(k + n) % 3] for n in range(3)) / 3 for k in range(3))
                for i in range(3)
            )

        return self._converted(average, self.impedance.labels, "phase")

    @property
    def zero(self) -> Sequence:
        """Zero-sequence diagonal entry; off-diagonal coupling is not implied to vanish."""
        return self._diagonal(0)

    @property
    def positive(self) -> Sequence:
        """Positive-sequence diagonal entry of a single circuit."""
        return self._diagonal(1)

    @property
    def negative(self) -> Sequence:
        """Negative-sequence diagonal entry of a single circuit."""
        return self._diagonal(2)

    def _diagonal(self, index: int) -> Sequence:
        if self.basis != "sequence" or len(self.impedance) != 3:
            raise ValueError(
                "sequence diagonal access requires one circuit in sequence coordinates"
            )
        return Sequence(
            impedance=self.impedance[index][index], admittance=self.admittance[index][index]
        )

    def _phase_circuits(self) -> None:
        if self.basis != "phase":
            raise ValueError("parameters are already in sequence coordinates")
        labels = self.impedance.labels
        if not labels or len(labels) % 3:
            raise ValueError("sequence calculations require named three-phase circuits")
        for i in range(0, len(labels), 3):
            name = labels[i].rsplit(".", 1)[0]
            if labels[i : i + 3] != tuple(f"{name}.{phase}" for phase in "ABC"):
                raise ValueError(
                    "sequence calculations require phase order A, B, C in each circuit"
                )

    def _converted(
        self,
        convert: Callable[[tuple[tuple[complex, ...], ...]], tuple[tuple[complex, ...], ...]],
        labels: tuple[str, ...],
        basis: Literal["phase", "sequence"],
    ) -> "Parameters":
        z = convert(self.impedance.to(ohm_per_m))
        y = convert(self.admittance.to(s_per_m))
        return Parameters(
            impedance=Phases(
                tuple(
                    tuple(
                        Impedance(ResistancePerLength(v.real), ReactancePerLength(v.imag))
                        for v in row
                    )
                    for row in z
                ),
                labels,
            ),
            admittance=Phases(
                tuple(
                    tuple(
                        Admittance(ConductancePerLength(v.real), SusceptancePerLength(v.imag))
                        for v in row
                    )
                    for row in y
                ),
                labels,
            ),
            basis=basis,
        )
