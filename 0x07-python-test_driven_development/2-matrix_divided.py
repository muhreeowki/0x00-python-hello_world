#!/usr/bin/python3
"""
    This module contains the 'matrix_divided' function from task 1
"""


def matrix_divided(matrix, div):
    """
    Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number to divide by

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero

    """

    if len(matrix) == 0 or matrix is None:
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    length = len(matrix[0])

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
