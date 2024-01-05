#!/usr/bin/python3
""" Module Containing find_peak function"""


def find_peak(list_of_integers):
    """Function that finds the peak in a list"""
    j = len(list_of_integers) - 1
    if j < 0:
        return None
    peak = float("-inf")
    for i in range(j):
        if i > j:
            break
        peak = list_of_integers[j] if peak < list_of_integers[j] else peak
        peak = list_of_integers[i] if peak < list_of_integers[i] else peak
        j -= 1
    return peak
