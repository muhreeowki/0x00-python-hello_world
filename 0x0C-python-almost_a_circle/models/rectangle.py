#!/usr/bin/python3
"""Module containing a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This is a class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns an informal string representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        """Setter method for width attribute"""
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute"""
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value):
        """
        This function checks weather a specified value: 'value' is valid
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))

        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle to stdout using '#'"""
        for space in range(self.__y):
            print()
        for col in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the attirbutes of an exsisting instance"""
        length = len(args)
        if args and length > 0:
            rect_args = ["id", "width", "height", "x", "y"]
            for i in range(length):
                if i < 5:
                    setattr(self, rect_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary represntation of all the attributes of a rectangle
        """
        convert = {
                "_Rectangle__width": "width",
                "_Rectangle__height": "height",
                "_Rectangle__x": "x",
                "_Rectangle__y": "y",
                "id": "id"
            }
        return {convert[key]: value for key, value in self.__dict__.items()}
