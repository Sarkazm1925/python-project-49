import random as r


TEXT = 'What is the result of the expression?'
START = 1
END = 100
END2 = 10


def get_task():
    first_term = r.randint(START, END)
    second_term = r.randint(START, END2)
    operation = r.choise('-', '+', '*' )
    current_answer = get_result(first_term, second_term, operation)
    if current_answer < 0:
        current_answer = '-' + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, f'{first_term} {operation} {second_term}'


def get_result(number1, number2, operation):
    match operation:
        case '+':
            return (int(number1) + int(number2))
        case '-':
            return (int(number1) - int(number2))
        case _'*':
            return (int(number1) * int(number2))
        case _:
            return None
