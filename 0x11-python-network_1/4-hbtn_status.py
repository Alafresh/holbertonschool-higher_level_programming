#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get
    r = get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
