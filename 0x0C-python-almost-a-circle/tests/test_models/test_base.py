#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.base import Base


class TestFib(unittest.TestCase):

    def test_construct(self):
        self.obj = Base()
        self.assertEqual(self.obj.id,1)
        