import random


message = "is wrong answer ;(. Correct answer was"


def request():
    selected_number = random.randint(1, 100)
    print(f'Question: {selected_number}')
    answer = input("Your answer: ")
    return examination(selected_number, answer)


def examination(num, text):
    even_number = not bool(num % 2)
    if even_number == (True if text == "yes" else False) and valid_answer(text):
        print("Correct!")
        return True
    print(f'"{text}" {message} "{("yes" if even_number else "no")}".')
    return False


def valid_answer(text):
    return (text == "yes" or text == "no")


def victory():
    count = 0
    while count < 3:
        if request():
            count += 1
        else:
            return False
    return True
