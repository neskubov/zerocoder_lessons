import unittest
from main import *

class TestCalculateRemainder(unittest.TestCase):

    def test_calculate_remainder(self):
        self.assertEqual(calculate_remainder(10, 5), 0)
        self.assertEqual(calculate_remainder(10, 7), 3)
        self.assertEqual(calculate_remainder(10, 7), 3)
        self.assertEqual(calculate_remainder(10, 9), 1)

    def test_division_by_zero(self):
        self.assertRaises(ValueError, calculate_remainder, 10, 0)

if __name__ == "__main__":
    unittest.main()
