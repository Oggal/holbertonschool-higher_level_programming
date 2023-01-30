#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_construct(self):
        self.obj = Square(1, id=3)
        self.assertEqual(self.obj.height, 1)
        self.assertEqual(self.obj.width, 1)
        self.assertEquar(self.obj.size, 1)
        self.assertEqual(self.obj.id, 2)