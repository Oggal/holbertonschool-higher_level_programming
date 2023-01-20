#!/usr/bin/python3
"""Task 2 - Say My Name"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))