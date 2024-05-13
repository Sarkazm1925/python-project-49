from random import randint


QUESTION = 'What number is missing in the progression?'
CELLS = 10
START_CELL = 1
START_STEP = -10
END_CELL = 100
END_STEP = 10
START_BASKET = 1
END_BASKET = 8


def get_task():
    basket, current_answer = create()
    if current_answer < 0:
        current_answer = '-' + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, basket


def create():
    first_cell = randint(START_CELL, END_CELL)
    step = randint(START_STEP, END_STEP)
    hidden_cell = randint(START_BASKET, END_BASKET)
    return fill(first_cell, step, hidden_cell)


def fill(start, step, hidden_cell):
    temp = []
    for i in range(CELLS):
        cell = start + step * i
        if i == hidden_cell:
            current_answer = cell
            temp.append("..")
        else:
            temp.append(str(cell))
    basket = ' '.join(temp)
    return basket, current_answer
