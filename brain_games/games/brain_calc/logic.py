import prompt
from random import randint
from .const import GAME_LIMIT, START, END, END2, SIGNS
from .const import SIGN_START, SIGN_END, TEXT


def calc_start():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count < GAME_LIMIT:
        number1, number2, sign = generator()
        current_answer = calculate(number1, number2, sign)
        answer = request(f'{number1} {sign} {number2}')
        valid_answer = is_integer(answer, current_answer)
        if current_answer < 0:
            current_answer = "-" + str(abs(current_answer))
        else:
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
    sign = SIGNS[randint(SIGN_START, SIGN_END)]
    return random_number1, random_number2, sign


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
