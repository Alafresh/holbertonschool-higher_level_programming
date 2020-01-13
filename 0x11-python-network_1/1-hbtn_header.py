#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    url = argv[1]
    with request.urlopen(url) as response:
        id = response.info()
        print(id['X-Request-Id'])
