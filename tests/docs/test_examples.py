"""Every example runs and prints. What their numbers should be is the library tests' to check:
the examples call the same functions."""

import runpy
from pathlib import Path

import matplotlib
import pytest

matplotlib.use("Agg")  # figures stay in memory; plt.show() opens no window

import matplotlib.pyplot as plt

EXAMPLES = sorted((Path(__file__).parents[2] / "examples").rglob("*.py"))


@pytest.mark.filterwarnings("ignore:.*cannot be shown:UserWarning")
@pytest.mark.parametrize(
    "example", EXAMPLES, ids=[f"{path.parent.name}/{path.stem}" for path in EXAMPLES]
)
def test_example_runs(example: Path, capsys: pytest.CaptureFixture[str]) -> None:
    try:
        runpy.run_path(str(example), run_name="__main__")
    finally:
        plt.close("all")
    assert capsys.readouterr().out
