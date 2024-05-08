import prompt
from .const import TEXT, GAME_LIMIT


def start_game(text, func):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(text)
    count = 0
    while count < GAME_LIMIT:
        current_answer, text_question = func()
        print(f'Question: {text_question}')
        answer = input("Your answer: ")
        if current_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' {TEXT} '{current_answer}'")
            print(f"Let's try again, {name}!")
            exit()
    print(f"Congratulations, {name}!")
    exit()
