"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/JoGun143/lab11--Partner1-AC---Partner2-JM-
# Partner 1: <Ameerul Chowdhury>
# Partner 2: <Joseph Mauldin>

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(a, b)

def exp(a, b):
    return a ** b

