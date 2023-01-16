#!/usr/bin/python3
"""Simple Square Project

This Module contains a class representing a simple Square.
"""


class Square:
    """Class representing a simple square"""
    @property
    def size(self):
        """int: Size of a Simple Square
        Value must be a positive integer.
        """
        return self.__size

    @property.setter
    def size(self, value):
        """int: Size of Simple Square
        Value must be an int >=0 
        """
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

    def area(self):
        """Get Area of a Square
        Returns:
            int: Area of Square
        """
        return self.__size ** 2
