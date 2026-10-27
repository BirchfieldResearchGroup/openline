"""Line geometry, stringing conditions, and circuits. Lines are user-defined."""

from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, overload

from . import Record
from .conductors import Conductor
from .environment import Earth
from .structures import Structure
from .structures.attachments import Attachment, Hold, Mount, Wire
from .structures.geometry import Point
from .units import (
    Admittance,
    CharacteristicAdmittance,
    Force,
    Impedance,
    Length,
    MeterPerFarad,
    OhmPerMeter,
    PotentialCoefficient,
    Quantity,
    Siemens,
    SiemensPerMeter,
    Temperature,
)

__all__ = [
    "Bundle",
    "Circuit",
    "Line",
    "Phase",
    "Phases",
    "Placed",
    "Shield",
    "Strung",
    "Suspended",
]

HUNG = (Hold.SUSPENSION, Hold.V_STRING)  # holds a mount hangs its wire below by its strings


class Strung(Record, kw_only=False):
    """Horizontal tension and temperature after creep: ``Strung(kn(28), celsius(15))``.

    All materials are assumed to have equal strain at this condition."""

    tension: Force
    """Its horizontal tension."""
    temperature: Temperature
    """The temperature it has that tension at."""


class Placed(Record, kw_only=False):
    """A wire of a radius at a point of a line's cross-section, the point's height above the
    earth: ``Placed(DRAKE.diameter / 2, Point(m(-5), m(0), m(20)))``."""

    radius: Length
    """Its outside radius."""
    point: Point
    """Where it is: across the line, and its height above the earth."""


class Bundle(Record):
    """Conductors equally spaced on a circle, with adjacent spacing ``spacing``."""

    conductor: Conductor
    """Each conductor."""
    count: int
    """How many conductors."""
    spacing: Length
    """The distance between neighbors."""

    def __post_init__(self) -> None:
        if self.count < 1 or (self.count > 1 and self.spacing.si <= 0):
            raise ValueError("a bundle needs a positive count and spacing between conductors")


class Phase(Record):
    """A phase conductor or bundle, its attachments, and stringing conditions."""

    conductor: Conductor | Bundle
    """What it is strung with: a conductor, or a bundle of them."""
    attachments: tuple[Attachment, ...]
    """Its attachments: one, or a strain structure's two, the wire midway between them."""
    strung: Strung
    """How each of its conductors is strung, which with its weight and the temperature sets the
    catenary it hangs in."""


class Suspended(Phase):
    """A phase suspended from mounts by insulator strings supplied with the line."""

    drop: Length
    """How far below its mounts its strings hold it."""


class Circuit(Record):
    """The phases of a circuit, in their order."""

    phases: tuple[Phase, ...]
    """Its phases."""
    labels: tuple[str, ...] = ()
    """Phase names in the same order; ABC by default for a three-phase circuit."""
    name: str | None = None
    """Optional circuit name, used in result labels such as west.A."""

    def __post_init__(self) -> None:
        if self.name is not None and (not self.name or "." in self.name):
            raise ValueError("a circuit name must be nonempty and contain no dots")
        labels = self.labels or (
            tuple("ABC")
            if len(self.phases) == 3
            else tuple(str(i + 1) for i in range(len(self.phases)))
        )
        if len(labels) != len(self.phases) or len(set(labels)) != len(labels):
            raise ValueError("each phase needs one distinct label")
        if any(not label or "." in label for label in labels):
            raise ValueError("phase labels must be nonempty and contain no dots")
        object.__setattr__(self, "labels", labels)

    @classmethod
    def uniform(
        cls,
        conductor: Conductor | Bundle,
        *,
        at: Mapping[str, Attachment | tuple[Attachment, ...]],
        strung: Strung,
        insulator_drop: Length | None = None,
        name: str | None = None,
    ) -> "Circuit":
        """Put identical conductors at named phase attachments, in mapping order.

        Supply an insulator drop for hanging mounts; omit it for catalog wire positions.
        A tuple groups strain attachments for one phase. Tension is per subconductor.
        """
        phases: list[Phase] = []
        for given in at.values():
            attachments = given if isinstance(given, tuple) else (given,)
            hung = bool(attachments) and all(
                isinstance(a, Mount) and a.hold in HUNG for a in attachments
            )
            if hung != (insulator_drop is not None):
                raise ValueError("supply insulator_drop only for phases hung below mounts")
            if insulator_drop is None:
                phases.append(Phase(conductor=conductor, attachments=attachments, strung=strung))
            else:
                phases.append(
                    Suspended(
                        conductor=conductor,
                        attachments=attachments,
                        strung=strung,
                        drop=insulator_drop,
                    )
                )
        return cls(phases=tuple(phases), labels=tuple(at), name=name)


class Shield(Record):
    """A shield wire, grounded at the structure."""

    conductor: Conductor
    """What it is strung with."""
    attachment: Attachment
    """Its attachment."""
    strung: Strung
    """How it is strung, which with its weight and the temperature sets the catenary it hangs
    in."""

    @classmethod
    def each(
        cls, conductor: Conductor, *, at: Iterable[Attachment], strung: Strung
    ) -> tuple["Shield", ...]:
        """Place the same grounded shield wire at each supplied attachment."""
        return tuple(cls(conductor=conductor, attachment=a, strung=strung) for a in at)


class Line(Record):
    """Conductors on a structure across a level span, with the structure datum at ``height``.

    Phases and shield wires use the corresponding structure attachments. Use ``Suspended``
    for phases hung below mounts."""

    structure: Structure[Any]
    """The structure."""
    height: Length
    """How high above the earth the structure's datum stands: one of its datum's heights, where
    it gives any."""
    span: Length
    """The length of the span, between structures alike."""
    circuits: tuple[Circuit, ...]
    """Its circuits."""
    shields: tuple[Shield, ...]
    """Its shield wires; none where it has none."""
    earth: Earth
    """The earth under it."""

    @property
    def circuit_names(self) -> tuple[str, ...]:
        """Circuit names: explicit names, or main for one circuit and 1, 2, ... otherwise."""
        return tuple(
            circuit.name or ("main" if len(self.circuits) == 1 else str(i + 1))
            for i, circuit in enumerate(self.circuits)
        )

    @property
    def labels(self) -> tuple[str, ...]:
        """Electrical matrix labels, in circuit and phase order."""
        return tuple(
            f"{name}.{phase}"
            for name, circuit in zip(self.circuit_names, self.circuits, strict=True)
            for phase in circuit.labels
        )

    def __post_init__(self) -> None:
        if len(set(self.circuit_names)) != len(self.circuits):
            raise ValueError("circuit names must be distinct; name each circuit explicitly")
        name, datum = self.structure.name, self.structure.datum
        if datum.heights and self.height not in datum.heights:
            raise ValueError(f"{name} is not built at {self.height}; its {datum}")
        held = set(self.structure.attachments)
        for circuit in self.circuits:
            for phase in circuit.phases:
                if not phase.attachments or any(
                    a not in held or a.wire is not Wire.PHASE for a in phase.attachments
                ):
                    raise ValueError(f"{name} holds no phase there")
                hung = all(isinstance(a, Mount) and a.hold in HUNG for a in phase.attachments)
                if hung and not isinstance(phase, Suspended):
                    raise ValueError(f"{name} hangs a phase below mounts: it is Suspended")
                if isinstance(phase, Suspended) and not hung:
                    raise ValueError(f"{name} holds a Suspended phase where its wire is")
        for shield in self.shields:
            if shield.attachment not in held or shield.attachment.wire is not Wire.SHIELD:
                raise ValueError(f"{name} holds no shield wire there")


class Phases[Q: (Impedance, Admittance, PotentialCoefficient, CharacteristicAdmittance, complex)](
    Record, kw_only=False
):
    """A named electrical matrix, ordered by circuit and phase.

    Integer row access and named access are available. Dimensionless matrices expose
    their numeric entries through ``rows``; quantities convert with ``to(unit)``.
    """

    rows: tuple[tuple[Q, ...], ...]
    """Its rows."""
    labels: tuple[str, ...] = ()
    """Row labels; empty for an unnamed matrix."""
    columns: tuple[str, ...] = ()
    """Column labels; default to row labels for a square matrix."""

    def __post_init__(self) -> None:
        if self.labels and not self.columns:
            object.__setattr__(self, "columns", self.labels)
        if self.labels and len(self.labels) != len(self.rows):
            raise ValueError("matrix row labels must match its rows")
        if self.columns and any(len(row) != len(self.columns) for row in self.rows):
            raise ValueError("matrix column labels must match its columns")

    @overload
    def __getitem__(self, phase: int) -> tuple[Q, ...]: ...
    @overload
    def __getitem__(self, phase: tuple[str, str]) -> Q: ...
    def __getitem__(self, phase: int | tuple[str, str]) -> tuple[Q, ...] | Q:
        if isinstance(phase, tuple):
            row, column = phase
            return self.rows[self.labels.index(row)][self.columns.index(column)]
        return self.rows[phase]

    @overload
    def to(
        self: "Phases[Impedance]", unit: Callable[[float], Quantity[OhmPerMeter]]
    ) -> tuple[tuple[complex, ...], ...]: ...
    @overload
    def to(
        self: "Phases[Admittance]", unit: Callable[[float], Quantity[SiemensPerMeter]]
    ) -> tuple[tuple[complex, ...], ...]: ...
    @overload
    def to(
        self: "Phases[PotentialCoefficient]", unit: Callable[[float], Quantity[MeterPerFarad]]
    ) -> tuple[tuple[complex, ...], ...]: ...
    @overload
    def to(
        self: "Phases[CharacteristicAdmittance]", unit: Callable[[float], Quantity[Siemens]]
    ) -> tuple[tuple[complex, ...], ...]: ...
    def to(self, unit: Callable[[float], Quantity[Any]]) -> tuple[tuple[complex, ...], ...]:
        """Numeric complex quantities in a unit, ready for ``numpy.asarray``."""

        def convert(value: Q) -> complex:
            if isinstance(value, complex):
                raise TypeError("dimensionless matrices need no conversion; use .rows")
            return value.to(unit)

        return tuple(tuple(convert(value) for value in row) for row in self.rows)

    def block(self, *, rows: str, columns: str) -> "Phases[Q]":
        """Select a block by circuit name, retaining row and column labels."""
        ri = [i for i, label in enumerate(self.labels) if label.split(".")[0] == rows]
        ci = [i for i, label in enumerate(self.columns) if label.split(".")[0] == columns]
        if not ri or not ci:
            raise KeyError(f"no matrix block for {rows!r}, {columns!r}")
        return Phases(
            tuple(tuple(self.rows[i][k] for k in ci) for i in ri),
            tuple(self.labels[i] for i in ri),
            tuple(self.columns[k] for k in ci),
        )

    def __len__(self) -> int:
        return len(self.rows)

    def __iter__(self) -> Iterator[tuple[Q, ...]]:
        return iter(self.rows)

    def __str__(self) -> str:
        cells: list[list[str]] = [[str(value) for value in row] for row in self.rows]
        if self.labels:
            cells = [
                ["", *self.columns],
                *[[label, *row] for label, row in zip(self.labels, cells, strict=True)],
            ]
        width = max((len(cell) for row in cells for cell in row), default=0)
        return "\n".join("  ".join(cell.rjust(width) for cell in row) for row in cells)
