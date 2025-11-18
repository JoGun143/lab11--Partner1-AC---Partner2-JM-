# https://github.com/JoGun143/lab11--Partner1-AC---Partner2-JM-
# Partner 1: <Ameerul Chowdhury>
# Partner 2: <Joseph Mauldin>
import unittest
import calculator
############ Partner 2 ############
class TestPartner2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-5, 10), 5)
        self.assertEqual(calculator.add(0, 0), 0)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(-2, -8), 6)
    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(8, 2), 3)
        self.assertEqual(calculator.logarithm(100, 10), 2)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 1)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -2)
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)
############ Partner 1 ############
class TestPartner1(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertEqual(calculator.div(9, 3), 3)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)
    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
