#!/usr/bin/python3
"""
    This module contains the 'print_square' function from task 2
"""


def print_square(size):
    """
    Function that prints a square of size 'size'

    Args:
        size: size of the square (width/height)

    Returns:
        Nothing

    Raises:
        TypeError:
            If size is not an integer
            if size is a float and is less than 0
        ValueError:
            If size is less than zero

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for _ in range(size):
            print("#", end="")
        print()
