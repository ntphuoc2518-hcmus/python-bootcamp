import csv
import json
from datetime import date
from dataclasses import asdict

from .models import Task

def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        expected_header = [
            "title",
            "importance",
            "effort_h",
            "deadline",
        ]

        if reader.fieldnames != expected_header:
            raise ValueError("Invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = []

    for task in tasks:
        task_data = asdict(task)
        task_data["deadline"] = task.deadline.isoformat()
        data.append(task_data)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
