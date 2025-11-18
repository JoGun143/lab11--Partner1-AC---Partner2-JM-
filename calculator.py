#https://github.com/JoGun143/lab11--Partner1-AC---Partner2-JM-
# Partner 1: <Ameerul Chowdhury>
# Partner 2: <Joseph Mauldin>
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b
def multiply(a, b):
    return a * b
def div(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def divide(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def log(a, b):
    if a <= 0:
        raise ValueError("Argument must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Invalid base.")
    return math.log(a, b)

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Argument must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Invalid base.")
    return math.log(a, b)


def exp(a, b):
    return a ** b
