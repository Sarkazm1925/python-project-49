from math import sqrt
from random import randint
from .const import START, END


def generator():
    number = randint(START, END)
    current_answer = prime(number)
    return current_answer, str(number)


def prime(number):
    count = 2
    while count <= int(sqrt(number)):
        if number % count == 0:
            return "no"
        count += 1
    return "yes"
