def binary_search(a: list[int], key: int) -> int:
    """Return the index of key in a sorted list, or -1 if absent.
    
    Unlike C++, Python accepts a list object directly without needing
    a const reference such as const std::vector<int>&.
    """
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid
        elif a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
