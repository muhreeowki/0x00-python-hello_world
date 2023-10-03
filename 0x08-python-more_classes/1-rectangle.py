#!/usr/bin/python3
"""
This a module containing a class that defines a rectangle
"""


class Rectangle():
    """
    This is a class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """This is a constructor method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
