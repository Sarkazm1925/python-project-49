import prompt
from random import randint
from .const import GAME_LIMIT, TEXT, START, END


def even_start():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < GAME_LIMIT:
        question = randint(START, END)
        answer = request(question)
        current_answer = ("no" if (question % 2) else "yes")
        valid_answer = (answer == "yes" or answer == "no")
        if conclusion(answer, current_answer, valid_answer, name):
            count += 1
    print(f"Congratulations, {name}!")
    exit()


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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
