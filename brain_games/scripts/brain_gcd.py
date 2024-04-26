#!/usr/bin/env python3


from brain_games import welcome_user, generator, request, victory
from brain_games import is_integer, get_gcd, conclusion, GAME_LIMIT


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < GAME_LIMIT:
        number1, number2 = generator("gcd")
        answer = request(f'{number1} {number2}')
        current_answer = str(get_gcd(number1, number2))
        valid_answer = is_integer(answer)
        if conclusion(current_answer, answer, valid_answer, name):
            count += 1
    victory(name)
