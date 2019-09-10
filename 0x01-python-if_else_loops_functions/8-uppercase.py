#!/usr/bin/python3
def uppercase(str):
    re = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            re += chr(ord(str[i]) - 32)
        else:
            re += str[i]
    print("{}".format(re))
