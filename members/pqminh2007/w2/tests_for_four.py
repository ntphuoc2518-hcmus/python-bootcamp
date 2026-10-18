import pytest
from members.pqminh2007.w1.translate import linear_search


def test_linear_search_found():
    arr = [10, 23, 45, 70, 11, 15]
    # Kiểm tra tìm thấy phần tử và trả về đúng index
    assert linear_search(arr, 70) == 3
    assert linear_search(arr, 10) == 0


def test_linear_search_not_found():
    arr = [1, 2, 3, 4, 5]
    # Không tìm thấy thì trả về -1 (hoặc tùy theo cách bạn implement hàm linear_search ở W1-4)
    assert linear_search(arr, 99) == -1


def test_linear_search_empty():
    arr = []
    assert linear_search(arr, 5) == -1