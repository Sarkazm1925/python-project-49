from random import randint
from .const import SIGNS, START, END, END2
from .const import END_OF_BASKET, SIGN_START, SIGN_END, CELLS


def generator():
    basket, current_answer = create()
    if current_answer < 0:
        current_answer = "-" + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, basket


def create():
    random_number1 = randint(START, END)
    random_number2 = randint(START, END2)
    random_number3 = randint(START, END_OF_BASKET)
    sign = SIGNS[randint(SIGN_START, SIGN_END)]
    return fill(random_number1, random_number2, sign, random_number3)


def fill(number1, number2, sign, number3):
    count = 0
    temp = []
    while count < CELLS:
        cell = calculate(number1, number2 * count, sign)
        if count == number3:
            current_answer = cell
            temp.append("..")
        else:
            temp.append(str(cell))
        count += 1
    basket = ' '.join(temp)
    return basket, current_answer


def calculate(number1, number2, sign):
    if sign == "+":
        return (int(number1) + int(number2))
    return (int(number1) - int(number2))
