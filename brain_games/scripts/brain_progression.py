#!/usr/bin/env python3


from brain_games import welcome_user, generator, request, victory
from brain_games import is_integer, conclusion, GAME_LIMIT


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    while count < GAME_LIMIT:
        divider = 20
        basket, current_answer = generator("progression", divider)
        while current_answer < 0:
            basket, current_answer = generator("progression", divider)
        current_answer = str(current_answer)
        answer = request(f'{basket}')
        valid_answer = is_integer(answer)
        if conclusion(answer, current_answer, valid_answer, name):
            count += 1
    victory(name)
