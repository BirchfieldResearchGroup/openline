"""Conductor figures: a cross section draws each wire where openline lays it, a round one a disc
and a trapezoidal one its sector of a band, and fills a ring of their area for wires it cannot
lay; a construction cuts each layer back from the one within it, its wires turning their
layer's lay and hand. How Sphinx places figures is test_sphinx's."""

import itertools
import math
import re
import xml.etree.ElementTree as ET
from dataclasses import replace

import pytest

from openline import conductors
from openline.conductors.astm import b231, b232, b524, b778, b857
from openline.conductors.csa.c61089 import OWL
from openline.conductors.iec.a2_syz import CODE_16_6_1
from openline.types import Missing
from openline.types.conductors import ACAR, Conductor
from openline.types.conductors.strands import Band, Center, Hand, HelicalBand, Helix, Ring
from openline.types.units import mm, mm2
from openline_sphinx.figures import cutback, section
from openline_sphinx.presentation.conductors import caption, figures

SVG = "{http://www.w3.org/2000/svg}"
UNLAID = replace(b231.ARBUTUS, wires=replace(b231.ARBUTUS.wires, count=5, diameter=mm(1)))
UNLAYERED = replace(  # trapezoidal wires whose layers no document gives
    b857.DRAKE, outer=replace(b857.DRAKE.outer, layers=None, outside_diameter=None)
)
ACAR_13 = next(v for v in vars(b524).values() if isinstance(v, ACAR) and v.core.count == 13)


def drawn(record: Conductor, view: str = "Cross section") -> ET.Element:
    (figure,) = (figure for figure in figures(record) if figure.heading == view)
    return ET.fromstring(figure.svg(interactive=True, occurrence="t-"))


def parts(root: ET.Element) -> dict[str, list[ET.Element]]:
    """Each part's groups, by its key, in drawing order."""
    found: dict[str, list[ET.Element]] = {}
    for group in root.iter(f"{SVG}g"):
        if "ol-part" in group.get("class", "").split():
            found.setdefault(group.attrib["data-ol-key"], []).append(group)
    return found


def test_every_section_draws_each_wire_openline_lays_once() -> None:
    for record in conductors.of(Conductor):
        layers, filled = section.laid(record)
        root = ET.fromstring(section.section(record, "", interactive=False, occurrence=""))
        groups = parts(root)
        assert list(groups) == [name for name, _ in reversed(record.parts)], record.title
        for name, strand in record.parts:
            (group,) = groups[name]
            discs = sum(
                wire is strand
                for layer in layers
                if not isinstance(layer, Band)
                for wire in layer.wires
            )
            sectors = sum(
                wire is strand
                for layer in layers
                if isinstance(layer, Band)
                for wire in layer.wires
            )
            unlaid = any(other is strand for other in filled)
            assert len(group.findall(f"{SVG}circle")) == discs, record.title
            assert discs + sectors == (0 if unlaid else strand.count), record.title
            assert len(group.findall(f"{SVG}path")) == sectors + unlaid, record.title


def test_trapezoidal_wires_draw_as_sectors_of_their_bands() -> None:
    record = b857.DRAKE
    layers, filled = section.laid(record)
    assert not filled
    bands = [layer for layer in layers if isinstance(layer, Band)]
    assert len(bands) == record.outer.layers
    root = drawn(record)
    groups = parts(root)
    assert len(groups["outer"][0].findall(f"{SVG}path")) == record.outer.count
    assert len(groups["core"][0].findall(f"{SVG}circle")) == record.core.count
    assert "layers as their standard counts" in root.attrib["aria-label"]


def test_aac_tw_lies_about_a_round_central_wire() -> None:
    record = b778.TULIP
    center, *bands = record.layers
    assert isinstance(center, Center)
    assert all(isinstance(band, Band) for band in bands)
    groups = parts(drawn(record))
    assert len(groups["wires"][0].findall(f"{SVG}circle")) == 1
    assert len(groups["wires"][0].findall(f"{SVG}path")) == record.wires.count - 1


def test_wires_openline_cannot_lay_fill_a_disc_of_their_area() -> None:
    assert section.laid(UNLAID) == ((), UNLAID.strands)
    root = drawn(UNLAID)
    ((group,),) = parts(root).values()
    assert not group.findall(f"{SVG}circle")
    (disc,) = group.findall(f"{SVG}path")
    assert disc.get("d") == section.circle(section.RADIUS)
    assert "Ø" not in "".join(root.itertext())
    assert "fill a ring of their area" in root.attrib["aria-label"]
    assert [figure.heading for figure in figures(UNLAID)] == ["Cross section"]


def test_unlayered_trapezoidal_wires_ring_the_core_by_their_area() -> None:
    record = UNLAYERED
    layers, filled = section.laid(record)
    assert filled == (record.outer,)
    core = layers[-1].outer_radius.to(mm)
    outside = math.sqrt(core**2 + record.outer.area.to(mm2) / math.pi)
    groups = parts(drawn(record))
    assert len(groups["core"][0].findall(f"{SVG}circle")) == record.core.count
    (ring,) = groups["outer"][0].findall(f"{SVG}path")
    inner = section.circle(core * section.RADIUS / outside)
    assert ring.get("d") == section.circle(section.RADIUS) + inner


def test_a_ring_of_two_parts_draws_each_in_its_own_group() -> None:
    assert any(
        len({id(wire) for wire in layer.wires}) == 2
        for layer in ACAR_13.layers
        if isinstance(layer, Ring)
    )
    groups = parts(drawn(ACAR_13))
    counts = {name: len(group.findall(f"{SVG}circle")) for name, (group,) in groups.items()}
    assert counts == {"core": 13, "outer": 24}


def test_parts_are_classed_and_shaded_by_their_material() -> None:
    root = drawn(b232.DRAKE)
    groups = parts(root)
    assert "ol-Aluminum" in groups["outer"][0].attrib["class"].split()
    assert "ol-Steel" in groups["core"][0].attrib["class"].split()
    shades = {node.attrib["id"]: node for node in root.iter(f"{SVG}radialGradient")}
    for name, (group,) in groups.items():
        shade = shades[group.attrib["fill"].removeprefix("url(#").removesuffix(")")]
        assert shade.attrib["class"].split()[1:] == group.attrib["class"].split()[1:], name


CONSTRUCTIONS = [  # three to eighty-four wires, two metals in one ring, one to six rings
    b232.DRAKE,
    OWL,
    ACAR_13,
    b231.ARBUTUS,
    b232.BLUEBIRD,
    next(
        c
        for c in conductors.of(Conductor)
        if cutback.helical(c) and any(len(layer.wires) == 3 for layer in c.layers)
    ),
]


def piece(root: ET.Element, identifier: str) -> ET.Element:
    (found,) = (node for node in root.iter() if node.get("id") == identifier)
    return found


def ends(path: str) -> tuple[tuple[float, float], tuple[float, float]]:
    """A path's first and last points."""
    numbers = [float(n) for n in re.findall(r"-?[0-9.]+", path)]
    return (numbers[0], numbers[1]), (numbers[-2], numbers[-1])


@pytest.mark.parametrize("record", CONSTRUCTIONS[:3])
def test_a_construction_turns_each_ring_its_lay_and_hand(record: Conductor) -> None:
    # A wire's front runs half a pitch either side of facing the viewer: 1/n of a lay along the
    # conductor, from a sin(π/n) above its axis to as far below, a right-hand lay falling.
    root = drawn(record, "Construction")
    scale = cutback.DIAMETER / record.diameter.to(mm)
    front = cutback.PIECES.index("front")
    for depth, layer in enumerate(record.layers):
        if not isinstance(layer, Helix):
            continue
        outline = piece(root, f"t-c{depth}p{front}")[0]
        (x0, y0), (x1, y1) = ends(outline.attrib["d"])
        n = len(layer.wires)
        assert x1 - x0 == pytest.approx(layer.lay.to(mm) * scale / n, abs=0.15)
        assert abs(y1) == pytest.approx(
            layer.radius.to(mm) * scale * math.sin(math.pi / n), abs=0.1
        )
        assert (y0 < 0 < y1) == (layer.hand is Hand.RIGHT), (record.title, depth)


@pytest.mark.parametrize("record", [b857.DRAKE, b778.TULIP], ids=lambda record: record.title)
def test_a_band_shows_closed_its_wires_meeting_seam_to_seam(record: Conductor) -> None:
    # A ribbon's trailing seam is its leading one a pitch on, outline to outline, and the passes
    # a pitch apart cover the band's cut at every height: no gap, and no wire behind another.
    root = drawn(record, "Construction")
    scale = cutback.DIAMETER / record.diameter.to(mm)
    for depth, (layer, (start, end)) in enumerate(
        zip(record.layers, cutback.cuts(len(record.layers)), strict=True)
    ):
        if not isinstance(layer, HelicalBand):
            continue
        lay, radius = layer.lay.to(mm) * scale, layer.outer.to(mm) * scale
        pitch = lay / len(layer.wires)
        leading, _, trailing = piece(root, f"t-c{depth}r")[0].attrib["d"].partition("H")
        first = [float(n) for n in re.findall(r"-?[0-9.]+", leading)]
        x, *rest = [float(n) for n in re.findall(r"-?[0-9.]+", trailing)]
        ahead = list(zip(first[::2], first[1::2], strict=True))
        back = [(x, ahead[-1][1]), *zip(rest[::2], rest[1::2], strict=True)][::-1]
        assert back == [pytest.approx((a + pitch, b), abs=0.11) for a, b in ahead]
        assert max(abs(y) for _, y in ahead) == pytest.approx(radius, abs=0.06)
        bases = sorted(
            float(use.attrib["x"])
            for use in root.iter(f"{SVG}use")
            if use.get("href") == f"#t-c{depth}r"
        )
        assert all(b - a == pytest.approx(pitch, abs=0.11) for a, b in itertools.pairwise(bases))
        assert bases[0] <= start - lay / 2 + pitch / 2
        assert bases[-1] >= end - pitch / 2


type Point = tuple[float, float, float]  # a wire's axis across the conductor, its depth toward
#                                          the viewer, and its half height on screen


def sampled(
    record: Conductor, depth: int, samples: int = 120
) -> tuple[list[tuple[float, list[Point | None]]], list[list[Point]], float]:
    """A helical layer's pieces as drawn, back to front, each by its pass and sampled across the
    layer's cut, None where the piece is not; every wire at each sample, drawn or not; and its
    wires' diameter, in drawing units."""
    layer = record.layers[depth]
    assert isinstance(layer, Helix)
    scale = cutback.DIAMETER / record.diameter.to(mm)
    lay, a = layer.lay.to(mm) * scale, layer.radius.to(mm) * scale
    d = layer.wires[0].diameter.to(mm) * scale
    cut = cutback.cuts(len(record.layers))[depth]
    xs = [cut[0] + (cut[1] - cut[0]) * (k + 0.5) / samples for k in range(samples)]
    spans = cutback.spans(len(layer.wires))

    def at(psi: float) -> Point:
        slope = 2 * math.pi * a * math.cos(psi) / lay
        return a * math.sin(psi), a * math.cos(psi), d / 2 * math.hypot(1, slope)

    drawn: list[tuple[float, list[Point | None]]] = []
    for name, base, _ in cutback.ordered(layer, lay, cut):
        low, high = spans[name][1]  # its body's span
        turns = [2 * math.pi * (x - base) / lay - math.pi / 2 for x in xs]
        drawn.append((base, [at(psi) if low <= psi <= high else None for psi in turns]))
    wires = len(layer.wires)
    every = [
        [at(2 * math.pi * (x + lay * (0.25 + i / wires)) / lay - math.pi / 2) for i in range(wires)]
        for x in xs
    ]
    return drawn, every, d


@pytest.mark.parametrize("record", CONSTRUCTIONS, ids=lambda record: record.title)
def test_every_wire_is_drawn_behind_those_in_front_of_it(record: Conductor) -> None:
    # Wherever two wires overlap on screen, the one drawn later is the nearer.
    for depth, layer in enumerate(record.layers):
        if not isinstance(layer, Helix):
            continue
        drawn, _, d = sampled(record, depth)
        for later, (base, points) in enumerate(drawn):
            for other, below in drawn[:later]:
                if other == base:
                    continue  # one pass's own pieces
                for here, there in zip(points, below, strict=True):
                    if here is None or there is None:
                        continue
                    if abs(here[0] - there[0]) < (here[2] + there[2]) * 0.98:
                        assert there[1] - here[1] < 0.01 * d, (record.title, depth)


@pytest.mark.parametrize("record", CONSTRUCTIONS, ids=lambda record: record.title)
def test_a_construction_s_outline_is_its_wires_outline(record: Conductor) -> None:
    # The wire nearest the outline is never more than half a pitch round from it, so what is
    # drawn reaches as far as all the wires do, above and below.
    for depth, layer in enumerate(record.layers):
        if not isinstance(layer, Helix):
            continue
        drawn, every, d = sampled(record, depth)
        for k, wires in enumerate(every):
            shown = [point for _, points in drawn if (point := points[k]) is not None]
            for side in (-1, 1):
                full = max(side * y + h for y, _, h in wires)
                assert max(side * y + h for y, _, h in shown) == pytest.approx(full, abs=0.01 * d)


@pytest.mark.parametrize("record", CONSTRUCTIONS[:3])
def test_half_a_ring_s_wires_lie_on_its_near_side_wherever_it_is_cut(record: Conductor) -> None:
    root = drawn(record, "Construction")
    scale = cutback.DIAMETER / record.diameter.to(mm)
    for depth, layer in enumerate(record.layers):
        if not isinstance(layer, Helix):
            continue
        lay = layer.lay.to(mm) * scale
        cut = cutback.cuts(len(record.layers))[depth]
        middle = (cut[0] + cut[1]) / 2
        spans = cutback.spans(len(layer.wires))
        near = set()
        for use in root.iter(f"{SVG}use"):
            found = re.fullmatch(rf"#t-c{depth}p(\d)", use.get("href", ""))
            if found is None:
                continue
            base = float(use.attrib["x"])
            low, high = spans[cutback.PIECES[int(found[1])]][1]
            psi = 2 * math.pi * (middle - base) / lay - math.pi / 2
            if low <= psi <= high and abs(psi) <= math.pi / 2:
                near.add(base)
        assert abs(len(near) - len(layer.wires) / 2) <= 0.5, (record.title, depth)


@pytest.mark.parametrize("record", CONSTRUCTIONS[:3])
def test_a_construction_colors_what_it_copies_by_its_parts_variables(
    record: Conductor,
) -> None:
    # A browser matches no selector of the page inside what a use copies: what it copies has no
    # class, and each stroke takes its color from a variable its part's group sets.
    root = drawn(record, "Construction")
    ids = {node.get("id"): node for node in root.iter() if node.get("id")}
    parents = {child: parent for parent in root.iter() for child in parent}
    for use in root.iter(f"{SVG}use"):
        group = parents[use]
        if "ol-part" not in group.get("class", "").split():
            continue  # a stroke within a piece
        copied = ids[use.attrib["href"][1:]]
        assert not [node.tag for node in copied.iter() if node.get("class")]
        strokes = [stroke.get("style") for stroke in copied]
        assert strokes == [f"stroke:var(--ol-{kind})" for kind in ("edge", "round", "shine")]
        variables = dict(item.split(":", 1) for item in group.attrib["style"].split(";") if item)
        for kind in ("round", "shine"):
            gradient = ids[variables[f"--ol-{kind}"].removeprefix("url(#").removesuffix(")")]
            assert len(ids[gradient.attrib["href"][1:]]) == 5  # its stops


def test_a_construction_needs_every_ring_s_lay_and_hand() -> None:
    for record in (UNLAYERED, UNLAID):
        assert not cutback.helical(record)
        with pytest.raises(Missing):
            cutback.cutback(record, "", interactive=False, occurrence="")
    assert cutback.helical(b232.DRAKE)
    assert [figure.heading for figure in figures(b232.DRAKE)] == ["Construction", "Cross section"]


@pytest.mark.parametrize("record", [b232.DRAKE, b857.DRAKE, OWL, ACAR_13, UNLAID])
def test_each_view_is_one_accessible_vector_svg(record: Conductor) -> None:
    ids: list[str] = []
    for index, figure in enumerate(figures(record)):
        static = ET.fromstring(figure.svg(interactive=False, occurrence="s-"))
        assert static.get("role") == "img"
        assert not any(n.get("role") == "button" or n.get("tabindex") for n in static.iter())
        root = ET.fromstring(figure.svg(interactive=True, occurrence=f"{index}-"))
        assert root.get("role") == "group"
        assert not any(node.tag.endswith("image") for node in root.iter())
        buttons = [n.attrib["data-ol-key"] for n in root.iter() if n.get("role") == "button"]
        assert sorted(buttons) == sorted(name for name, _ in record.parts)
        own = [node.attrib["id"] for node in root.iter() if node.get("id")]
        assert all(identifier.startswith(f"{index}-") for identifier in own)
        referenced = {
            value.removeprefix("#").removeprefix("url(#").removesuffix(")")
            for node in root.iter()
            for key in ("href", "fill", "clip-path")
            if (value := node.get(key)) and (value.startswith(("#", "url(#")) or "by" in key)
        }
        assert referenced <= set(own)
        text = "".join(root.itertext())
        assert all(section.wire(strand) in text for _, strand in record.parts)
        ids.extend(own)
    assert len(ids) == len(set(ids))


def test_a_laid_conductor_s_views_give_its_diameter() -> None:
    for figure in figures(b232.DRAKE):
        root = ET.fromstring(figure.svg(interactive=False, occurrence=""))
        assert f"Ø {b232.DRAKE.diameter.to(mm):.4g} mm" in "".join(root.itertext())


def test_wires_and_captions_are_named_as_documents_give_them() -> None:
    assert section.wire(b232.DRAKE.outer) == "26 round wires of 4.442 mm, Aluminum 1350-H19"
    assert caption(b232.DRAKE) == "ACSR Drake"
    assert caption(b857.DRAKE) == "ACSS/TW Drake"
    assert caption(CODE_16_6_1) == "AACSR 16"
