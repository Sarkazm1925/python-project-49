#!/usr/bin/env python3


from brain_games import welcome_user, generator, request, victory
from brain_games import is_integer, calculate, conclusion, GAME_LIMIT


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count < GAME_LIMIT:
        number1, number2, sign = generator("calc")
        answer = request(f'{number1} {sign} {number2}')
        current_answer = str(calculate(number1, number2, sign))
        valid_answer = is_integer(answer)
        if conclusion(current_answer, answer, valid_answer, name):
            count += 1
    victory(name)
    exit()