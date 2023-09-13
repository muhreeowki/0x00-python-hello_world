#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    if matrix:
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                row.append(matrix[i][j] * matrix[i][j])
            new_matrix.append(row)
    return new_matrix
