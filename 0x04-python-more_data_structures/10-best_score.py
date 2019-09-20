#!/usr/bin/python3
def best_score(a_dictionary):
    bigger = 0
    bigger_str = ""
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > bigger:
            bigger = a_dictionary[i]
            bigger_str = i
    return bigger_str
