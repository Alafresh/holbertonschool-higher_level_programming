#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, options
    r = get('https://intranet.hbtn.io/status')
    print(r.headers.get('X-Request-Id'))
