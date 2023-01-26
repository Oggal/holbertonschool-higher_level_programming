#!/usr/bin/python3
"""Project 0x07 Task 2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The Square Squared Square Squares"""
    def __init__(self, size):
        super().__init__(size, size)
