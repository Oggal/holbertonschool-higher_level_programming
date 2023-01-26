#!/usr/bin/python3
"""Project 0x07 Task 1"""


class MyList(list):
    """It's a list, and some"""
    def print_sorted(self):
        _t = self[:]
        _t.sort()
        print(_t)
