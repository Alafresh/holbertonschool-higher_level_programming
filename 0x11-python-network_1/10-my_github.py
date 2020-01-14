#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, post
    from sys import argv
    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    res = r.json()
    print(res['id'])
