#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0 if sentence is None else len(sentence)
    character = None if length is 0 else sentence[0]
    return (length, character)
