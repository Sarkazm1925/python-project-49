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
        answer = request(f'{basket}')
        valid_answer = is_integer(answer)
        if conclusion(current_answer, answer, valid_answer, name):
            count += 1
    victory(name)
