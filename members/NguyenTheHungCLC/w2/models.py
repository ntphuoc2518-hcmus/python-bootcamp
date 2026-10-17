from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    title: str
    importance: int  # Từ 1 đến 5
    effort_h: float
    deadline: date

    def __post_init__(self):
        # Ràng buộc importance trong khoảng 1-5
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        # Tính số ngày còn lại tới deadline (không âm)
        delta = (self.deadline - today).days
        return max(0, delta)
