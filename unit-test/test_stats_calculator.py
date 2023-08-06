import unittest
import numpy as np
from stats_calculator import calculate_statistics

class TestStatisticsCalculations(unittest.TestCase):
    def test_mean(self):
        mean, _, _ = calculate_statistics([1, 2, 3, 4, 5])
        self.assertAlmostEqual(mean, 3.0)

    def test_median_odd(self):
        _, median, _ = calculate_statistics([1, 2, 3, 4, 5])
        self.assertAlmostEqual(median, 3)

    def test_median_even(self):
        _, median, _ = calculate_statistics([1, 2, 3, 4, 5, 6])
        self.assertAlmostEqual(median, 3.5)

    def test_std_deviation(self):
        _, _, std_deviation = calculate_statistics([1, 2, 3, 4, 5])
        self.assertTrue(abs(std_deviation - 1.581139) < 0.2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element(self):
        mean, median, std_deviation = calculate_statistics([7])
        self.assertEqual(mean, 7)
        self.assertEqual(median, 7)
        self.assertEqual(std_deviation, 0)

if __name__ == '__main__':
    unittest.main()
