#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = a_dictionary
    return [print("{}: {}".format(i, dic[i])) for i in sorted(dic)]
