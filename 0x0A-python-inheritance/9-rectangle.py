"""Module that contains a Class called Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class that represents a rectangle
    """
    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """str method to return a string representation of the object"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """method that returns the area of the object"""
        return self.__width * self.__height
