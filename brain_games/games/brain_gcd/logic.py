import prompt
from random import randint
from math import gcd
from .const import GAME_LIMIT, START, END, TEXT


def gcd_start():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < GAME_LIMIT:
        number1, number2 = generator()
        answer = request(f'{number1} {number2}')
        current_answer = str(gcd(number1, number2))
        valid_answer = answer.isdigit()
        if conclusion(answer, current_answer, valid_answer, name):
            count += 1
    print(f"Congratulations, {name}!")
    exit()


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def generator():
    random_number1 = randint(START, END)
    random_number2 = randint(START, END)
    return random_number1, random_number2


def request(question):
    print(f'Question: {question}')
    answer = input("Your answer: ")
    return answer


def conclusion(answer, current_answer, valid_answer, name):
    if current_answer == answer and valid_answer:
        print("Correct!")
        return True
    defeat(name, answer, current_answer)


def defeat(name, answer, current_answer):
    print(f"'{answer}' {TEXT} '{current_answer}'")
    print(f"Let's try again, {name}!")
    exit()
