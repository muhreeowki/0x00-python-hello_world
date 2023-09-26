#!/usr/bin/python3
""" Task 3 """


class Square:
    """This is a square class"""

    def __init__(self, size=0):
        """
        This is the square constructor
        it checks to see if the user size is valid...
        if not it raises a TypeError
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise TypeError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Function to return the area of the square"""
        return self.__size * self.__size
