#!/usr/bin/env python3


from brain_games import welcome_user, generator, request, victory
from brain_games import prime, is_valid_answer, conclusion, GAME_LIMIT


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < GAME_LIMIT:
        question = generator("even")
        answer = request(question)
        current_answer = prime(question)
        valid_answer = is_valid_answer(answer)
        if conclusion(answer, current_answer, valid_answer, name):
            count += 1
    victory(name)
    exit()
