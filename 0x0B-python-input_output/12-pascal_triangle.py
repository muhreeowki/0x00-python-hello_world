#!/usr/bin/python3
"""Module containing a Technical interview question"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []


    triangle = [[1]]

    for i in range(2, n + 1):
        prev_row = triangle[0]
        row = [0 for _ in range(len(prev_row) + 1)]
        row[0] = prev_row[0]
        for j in range(1, len(prev_row) + 1):
            if j == len(prev_row):
                row[j] = prev_row[-1]
            else:
                row[j] = prev_row[j - 1] + prev_row[j]
        triangle.insert(0, row)
    triangle.reverse()
    return triangle
