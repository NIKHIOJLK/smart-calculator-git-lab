import unittest

from calculator import add, calculate, divide, multiply, subtract


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_rounds(self):
        self.assertEqual(divide(10, 3), 3.33)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)

    def test_calculate(self):
        self.assertEqual(calculate("2 + 3"), 5)


if __name__ == "__main__":
    unittest.main()
