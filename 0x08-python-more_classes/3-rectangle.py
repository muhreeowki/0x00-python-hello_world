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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += "#"
                if h < self.__height - 1:
                    string += "\n"
        return string

    @property
    def width(self):
        """Getter method for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width instance attribute"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
