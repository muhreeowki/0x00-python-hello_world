#!/usr/bin/python3
"""Module containing write_file funtion"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file
    and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
