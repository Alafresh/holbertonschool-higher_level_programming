def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()
