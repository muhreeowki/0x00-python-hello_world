#!/usr/bin/python3
"""
    This module contains the 'text_indentation' function from task 2
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: String of text

    Returns:
        Nothing

    Raises:
        TypeError:
            If text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0

    for char in text:
        if flag == 1 and char == ' ':
            flag = 0
            continue

        print(char, end="")

        if char in [':', '?', '.']:
            flag = 1
            print('\n')
