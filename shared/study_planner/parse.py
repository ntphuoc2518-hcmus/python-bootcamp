import csv
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    tasks = []
    required_columns = {"title", "importance", "effort_h", "deadline"}

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain title, importance, effort_h, deadline"
            )

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
            except (ValueError, AttributeError, KeyError, TypeError) as error:
                raise ValueError(
                    f"Invalid data on line {line_number}"
                ) from error

            tasks.append(task)

    return tasks
