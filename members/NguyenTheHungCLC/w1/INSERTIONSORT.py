def insertion_sort(arr):
    """
    Thuật toán Sắp xếp chèn (Insertion Sort)
    Độ phức tạp thời gian: O(n^2)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Chèn phần tử arr[i] vào dãy đã sắp xếp arr[0..i-1]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Test thử hàm
if __name__ == "__main__":
    test_arr = [12, 11, 13, 5, 6]
    print("Mảng ban đầu:", test_arr)
    sorted_arr = insertion_sort(test_arr)
    print("Mảng sau khi sắp xếp:", sorted_arr)
