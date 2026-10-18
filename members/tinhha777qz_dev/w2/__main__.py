"""W2-5 CLI entry point for running the w2 package directly.

Usage:
    python -m members.tinhha777qz_dev.w2
"""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks and print them."""
    project_root = Path(__file__).resolve().parents[3]
    csv_path = project_root / "samples" / "tasks.csv"

    if not csv_path.exists():
        csv_path = Path("samples/tasks.csv")

    if csv_path.exists():
        tasks = load_tasks(csv_path)
        print("Week 2 - Task List")
        print("-" * 40)
        for task in tasks:
            print(f"- {task.title}: importance={task.importance}")
    else:
        print("Sample tasks file not found.")


if __name__ == "__main__":
    main()
