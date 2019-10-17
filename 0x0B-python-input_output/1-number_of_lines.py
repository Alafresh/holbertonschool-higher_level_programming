#!/usr/bin/pyhton3
def number_of_lines(filename=""):
    with open(filename) as myFile:
        number = myFile.readlines()
    return len(number)
