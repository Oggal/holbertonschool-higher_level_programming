#!/usr/bin/python3


def best_score(a_dictionary):
    result = None
    top = None
    for k, v in a_dictionary:
        if (top is None or v > top):
            top = v
            result = k
    return k
