"""Module that contains a Class called Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass of BaseGeometry that represents a rectangle
    """
    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height
