#!/usr/bin/python3
""" Module Containing find_peak function"""


def find_peak(list_of_integers):
    """Function that finds the peak in a list"""
    if len(list_of_integers) == 0:
        return None
    peak = float("-inf")
    for i in range(0, len(list_of_integers), 3):
        triplet = []
        triplet.append(list_of_integers[i])
        if i > 0:
            triplet.append(list_of_integers[i - 1])
        if i < len(list_of_integers) - 1:
            triplet.append(list_of_integers[i + 1])
        peak = max(triplet)

    return peak
