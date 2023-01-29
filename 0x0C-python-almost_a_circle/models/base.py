#!/usr/bin/python3
""" Base Class"""


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
        self.id = Base.__nb_objects if id is None else id

    def check_int(cls, value):
        """check if an int value is valid, raise error if not """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        return value
