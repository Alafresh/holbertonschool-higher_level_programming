#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (NameError, ValueError) as err:
        print("Exception: {}".format(err), file=stderr)
        return False
