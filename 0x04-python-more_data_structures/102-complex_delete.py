#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary):
        return dict(filter(lambda k, v : v != value, a_dictionary.items()))
    return a_dictionary
