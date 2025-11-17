import unittest
import calculator
import pytest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
        """"""# https://github.com/JoGun143/lab11--Partner1-AC---Partner2-JM-
    # Partner 1: <Ameerul Chowdhury>
    # Partner 2: <Joseph Mauldin>

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(0, 5) == -5
    assert calculator.sub(-3, -2) == -1
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertAlmostEqual(calculator.divide(7, 3), 7 / 3)
    # ##########################

    ######## Partner 2
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.div(5, 0)
def test_logarithm():
    assert calculator.log(8, 2) == 3
    assert calculator.log(100, 10) == 2
def test_log_invalid_base():
    with pytest.raises(ValueError):
        calculator.log(-1, 10)
    with pytest.raises(ValueError):
        calculator.log(10, 1)
    with pytest.raises(ValueError):
        calculator.log(10, -2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(10, 1)

        with self.assertRaises(ValueError):
            calculator.logarithm(10, -2)

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