from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def get_task():
    number = randint(START, END)
    current_answer = ('yes' if is_even(number) else 'no')
    return current_answer, str(number)


def is_even(number):
    return (number % 2 == 0)
