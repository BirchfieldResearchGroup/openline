"""One journal style for example figures, inline SVG, and vector downloads."""

import warnings
from collections.abc import Iterator
from contextlib import contextmanager
from io import BytesIO, StringIO
from typing import TYPE_CHECKING, Any, NamedTuple

if TYPE_CHECKING:
    from matplotlib.typing import RcKeyType

STYLE: dict["RcKeyType", Any] = {
    "figure.figsize": (7.2, 3.0),
    "figure.dpi": 120,
    "figure.facecolor": "white",
    "figure.constrained_layout.use": True,
    "figure.constrained_layout.w_pad": 0.08,
    "figure.constrained_layout.h_pad": 0.08,
    "figure.constrained_layout.wspace": 0.12,
    "figure.constrained_layout.hspace": 0.12,
    "savefig.dpi": 300,
    "savefig.facecolor": "white",
    "savefig.transparent": False,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "svg.fonttype": "path",
    "pdf.fonttype": 42,
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 9,
    "mathtext.fontset": "dejavusans",
    "axes.prop_cycle": (
        "cycler(color=['#0072b2', '#d55e00', '#009e73']) + cycler(linestyle=['-', '--', '-.'])"
    ),
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.6,
    "axes.labelcolor": "#222222",
    "axes.labelsize": 9,
    "axes.labelpad": 5,
    "axes.titlecolor": "#222222",
    "axes.titlesize": 9.5,
    "axes.titleweight": "normal",
    "axes.titlelocation": "center",
    "axes.titlepad": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "axes.formatter.use_mathtext": True,
    "axes.formatter.limits": (-3, 4),
    "axes.xmargin": 0.02,
    "axes.ymargin": 0.08,
    "grid.color": "#d0d0d0",
    "grid.linewidth": 0.35,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "xtick.labelcolor": "#222222",
    "ytick.labelcolor": "#222222",
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.minor.width": 0.4,
    "ytick.minor.width": 0.4,
    "text.color": "#222222",
    "legend.frameon": False,
    "legend.fontsize": 9,
    "legend.handlelength": 1.8,
    "legend.handletextpad": 0.5,
    "legend.columnspacing": 1,
    "lines.linewidth": 1.3,
    "lines.markersize": 3.5,
    "lines.markeredgewidth": 0.7,
    "lines.markerfacecolor": "white",
}
"""The style the documentation draws every example's figures in; the scripts set none."""


class Plot(NamedTuple):
    svg: str
    pdf: bytes


@contextmanager
def drawing() -> Iterator[list[Plot]]:
    """Capture each example figure as SVG and PDF, in the documentation's style."""
    found: list[Plot] = []
    try:
        import matplotlib
    except ImportError:
        yield found
        return
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with (
        matplotlib.rc_context(STYLE),
        warnings.catch_warnings(),
    ):
        warnings.filterwarnings("ignore", message=".*cannot be shown", category=UserWarning)
        try:
            yield found
            for number in plt.get_fignums():
                figure = plt.figure(number)
                title = figure.get_label() or "Example figure"
                drawn = StringIO()
                figure.savefig(drawn, format="svg", metadata={"Date": None, "Title": title})
                markup = drawn.getvalue()
                svg = markup[markup.index("<svg") :]
                pdf = BytesIO()
                figure.savefig(
                    pdf,
                    format="pdf",
                    metadata={"CreationDate": None, "ModDate": None, "Title": title},
                )
                found.append(Plot(svg, pdf.getvalue()))
        finally:
            plt.close("all")
