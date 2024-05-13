from math import sqrt
from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def get_task():
    number = randint(START, END)
    current_answer = ('yes' if is_prime(number) else 'no')
    return current_answer, str(number)


def is_prime(number):
    if number < 2:
        return False
    count = 2
    while count <= int(sqrt(number)):
        if number % count == 0:
            return False
        count += 1
    return True
