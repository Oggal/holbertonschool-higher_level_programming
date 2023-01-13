#!/usr/bin/python3


def multiple_returns(sent):
    if (len(sent) > 0):
        let = sent[0]
    else:
        let = None
    return tuple((len(sent), let))
