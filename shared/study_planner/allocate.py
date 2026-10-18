from shared.contract import Block, Task

def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """
    Phân bổ quỹ thời gian (hours) cho danh sách công việc theo chiến lược Greedy.
    """
    if hours <= 0:
        return []

    blocks = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        allocated_h = min(task.effort_h, remaining_hours)
        blocks.append(Block(task=task, hours=allocated_h))
        remaining_hours -= allocated_h

    return blocks
