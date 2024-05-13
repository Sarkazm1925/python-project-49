from random import randint
from math import gcd


QUESTION = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def get_task():
    number1 = randint(START, END)
    number2 = randint(START, END)
    current_answer = str(gcd(number1, number2))
    return current_answer, f'{number1} {number2}'
