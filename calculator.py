#https://github.com/JoGun143/lab11--Partner1-AC---Partner2-JM-
# Partner 1: <Ameerul Chowdhury>
# Partner 2: <Joseph Mauldin>
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Invalid base for logarithm.")
    return math.log(a, b)

def exponent(a, b):
    return a ** b