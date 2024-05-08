from random import randint
from math import gcd
from .const import START, END


def generator():
    number1 = randint(START, END)
    number2 = randint(START, END)
    current_answer = str(gcd(number1, number2))
    return current_answer, f"{number1} {number2}"
