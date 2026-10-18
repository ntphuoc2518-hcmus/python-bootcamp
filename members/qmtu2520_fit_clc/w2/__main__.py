from pathlib import Path

from .io_utils import load_tasks


def main():
    """Load sample tasks and print them."""
    csv_path = Path(__file__).resolve().parent / "tasks.csv"
    tasks = load_tasks(csv_path)

    print("Week 2 - Task list")
    print("-" * 40)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()