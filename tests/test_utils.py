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

    def test_greet(self):
        self.assertEqual(utils.greet("Bob"), "Hello, Bob!")
        self.assertEqual(utils.greet(""), "Hello, !")  # Might be an edge case

if __name__ == '__main__':
    unittest.main()
