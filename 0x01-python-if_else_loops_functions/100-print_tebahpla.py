#!/usr/bin/python3
odd = ""
for i in range(122, 96, -1):
    if i % 2 == 1:
        odd = chr(i - 32)
    else:
        odd = chr(i)
    print(odd, end="")
