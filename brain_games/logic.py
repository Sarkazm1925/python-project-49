from random import randint
from brain_games.const import SIGNS


def generator(text):
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 10)
    sign = SIGNS[randint(0, 2)]
    match text:
        case "even":
            return random_number1
        case "calc":
            return random_number1, random_number2, sign
        case _:
            return None


def is_valid_answer(text):
    return (text == "yes" or text == "no")


def even(number):
    current_answer = not bool(number % 2)
    return ("yes" if current_answer else "no")


def is_integer(answer):
    return answer.isdigit()


def calculate(number1, number2, sign):
    match sign:
        case "+":
            return (int(number1) + int(number2))
        case "-":
            return (int(number1) - int(number2))
        case _:
            return (int(number1) * int(number2))
