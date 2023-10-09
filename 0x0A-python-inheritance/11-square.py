"""Module that contains a Class called Sqaure"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class that represents a square
    """
    def __init__(self, size):
        """Constructor method"""
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        """str method to return a string representation of the object"""
        return f"[Square] {self.__width}/{self.__height}"

    def area(self):
        """method that returns the area of the object"""
        return self.__width * self.__height
