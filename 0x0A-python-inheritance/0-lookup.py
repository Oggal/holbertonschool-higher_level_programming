#!/usr/bin/python3
"""Module to list object atributes"""


def lookup(obj):
    '''List the object attributes'''
    return list(obj.__dict__.keys())