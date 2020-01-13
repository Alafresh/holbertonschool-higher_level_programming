#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, options
    from sys import argv
    r = get(argv[1])
    print(r.headers.get('X-Request-Id'))
