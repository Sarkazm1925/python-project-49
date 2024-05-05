import prompt
from random import randint
from .const import GAME_LIMIT, TEXT, SIGNS, START, END, END2
from .const import END_OF_BASKET, SIGN_START, SIGN_END, CELLS


def progression_start():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    while count < GAME_LIMIT:
        basket, current_answer = generator()
        answer = request(f'{basket}')
        valid_answer = is_integer(answer, current_answer)
        if current_answer < 0:
            current_answer = "-" + str(abs(current_answer))
        current_answer = str(current_answer)
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
    match sign:
        case "+":
            return (int(number1) + int(number2))
        case "-":
            return (int(number1) - int(number2))
        case _:
            return (int(number1) * int(number2))


def request(question):
    print(f'Question: {question}')
    answer = input("Your answer: ")
    return answer


def is_integer(answer, current_answer):
    if current_answer < 0:
        return (answer[:1] == "-" and answer[1:].isdigit())
    return answer.isdigit()


def conclusion(answer, current_answer, valid_answer, name):
    if current_answer == answer and valid_answer:
        print("Correct!")
        return True
    defeat(name, answer, current_answer)


def defeat(name, answer, current_answer):
    print(f"'{answer}' {TEXT} '{current_answer}'")
    print(f"Let's try again, {name}!")
    exit()
