import csv
from datetime import date
from pathlib import Path

from ..contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {
            "title",
            "importance",
            "effort_h",
            "deadline",
        }

        if reader.fieldnames is None or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError("CSV is missing required columns")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )

                if not task.title:
                    raise ValueError("title cannot be empty")

                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid data at line {line_number}: {error}"
                ) from error

    return tasks
