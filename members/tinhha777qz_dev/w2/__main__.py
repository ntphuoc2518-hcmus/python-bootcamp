"""W2-5 CLI entry point for running the w2 package directly.

Usage:
    python -m members.tinhha777qz_dev.w2
"""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks and print them."""
    # Look for tasks.csv in root samples/ or in current package directory
    root_sample = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    pkg_sample = Path(__file__).resolve().parent / "tasks.csv"

    csv_path = root_sample if root_sample.is_file() else pkg_sample

    tasks = load_tasks(csv_path)

    print("Week 2 - Task List")
    print("-" * 40)
    for task in tasks:
        print(f"- {task.title}: importance={task.importance}, effort={task.effort_h}h, deadline={task.deadline}")


if __name__ == "__main__":
    main()
