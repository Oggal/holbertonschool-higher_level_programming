#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([0, 5]), 5)
        self.assertEqual(max_integer([0, 5, 9]), 9)
        self.assertEqual(max_integer([1.5, 5.5]), 5.5)
        self.assertEqual(max_integer(["dogz"]), 'z')
        
        with self.assertRaises(TypeError):
            max_integer("string?")
