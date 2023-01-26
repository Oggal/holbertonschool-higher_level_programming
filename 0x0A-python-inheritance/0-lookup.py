#!/usr/bin/python3
"""Module to list object atributes"""


def lookup(obj):
    '''List the object attributes'''
    startlist = list(obj.__dict__.keys())
    startlist.extend(x for x in dir(obj) if x not in startlist)
    startlist.sort()
    return startlist
