#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0 if sentence == None else len(sentence)
    character = None if length == 0 else sentence[0]
    return (length, character)
