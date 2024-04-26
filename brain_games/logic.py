from random import randint
from brain_games.const import SIGNS, CELLS


def generator(text, divider=1):
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100 // divider)
    random_number3 = randint(2, 7)
    sign = SIGNS[randint(0, 2)]
    match text:
        case "even":
            return random_number1
        case "calc":
            return random_number1, random_number2, sign
        case "gcd":
            return random_number1, random_number2
        case "progression":
            return fill(random_number1, random_number2, sign, random_number3)
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


def get_gcd(number1, number2):
    count = 2
    result = 1
    while count <= min(number1, number2):
        if number1 % count == 0 and number2 % count == 0:
            result *= count
            number1 = number1 // count
            number2 = number2 // count
        else:
            count += 1
    return result


def fill(number1, number2, sign, number3):
    count = 0
    basket = ""
    while count < CELLS:
        cell = calculate(number1, number2 * count, sign)
        if count == number3:
            current_answer = str(cell)
            basket += ".."
        else:
            basket += str(cell)
        if count < CELLS-1:
            basket += " "
        count += 1
    return basket, current_answer
