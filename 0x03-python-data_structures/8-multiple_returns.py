#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None, None
    length = 0
    for i in sentence:
        length += 1
    return length, sentence[0]
