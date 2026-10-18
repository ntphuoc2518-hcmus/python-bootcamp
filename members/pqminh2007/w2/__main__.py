from pathlib import Path

from .io_utils import load_tasks, save_json


def main() -> None:
    tasks = load_tasks(Path("samples/tasks.csv"))
    for t in tasks:
        print(t)
    save_json(tasks, Path("tasks.json"))
    print(f"Saved {len(tasks)} tasks to tasks.json")


if __name__ == "__main__":
    main()