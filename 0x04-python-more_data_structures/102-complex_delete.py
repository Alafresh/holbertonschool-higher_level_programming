#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return None
    for i in list(a_dictionary):
        if a_dictionary[i] is value:
            a_dictionary.pop(i)
    return a_dictionary
