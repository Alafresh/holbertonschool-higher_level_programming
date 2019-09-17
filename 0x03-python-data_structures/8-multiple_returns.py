#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    length = 0
    for i in sentence:
        length += 1
    return length, sentence[0]
