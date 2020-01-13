#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, options, post
    from sys import argv
    r = get(argv[1])
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 401:
        print('Error code: {}'.format(r.status_code))
    elif r.status_code == 404:
        print('Error code: {}'.format(r.status_code))
    elif r.status_code == 500:
        print('Error code: {}'.format(r.status_code))
