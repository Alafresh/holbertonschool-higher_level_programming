#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    url = argv[1]
    value = {'Your email is': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        ida = response.read()
        print(ida)
