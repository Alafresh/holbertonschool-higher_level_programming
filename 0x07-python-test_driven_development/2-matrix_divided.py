#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = [x [:] for x in matrix]

    for row in new_matrix:
        count = 0
        for colum in row:
            row[count] /= div
            row[count] = round(row[count], 2)
            count += 1
    return new_matrix
