"""W2-2 Load and save tasks in CSV and JSON formats."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file.

    Expected CSV header: title,importance,effort_h,deadline
    Raises ValueError with the line number for invalid rows.
    """
    path = Path(path)
    expected_header = ["title", "importance", "effort_h", "deadline"]
    tasks: list[Task] = []

    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("CSV file is empty (line 1)") from None

        clean_header = [col.strip() for col in header]
        if clean_header != expected_header:
            msg = (
                f"Invalid CSV header at line 1: expected {expected_header}, "
                f"got {clean_header}"
            )
            raise ValueError(msg)

        for line_number, row in enumerate(reader, start=2):
            if not row or not any(field.strip() for field in row):
                continue

            if len(row) != 4:
                msg = (
                    f"Invalid row at line {line_number}: "
                    f"expected 4 columns, got {len(row)}"
                )
                raise ValueError(msg)

            try:
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid data at line {line_number}: {exc}") from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save a list of Task objects to a JSON file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
