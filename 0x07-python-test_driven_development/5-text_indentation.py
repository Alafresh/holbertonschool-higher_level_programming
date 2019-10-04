#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    count = 0
    for i in text:
        if text[count] is '.':
            print('{}\n'.format(text[count]))
        elif text[count] is '?':
            print('{}\n'.format(text[count]))
        elif text[count] is ':':
            print('{}\n'.format(text[count]))
        elif text[count] is ' ' and text[count - 1] is '.':
            pass
        elif text[count] is ' ' and text[count - 1] is ':':
            pass
        elif text[count] is ' ' and text[count - 1] is '?':
            pass
        else:
            print(text[count], end='')
        count += 1
