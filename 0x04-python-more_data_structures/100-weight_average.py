#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul = 0
    ad = 0
    for x, y in my_list:
        mul += x * y
        ad += y
    return mul / ad
