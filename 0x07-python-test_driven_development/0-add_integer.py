#!/usr/bin/python3
"""Task 0 - Project 0x05:: Add Integer"""


def add_integer(a: int, b: int=98)->int:
    """Adds two ints together"""
    a = a if isinstance(a, int) else int(a) if isinstance(a, float) else None
    b = b if isinstance(b, int) else int(b) if isinstance(b, float) else None
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    return a+b
