#!/usr/bin/python3
def matrix_divided(matrix, div):
    if matrix is None or type(matrix[0]) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    elif div is 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is int:
        pass
    elif type(div) is float:
        pass
    else:
        raise TypeError('div must be a number')
    new_matrix = [x [:] for x in matrix]
    size = len(new_matrix[0])
    for row in new_matrix:
        count = 0
        if size != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for colum in row:
            if type(colum) is int or type(colum) is float:
                pass
            else:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            row[count] /= div
            row[count] = round(row[count], 2)
            count += 1
    return new_matrix
