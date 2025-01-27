"""
test_utils.py
Basic test cases for utils.py functions.
"""

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(utils.add_numbers(2, 3), 5)
        self.assertEqual(utils.add_numbers(-1, 1), 0)
        self.assertEqual(utils.add_numbers(2.5, 2.5), 5.0)

    def test_add_numbers_list(self):
        # Test summing a list of integers
        self.assertEqual(utils.add_numbers([1, 2, 3]), 6)

        # Test summing a list of floats
        self.assertEqual(utils.add_numbers([0.5, 1.5, 2.0]), 4.0)

        # You could also test an empty list if desired
        self.assertEqual(utils.add_numbers([]), 0, "Sum of an empty list should be 0")

    def test_greet(self):
        # Normal name
        self.assertEqual(utils.greet("Bob"), "Hello, Bob!", "Should greet Bob by name")

        # Empty string
        self.assertEqual(utils.greet(""), "Hello, there!", "Should greet properly when name is empty")

        # None
        self.assertEqual(utils.greet(None), "Hello, there!", "Should greet properly when name is None")

if __name__ == '__main__':
    unittest.main()
