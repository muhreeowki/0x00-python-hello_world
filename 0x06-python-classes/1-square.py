#!/usr/bin/python3
""" Task 1 """


class Square:
    """This is a square class"""

    def __init__(self, size):
        """This is the square constructor"""
        try:
            self.__size = int(size)
        except Exception:
            self.__size = 0
