"""openline.types.parameters: a line's matrices in sequence coordinates, each three-phase circuit
by its symmetrical components with every coupling kept, and one circuit transposed ideally."""

import numpy as np
import pytest
from numpy.typing import NDArray

from openline.types.lines import Phases
from openline.types.parameters import Parameters
from openline.types.units import (
    Admittance,
    ConductancePerLength,
    Impedance,
    ReactancePerLength,
    ResistancePerLength,
    SusceptancePerLength,
    ohm_per_m,
    s_per_m,
)

type Matrix = NDArray[np.complex128]

A = np.exp(2j * np.pi / 3)
COMPONENTS = np.array([[1, 1, 1], [1, A**2, A], [1, A, A**2]])  # phases of zero, positive, negative
# A flat line's, in Ω/m: its middle phase nearer each outer one than they are to each other.
LINE: Matrix = 1e-5 * np.array(
    [[5 + 50j, 1 + 20j, 1 + 15j], [1 + 20j, 5 + 50j, 1 + 20j], [1 + 15j, 1 + 20j, 5 + 50j]],
    dtype=np.complex128,
)


def parameters(matrix: Matrix, labels: tuple[str, ...]) -> Parameters:
    """A matrix's numbers as both a line's impedance, in Ω/m, and its admittance, in S/m."""
    return Parameters(
        impedance=Phases(
            tuple(
                tuple(
                    Impedance(ResistancePerLength(v.real), ReactancePerLength(v.imag)) for v in row
                )
                for row in matrix
            ),
            labels,
        ),
        admittance=Phases(
            tuple(
                tuple(
                    Admittance(ConductancePerLength(v.real), SusceptancePerLength(v.imag))
                    for v in row
                )
                for row in matrix
            ),
            labels,
        ),
    )


def abc(*circuits: str) -> tuple[str, ...]:
    """Each circuit's phases, A, B and C."""
    return tuple(f"{circuit}.{phase}" for circuit in circuits for phase in "ABC")


SIX: Matrix = np.asarray(  # two circuits, every entry its own
    np.arange(36).reshape(6, 6) / 100 + 1j * np.arange(36, 72).reshape(6, 6) / 100,
    dtype=np.complex128,
)
DOUBLE = parameters(SIX, abc("west", "east"))


def coupling(given: Parameters) -> float:
    """The largest impedance between different sequences, over the largest of the line's."""
    matrix = np.asarray(given.sequence().impedance.to(ohm_per_m))
    return float(np.max(np.abs(matrix - np.diag(np.diag(matrix)))) / np.max(np.abs(LINE)))


def test_sequence_takes_each_circuit_to_its_symmetrical_components_keeping_every_coupling() -> None:
    blocks = np.kron(np.eye(2), COMPONENTS)
    expected = np.linalg.solve(blocks, SIX @ blocks)
    sequence = DOUBLE.sequence()
    np.testing.assert_allclose(sequence.impedance.to(ohm_per_m), expected, atol=1e-14)
    np.testing.assert_allclose(sequence.admittance.to(s_per_m), expected, atol=1e-14)


def test_sequence_labels_each_circuit_s_zero_positive_and_negative() -> None:
    labels = tuple(f"{circuit}.{n}" for circuit in ("west", "east") for n in "012")
    assert DOUBLE.sequence().impedance.labels == labels


def test_an_untransposed_circuit_s_sequences_couple() -> None:
    assert coupling(parameters(LINE, abc("main"))) > 0.01


def test_a_transposed_circuit_s_sequences_do_not_couple() -> None:
    assert coupling(parameters(LINE, abc("main")).transposed()) < 1e-14


def test_zero_positive_and_negative_are_the_sequence_matrix_s_diagonal() -> None:
    sequence = parameters(LINE, abc("main")).sequence()
    diagonal = [sequence.impedance[f"main.{n}", f"main.{n}"] for n in "012"]
    found = [each.impedance for each in (sequence.zero, sequence.positive, sequence.negative)]
    assert found == diagonal


def test_sequence_entries_are_of_sequence_coordinates_alone() -> None:
    with pytest.raises(ValueError, match="sequence coordinates"):
        _ = parameters(LINE, abc("main")).positive


def test_sequence_entries_are_of_one_circuit_alone() -> None:
    with pytest.raises(ValueError, match="one circuit"):
        _ = DOUBLE.sequence().positive


def test_only_one_circuit_transposes_ideally() -> None:
    with pytest.raises(ValueError, match="one three-phase circuit"):
        DOUBLE.transposed()


def test_sequence_coordinates_do_not_convert_again() -> None:
    with pytest.raises(ValueError, match="already in sequence coordinates"):
        DOUBLE.sequence().sequence()


def test_sequence_takes_phases_in_order_a_b_c() -> None:
    with pytest.raises(ValueError, match="phase order A, B, C"):
        parameters(LINE, ("main.B", "main.A", "main.C")).sequence()
