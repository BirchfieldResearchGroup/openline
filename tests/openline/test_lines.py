"""openline.types.lines: a line's records, which refuse a line its structure cannot hold; how a
line labels its circuits and phases; and the named matrices its calculations give. What those
matrices hold is test_electrical's."""

from dataclasses import FrozenInstanceError, replace

import pytest

from openline.conductors.astm.b232 import DRAKE, TURKEY
from openline.structures.frame import TH_230
from openline.structures.tower import D_2_D_2018_3_T1 as T1
from openline.types.environment import Earth
from openline.types.lines import Bundle, Circuit, Line, Phase, Phases, Shield, Strung, Suspended
from openline.types.structures.attachments import Attachment, Hold, Mount, Wire
from openline.types.structures.geometry import Point
from openline.types.units import (
    Impedance,
    Length,
    ReactancePerLength,
    celsius,
    kn,
    m,
    ohm_m,
    ohm_per_km,
)

STRUNG = Strung(kn(28), celsius(15))
EARTH = Earth(ohm_m(100), 10)


def hung(name: str | None = None) -> Circuit:
    """Drake hung 2.5 m below the three phase mounts of RUS's TH-230 H-frame."""
    phases = dict(zip("ABC", TH_230.phases, strict=True))
    return Circuit.uniform(DRAKE, at=phases, strung=STRUNG, insulator_drop=m(2.5), name=name)


def frame(*circuits: Circuit, shields: tuple[Shield, ...] = ()) -> Line:
    """A line on TH-230, its pole tops 22 m up, of ``circuits``, one hung by default."""
    return Line(
        structure=TH_230,
        height=m(22),
        span=m(300),
        circuits=circuits or (hung(),),
        shields=shields,
        earth=EARTH,
    )


def ohms(*rows: tuple[float, ...]) -> tuple[tuple[Impedance, ...], ...]:
    """Impedances whose resistance and reactance are each ``row``'s value, in ohms per km."""
    return tuple(
        tuple(Impedance(ohm_per_km(v), ReactancePerLength.of(ohm_per_km(v))) for v in row)
        for row in rows
    )


TWO = Phases(ohms((1, 2), (3, 4)), ("west.A", "east.A"))  # two circuits of a phase each


def test_a_circuit_of_three_phases_labels_them_a_b_c() -> None:
    assert Circuit(phases=hung().phases).labels == ("A", "B", "C")


def test_a_circuit_of_other_than_three_phases_numbers_them() -> None:
    assert Circuit(phases=hung().phases[:2]).labels == ("1", "2")


def test_each_phase_takes_one_distinct_label() -> None:
    with pytest.raises(ValueError, match="distinct label"):
        Circuit(phases=hung().phases, labels=("A", "A", "B"))


def test_a_phase_label_takes_no_dot() -> None:
    with pytest.raises(ValueError, match="no dots"):
        Circuit(phases=hung().phases, labels=("A", "B.1", "C"))


def test_a_circuit_name_takes_no_dot() -> None:
    with pytest.raises(ValueError, match="no dots"):
        hung("west.1")


def test_uniform_puts_its_conductor_at_each_named_attachment_in_order() -> None:
    circuit = hung()
    assert [phase.attachments for phase in circuit.phases] == [(a,) for a in TH_230.phases]
    assert circuit.labels == ("A", "B", "C")


@pytest.mark.parametrize(
    ("at", "drop"), [(TH_230.phases, None), (T1.phases[:3], m(2.5))], ids=["mounts", "wires"]
)
def test_uniform_takes_an_insulator_drop_only_for_phases_hung_below_mounts(
    at: tuple[Attachment, ...], drop: Length | None
) -> None:
    with pytest.raises(ValueError, match="insulator_drop"):
        Circuit.uniform(
            DRAKE, at=dict(zip("ABC", at, strict=True)), strung=STRUNG, insulator_drop=drop
        )


def test_shield_each_strings_a_shield_wire_at_each_attachment() -> None:
    shields = Shield.each(TURKEY, at=TH_230.shields, strung=STRUNG)
    assert tuple(shield.attachment for shield in shields) == TH_230.shields


def test_a_line_of_one_circuit_labels_it_main() -> None:
    assert frame().labels == ("main.A", "main.B", "main.C")


def test_a_named_circuit_labels_its_phases_with_its_name() -> None:
    assert frame(hung("west")).labels == ("west.A", "west.B", "west.C")


def test_unnamed_circuits_are_numbered() -> None:
    line = frame(hung(), hung())
    assert line.circuit_names == ("1", "2")
    assert line.labels == tuple(f"{name}.{phase}" for name in "12" for phase in "ABC")


def test_a_line_s_circuit_names_are_distinct() -> None:
    with pytest.raises(ValueError, match="distinct"):
        frame(hung("2"), hung())  # the second, unnamed, is also 2


def test_a_line_holds_phases_only_where_its_structure_holds_them() -> None:
    elsewhere = Mount(Wire.PHASE, Point(m(1), m(0), m(-1)), Hold.SUSPENSION)
    stray = Suspended(conductor=DRAKE, attachments=(elsewhere,), strung=STRUNG, drop=m(2.5))
    with pytest.raises(ValueError, match="holds no phase there"):
        frame(Circuit(phases=(stray,)))


def test_a_line_holds_shield_wires_only_where_its_structure_holds_them() -> None:
    misplaced = Shield(conductor=TURKEY, attachment=TH_230.phases[0], strung=STRUNG)
    with pytest.raises(ValueError, match="holds no shield wire there"):
        frame(shields=(misplaced,))


def test_a_line_stands_at_a_height_its_structure_is_built_at() -> None:  # 26 to 50 m
    phases = dict(zip("ABC", T1.phases[:3], strict=True))
    circuit = Circuit.uniform(DRAKE, at=phases, strung=STRUNG)
    with pytest.raises(ValueError, match="not built at 3 m"):
        Line(structure=T1, height=m(3), span=m(300), circuits=(circuit,), shields=(), earth=EARTH)


def test_a_phase_hung_below_mounts_is_suspended() -> None:
    held = Phase(conductor=DRAKE, attachments=(TH_230.phases[0],), strung=STRUNG)
    with pytest.raises(ValueError, match="it is Suspended"):
        frame(Circuit(phases=(held,)))


def test_a_suspended_phase_hangs_only_below_mounts() -> None:
    wire = Suspended(conductor=DRAKE, attachments=(T1.phases[0],), strung=STRUNG, drop=m(2.5))
    with pytest.raises(ValueError, match="Suspended phase where its wire is"):
        Line(
            structure=T1,
            height=m(26),
            span=m(300),
            circuits=(Circuit(phases=(wire,)),),
            shields=(),
            earth=EARTH,
        )


@pytest.mark.parametrize(("count", "spacing"), [(0, 0.457), (2, 0)], ids=["none", "touching"])
def test_a_bundle_has_conductors_spaced_apart(count: int, spacing: float) -> None:
    with pytest.raises(ValueError, match="positive count and spacing"):
        Bundle(conductor=DRAKE, count=count, spacing=m(spacing))


def test_a_line_changes_only_by_replacement() -> None:
    line = frame()
    with pytest.raises(FrozenInstanceError):
        line.height = m(23)  # type: ignore[misc]
    assert replace(line, height=m(23)).height == m(23)


def test_a_matrix_reads_by_label_as_by_place() -> None:
    assert TWO["west.A", "east.A"] == TWO[0][1]


def test_a_matrix_block_is_one_circuit_against_another() -> None:
    block = TWO.block(rows="east", columns="west")
    assert (block.rows, block.labels, block.columns) == (ohms((3,)), ("east.A",), ("west.A",))


def test_a_matrix_has_no_block_for_a_circuit_it_lacks() -> None:
    with pytest.raises(KeyError, match="main"):
        TWO.block(rows="main", columns="west")


def test_a_matrix_reads_in_a_unit_as_complex_numbers() -> None:
    assert TWO.to(ohm_per_km) == ((1 + 1j, 2 + 2j), (3 + 3j, 4 + 4j))


def test_a_dimensionless_matrix_reads_only_as_its_rows() -> None:
    with pytest.raises(TypeError, match="rows"):
        Phases(((1 + 0j,),)).to(ohm_per_km)  # type: ignore[misc]


def test_a_matrix_s_labels_are_its_rows() -> None:
    with pytest.raises(ValueError, match="row labels"):
        Phases(ohms((1, 2), (3, 4)), ("main.A",))


def test_a_matrix_prints_each_value_against_its_labels() -> None:
    header, *rows = [line.split("  ") for line in str(TWO).splitlines()]
    cells = [[cell.strip() for cell in row if cell.strip()] for row in [header, *rows]]
    assert cells == [
        ["west.A", "east.A"],
        ["west.A", str(TWO[0][0]), str(TWO[0][1])],
        ["east.A", str(TWO[1][0]), str(TWO[1][1])],
    ]
