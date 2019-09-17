#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        count = 0
        for elem in row:
            if len(row) - 1 > count:
                print("{}".format(elem), end=' ')
            else:
                print("{}".format(elem), end='')
            count += 1
        print()
