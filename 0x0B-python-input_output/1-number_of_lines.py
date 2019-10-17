#!/usr/bin/pyhton3
def number_of_lines(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        number = myFile.readlines()
    return len(number)
