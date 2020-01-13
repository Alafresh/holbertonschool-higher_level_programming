#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, head, options, post
    from sys import argv
    try:
        r = post('http://0.0.0.0:5000/search_user', data={'q': argv[1]})
        res = r.json()
        print('[{}] {}'.format(res['id'], res['name']))
    except KeyError:
        print('No result')
    except Exception:
        print('Not a valid JSON')
