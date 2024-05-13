from random import randint, choice


QUESTION = 'What is the result of the expression?'
FIRST_START = 1
FIRST_END = 100
SECOND_START = 1
SECOND_END = 10


def get_task():
    first_term = randint(FIRST_START, FIRST_END)
    second_term = randint(SECOND_START, SECOND_END)
    operation = choice('-+*')
    current_answer = get_answer(first_term, second_term, operation)
    if current_answer < 0:
        current_answer = '-' + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, f'{first_term} {operation} {second_term}'


def get_answer(number1, number2, operation):
    match operation:
        case '+':
            return (int(number1) + int(number2))
        case '-':
            return (int(number1) - int(number2))
        case '*':
            return (int(number1) * int(number2))
        case _:
            return None
