#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[y * y for y in row] for row in matrix]
# return list(map(lambda x: x * x, row))
