
import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path) -> list[Task]:
    """Load tasks from a CSV file with line-numbered validation errors."""
    tasks = []

    expected_header = ["title", "importance", "effort_h", "deadline"]

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("CSV file is empty (line 1).")

        header = [column.strip() for column in header]
        if header != expected_header:
            raise ValueError("Invalid CSV header at line 1.")

        for line_number, row in enumerate(reader, start=2):
            try:
                if len(row) != 4:
                    raise ValueError("Expected 4 columns.")

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
                raise ValueError(
                    f"Invalid data at line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks, path) -> None:
    """Save tasks to a JSON file."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
