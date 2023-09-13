#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0

    if (my_list):
        uniq = set(my_list)
        for num in uniq:
            total += num

    return total
