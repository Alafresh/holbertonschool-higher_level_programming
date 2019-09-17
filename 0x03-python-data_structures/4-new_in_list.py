#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    if idx < 0:
        return cp_list
    elif idx > len(my_list) - 1:
        return cp_list
    for i in range(len(my_list)):
        if (i is idx):
            cp_list[i] = element
    return cp_list
