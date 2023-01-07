#!/usr/bin/python3
def multiple_returns(sentence):
    new_tup = ()
    if len(sentence) == 0:
        return None
    else:
        new_tup = len(sentence), sentence[0]
        return new_tup
