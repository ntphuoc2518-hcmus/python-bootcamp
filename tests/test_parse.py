from datetime import date

import pytest

from shared.study_planner.parse import parse_csv


def test_parse_valid_csv(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6.0,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )

    tasks = parse_csv(csv_path)

    assert len(tasks) == 2
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 6.0
    assert tasks[0].deadline == date(2026, 10, 30)


def test_parse_empty_csv(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    assert parse_csv(csv_path) == []


def test_parse_missing_column(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,deadline\n"
        "DS exam,5,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(csv_path)


def test_parse_invalid_importance(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,high,6.0,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(csv_path)


def test_parse_invalid_deadline(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6.0,30-10-2026\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(csv_path)
