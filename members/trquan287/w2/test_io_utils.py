from pathlib import Path

from .io_utils import load_tasks, save_json


def main():
    csv_path = Path("members/trquan287/w2/sample_tasks.csv")
    json_path = Path("members/trquan287/w2/tasks.json")

    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)

    save_json(tasks, json_path)

    print(f"Saved {len(tasks)} tasks to {json_path}")


if __name__ == "__main__":
    main()
