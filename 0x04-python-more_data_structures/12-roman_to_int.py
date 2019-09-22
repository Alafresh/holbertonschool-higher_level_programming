#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string and str:
        return 0
    roma_number = {"I": 1,
                   "V": 5, "X": 10,
                   "L": 50,
                   "C": 100, "D": 500,
                   "M": 1000}
    val = len(roman_string)
    total = roma_number[roman_string[val - 1]]
    for x in range(val - 1, 0, -1):
        current = roma_number[roman_string[x]]
        prev = roma_number[roman_string[x - 1]]
        total += prev if prev >= current else -prev
    return total
