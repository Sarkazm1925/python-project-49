import prompt


def welcome_user1():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return None
