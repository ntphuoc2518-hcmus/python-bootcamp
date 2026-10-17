from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Phân bổ thời gian khả dụng cho danh sách công việc theo thuật toán Greedy."""
    blocks = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break
        # Lấy số giờ nhỏ hơn giữa thời lượng cần của task và số giờ còn rảnh
        allocated_h = min(task.effort_h, remaining_hours)
        blocks.append(Block(task=task, hours=allocated_h))
        remaining_hours -= allocated_h

    return blocks
