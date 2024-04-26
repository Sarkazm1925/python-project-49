#!/usr/bin/env python3


from brain_games import welcome_user, generator, request, victory, task
from brain_games import even, is_valid_answer, conclusion, GAME_LIMIT


def main():
    name = welcome_user()
    task("even ,o")
    count = 0
    while count < GAME_LIMIT:
        question = generator("even")
        answer = request(question)
        current_answer = even(question)
        valid_answer = is_valid_answer(answer)
        if conclusion(answer, current_answer, valid_answer, name):
            count += 1
    victory(name)
    exit()


if __name__ == '__main__':
    main()
