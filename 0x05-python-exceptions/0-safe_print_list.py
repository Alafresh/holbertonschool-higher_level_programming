#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            a = my_list[i]
            print("{:d}".format(a), end="")
        except IndexError:
            pass
    print()
    return a
