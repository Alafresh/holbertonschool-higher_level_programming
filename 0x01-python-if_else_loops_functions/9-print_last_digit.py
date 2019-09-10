#!/usr/bin/python3
def print_last_digit(number):
    r = ""
    if number == 0:
        r += str(0)
    elif number < 0:
        r += str(abs(number) % 10)
    else:
        r += str(number % 10)
    print(r, end="")
    return r
