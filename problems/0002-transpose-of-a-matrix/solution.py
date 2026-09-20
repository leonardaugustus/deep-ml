def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    new = []
    for row in zip(*a):
        new.append(list(row))
    
    for i,row in enumerate(a):
        for j,value in enumerate(row):
            new[j][i] = value
    return new


a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
