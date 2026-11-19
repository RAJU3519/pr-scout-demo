import unittest

from calculator import calculate_total, calculate_discount


class CalculatorTests(unittest.TestCase):

    def test_calculate_total(self):
        self.assertEqual(calculate_total(100, 5), 500)

    def test_calculate_total_with_zero_quantity(self):
        self.assertEqual(calculate_total(100, 0), 0)

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(500, 50), 450)

    def test_calculate_discount_with_zero_discount(self):
        self.assertEqual(calculate_discount(500, 0), 500)


if __name__ == "__main__":
    unittest.main()
