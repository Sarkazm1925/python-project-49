from random import randint

TEXT = "What number is missing in the progression?"
CELLS = 10
START = 1
START2 = -10
END = 100
END2 = 10
END_OF_BASKET = 8


def get_task():
    basket, current_answer = create()
    if current_answer < 0:
        current_answer = "-" + str(abs(current_answer))
    current_answer = str(current_answer)
    return current_answer, basket


def create():
    first_cell = randint(START, END)
    step = randint(START2, END2)
    hidden_cell = randint(START, END_OF_BASKET)
    return fill(first_cell, step, hidden_cell)


def fill(start, step, hidden_sell):
    count = 0
    temp = []
    while count < CELLS:
        cell = start + step * count
        if count == hidden_cell:
            current_answer = cell
            temp.append("..")
        else:
            temp.append(str(cell))
        count += 1
    basket = ' '.join(temp)
    return basket, current_answer
