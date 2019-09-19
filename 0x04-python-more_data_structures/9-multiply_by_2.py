#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    return {i: new_dictionary[i] * 2 for i in new_dictionary}
