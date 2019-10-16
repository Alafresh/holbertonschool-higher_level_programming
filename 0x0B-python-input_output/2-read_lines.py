#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        count = 0
        if nb_lines <= 0:
            print(myFile.read(), end='')
        for line in myFile:
            if nb_lines == count:
                break
            print(line, end='')
            count += 1
