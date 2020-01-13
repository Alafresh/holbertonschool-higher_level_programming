#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        data = html
    print('    - type: {}'.format(type(html)))
    print('    - content: {}'.format(html))
    print('    - utf8 content: {}'.format(data.decode('UTF-8')))
