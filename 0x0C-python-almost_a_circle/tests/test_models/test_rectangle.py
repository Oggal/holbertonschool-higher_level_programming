#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.rectangle import Rectangle


class TestFib(unittest.TestCase):

    def test_construct(self):
        self.obj = Rectangle(1,1, id=2)
        self.assertEqual(self.obj.height,1)
        self.assertEqual(self.obj.width,1)
        self.assertEqual(self.obj.id, 2)

    def test_strings(self):
        self.obj = Rectangle(1,2,3,4,3)
        self.assertEqual(str(self.obj), "[Rectangle] (3) 3/4 - 1/2")