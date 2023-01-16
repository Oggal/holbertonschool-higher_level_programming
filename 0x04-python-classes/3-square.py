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
    @property
    def size(self):
        """int: Size of a Simple Square
        Value must be a positive integer."""
        return self.__size

    @property.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, _size=0):
        """Initialize a simple Square
        Args:
            _size (int): Size of the Square.
        """
        self.size = _size

    def area(self) -> int:
        """Get Area of a Square
        Returns:
            Area of Square
        """
        return self.__size ** 2
