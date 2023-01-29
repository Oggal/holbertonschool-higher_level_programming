#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.base import Base


class TestFib(unittest.TestCase):

    def test_construct(self):
        self.obj = Base()
        self.assertEqual(self.obj.id,1)
        
    def test_validator(self):
        self.assertRaises(TypeError, Base.check_int, "fail", "fail")
        self.assertRaises(TypeError, Base.check_int, 2.5, "failure")