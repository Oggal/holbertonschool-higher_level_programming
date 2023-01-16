#!/usr/bin/python3
"""Simple Square Project

This Module contains a class representing a simple Square.

Example:
    >>>square = __import__('1-square').Square
    >>>new_square = square(2)

"""


class Square:
    """Class representing a simple square
    """
    def __init__(self, _size=0):
        """Initialize a simple Square
        Args:
            _size (int): Size of the Square.
        """
        if (_size is not int):
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self.__size = _size
