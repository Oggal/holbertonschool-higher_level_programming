#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not dict:
        return None
    result = None
    top = None
    for k, v in a_dictionary.items():
        if (top is None or v > top):
            top = v
            result = k
    return k
