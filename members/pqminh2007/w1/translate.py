"""Module thực hiện chuyển vị ma trận (Matrix Transpose)."""

def transpose(matrix):
    """Chuyển vị ma trận 2D."""
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed