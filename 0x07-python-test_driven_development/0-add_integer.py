#!/usr/bin/python3
def add_integer(a, b=98):
    total = 0
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    elif type(a) != int:
        raise TypeError('a must be an integer')
    elif type(b) != int:
        raise TypeError('b must be an integer')
    total = a + b
    return int(total)
