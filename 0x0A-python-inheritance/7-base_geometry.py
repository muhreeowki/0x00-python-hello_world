#!/usr/bin/python3
"""Module that contains a Class called BaseGeometry"""


class BaseGeometry:
    """This is a class that represents geometric objects"""

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value

        Value is only valid if:
            1. it is an integer.
            2. it is greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
