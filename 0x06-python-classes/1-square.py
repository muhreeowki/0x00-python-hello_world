#!/usr/bin/python3
""" Task 1 """


class Square:
    """This is a square class"""

    def __init__(self, new_size):
        """This is the square constructor"""
        try:
            self.__size = int(new_size)
        except Exception:
            self.__size = 0
