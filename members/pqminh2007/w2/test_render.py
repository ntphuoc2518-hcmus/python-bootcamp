from datetime import date
from types import SimpleNamespace
from your_file import render  # Đổi your_file thành tên file chứa hàm render


# Tạo dữ liệu giả để kiểm tra
blocks = [
    SimpleNamespace(
        task=SimpleNamespace(
            title="Python Assignment",
            importance=5,
            deadline=date(2026, 10, 19)
        ),
        hours=3.5
    ),
    SimpleNamespace(
        task=SimpleNamespace(
            title="Database Project",
            importance=4,
            deadline=date(2026, 10, 21)
        ),
        hours=4.5
    ),
    SimpleNamespace(
        task=SimpleNamespace(
            title="English Practice",
            importance=3,
            deadline=date(2026, 10, 22)
        ),
        hours=2.0
    )
]

# Chạy thử hàm render
print(render(blocks))

# Kiểm tra tổng số giờ
result = render(blocks)
assert "Total" in result
assert "10.0" in result

# Kiểm tra danh sách rỗng
assert render([]) == "No tasks scheduled."

print("\nAll tests passed!")