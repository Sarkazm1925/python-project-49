from random import randint
from .const import START, END


def generator():
    number = randint(START, END)
    current_answer = ("no" if (number % 2) else "yes")
    return current_answer, str(number)


def tut():
    return "aga"
