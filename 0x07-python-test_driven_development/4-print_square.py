#!/usr/bin/python3


def print_square(size):
    if not isinstance(size, (int)):
        if isinstance(size, float) and size > 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
       print("{}".format('#' * size))