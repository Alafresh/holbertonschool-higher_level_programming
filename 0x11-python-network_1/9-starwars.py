#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, post
    from sys import argv
    r = get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    res = r.json()
    print('Number of results: {}'.format(res['count']))
    for i in res['results']:
        print(i['name'])
