#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -4, 10, 0]), 10)

    def test_all_equal(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.6, 0.3]), 2.6)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "d"]), "z")

    def test_string_list(self):
        self.assertEqual(max_integer("azerty"), "z")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_list_with_bool(self):
        self.assertEqual(max_integer([True, False, 3]), 3)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()