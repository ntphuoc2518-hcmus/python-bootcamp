from datetime import date
from types import SimpleNamespace

from shared.study_planner.render import render


def test_render_normal():
    blocks = [
        SimpleNamespace(
            task=SimpleNamespace(
                title="Python Assignment",
                importance=5,
                deadline=date(2026, 10, 19),
            ),
            hours=3.5,
        ),
        SimpleNamespace(
            task=SimpleNamespace(
                title="Database Project",
                importance=4,
                deadline=date(2026, 10, 21),
            ),
            hours=4.5,
        ),
    ]

    result = render(blocks)
    assert isinstance(result, str)
    assert "Python Assignment" in result
    assert "Database Project" in result
    assert "Total" in result


def test_render_empty():
    result = render([])
    assert result == "No tasks scheduled."