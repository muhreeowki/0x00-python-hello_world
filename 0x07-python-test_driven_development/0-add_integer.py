#!/usr/bin/python3
"""
    This module contains the 'add_integer' function from task 0
"""
def add_integer(a, b=98):
    """
        Funtion to add two numbers together

        Args:
            a: a number to add
            b: a number to add

        Returns:
            The sum of a and b

        Raises:
            TypeError: if a or b are not integers/floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
