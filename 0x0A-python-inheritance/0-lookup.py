#!/usr/bin/python3
"""Module to list object atributes"""


def loopup(obj):
    '''List the object attributes'''
    return [k for k,v in obj.__dict__]