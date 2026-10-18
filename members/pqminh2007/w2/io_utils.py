import csv
import json
from datetime import date, datetime
from pathlib import Path

from members.pqminh2007.w2.models import Task

# Các định dạng ngày chấp nhận được (WPS/Excel hay lưu dạng tháng/ngày/năm)
DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y")


def parse_deadline(text: str) -> date:
    """Chuyển chuỗi ngày thành date, thử lần lượt từng định dạng."""
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date: {text!r}")


def load_tasks(csv_path: str | Path) -> list[Task]:
    """Đọc danh sách task từ file CSV (title, priority, work_hours, deadline)."""
    tasks = []
    path = Path(csv_path)

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # bỏ dòng header

        for line_num, row in enumerate(reader, start=2):
            # Bỏ qua dòng trống hoặc dòng chỉ có dấu phẩy
            if not row or all(cell.strip() == "" for cell in row):
                continue

            if len(row) < 4:
                raise ValueError(f"Invalid format at line {line_num}")

            title, priority, work_hours, deadline = (cell.strip() for cell in row[:4])

            try:
                task = Task(
                    title=title,
                    priority=int(priority),
                    work_hours=float(work_hours),
                    deadline=parse_deadline(deadline),
                )
            except ValueError as e:
                raise ValueError(f"Invalid format at line {line_num}: {e}") from e

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], json_path: str | Path) -> None:
    """Lưu danh sách task ra file JSON."""
    path = Path(json_path)
    data = [
        {
            "title": t.title,
            "priority": t.priority,
            "work_hours": t.work_hours,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]

    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )