#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print('0 arguments.')
else:
    print('{} arguments'.format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv), 1):
            print('{}: {}'.format(i, sys.argv[i]))