#!/usr/bin/python3
def weight_average(my_list=[]):
    avarage = 0

    if my_list:
        weight_sum = 0
        multiplied = 0
        for tup in my_list:
            weight_sum += tup[1]
            multiplied += (tup[0] * tup[1])
        return multiplied / weight_sum

    return avarage
