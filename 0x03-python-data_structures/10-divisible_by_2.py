#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    count = 0
    for i in new_list:
        if i % 2 is 0:
            new_list[count] = True
        else:
            new_list[count] = False
        count += 1
    return new_list
