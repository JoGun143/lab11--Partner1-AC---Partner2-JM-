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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()