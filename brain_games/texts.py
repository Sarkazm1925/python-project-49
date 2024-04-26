import prompt
from brain_games.const import TEXT


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


def victory(name):
    print(f"Congratulations, {name}!")


def defeat(name, answer, current_answer):
    print(f"'{answer}' {TEXT} '{current_answer}'")
    print(f"Let's try again, {name}!")
    exit()


def task(text):
    print(f'Answer "yes" if the number is {text}, otherwise answer "no".')
