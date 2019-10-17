#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as myFile:
        count = 0
        for line in myFile:
            count += 1
    return count
