#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    a = 0
    try:
        a = fct(*args)
    except ZeroDivisionError:
        print("Exception: division by zero", file=stderr)
        return None
    except IndexError:
        print("Exception: list index out of range", file=stderr)
        return None
    return a
