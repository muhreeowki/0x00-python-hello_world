#!/usr/bin/python3
"""Module containing a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an informal string representation of a rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        self.validate("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attirbutes of an exsisting instance"""
        length = len(args)
        if args and length > 0:
            sqr_args = ["id", "size", "x", "y"]
            for i in range(length):
                if i < 4:
                    setattr(self, sqr_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary represntation of all the attributes of a rectangle
        """
        convert = {
                "_Rectangle__width": "size",
                "_Rectangle__height": "size",
                "_Rectangle__x": "x",
                "_Rectangle__y": "y",
                "id": "id"
            }
        return {convert[key]: value for key, value in self.__dict__.items()}
