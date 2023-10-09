#!/usr/bin/python3
"""Module that contains a Class called Sqaure"""


class MyInt(int):
    """
    Subclass that inherits int
    """
    def __eq__(self, value):
        """
        Checks if the int object is not equal to the value
        """
        return self != value

    def __ne__(self, value):
        """
        Checks if the int object is equal to the value
        """
        return self == value
