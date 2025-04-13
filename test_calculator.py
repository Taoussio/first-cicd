import unittest
from calculator import addition, soustraction, multiplication, division

class TestCalculatrice(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 4), 6)
        self.assertEqual(soustraction(0, 5), -5)
        self.assertEqual(soustraction(-3, -2), -1)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 7), 21)
        self.assertEqual(multiplication(-2, 4), -8)
        self.assertEqual(multiplication(0, 100), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-9, 3), -3)
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
