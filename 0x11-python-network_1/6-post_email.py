#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, options, post
    from sys import argv
    r = post(argv[1], data={'email': argv[2]})
    print(r.text)
