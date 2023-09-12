#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        highest = my_list[0];
        for num in my_list:
            highest = num if num > highest else highest
        return highest
    return None
