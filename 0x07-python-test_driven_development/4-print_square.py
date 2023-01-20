#!/usr/bin/python3
"""4-print_squre - Print a square"""


def print_square(size):
    """print_square - print a square with size number of # per side"""
    if not isinstance(size, (int)):
        if isinstance(size, float) and size > 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("{}".format('#' * size))
