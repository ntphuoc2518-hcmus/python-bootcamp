import csv
import json
from datetime import datetime, date
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2): # Header nằm ở dòng 1
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()
                tasks.append(Task(title, importance, effort_h, deadline))
            except Exception as e:
                raise ValueError(f"Error on line {line_num}: {e}")
    return tasks

def save_json(tasks: list[Task], path: str):
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
        })
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
