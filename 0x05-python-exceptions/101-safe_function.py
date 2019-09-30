#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        fct(*args)
    except ZeroDivisionError:
        print("Exception: division by zero", file=stderr)
        return None
    except IndexError:
        print("Exception: list index out of range", file=stderr)
        return None
    return fct(*args)
