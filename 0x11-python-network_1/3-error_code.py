#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request, parse, error
    from sys import argv
    try:
        url = argv[1]
        with request.urlopen(url) as response:
            ida = response.code
            print(ida)
    except error.HTTPError as e:
        if e.code == 401:
            print('Error code: {}'.format(e.code))
        elif e.code == 404:
            print('Error code: {}'.format(e.code))
        elif e.code == 500:
            print('Error code: {}'.format(e.code))
