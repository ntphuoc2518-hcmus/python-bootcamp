"""Module translating C++ vector functions to Pythonic implementations."""


def transpose(matrix):
    """
    Transpose a 2D matrix (list of lists).

    Difference from C++:
    In C++, transposing requires nested loops and manual indexing with
    vector<vector<T>>. In Python, 'zip(*matrix)' unpacks rows and pairs 
    corresponding elements into columns in a single Pythonic line.
    """
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]