from random import randint
from .const import START, END, END2, SIGNS
from .const import SIGN_START, SIGN_END


def generator():
    number1 = randint(START, END)
    number2 = randint(START, END2)
    sign = SIGNS[randint(SIGN_START, SIGN_END)]
    current_answer = calculate(number1, number2, sign)
    if current_answer < 0:
        current_answer = "-" + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, f'{number1} {sign} {number2}'


def calculate(number1, number2, sign):
    match sign:
        case "+":
            return (int(number1) + int(number2))
        case "-":
            return (int(number1) - int(number2))
        case _:
            return (int(number1) * int(number2))
