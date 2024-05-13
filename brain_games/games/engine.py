import prompt


GAME_LIMIT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    for i in range(GAME_LIMIT):
        answer, text_question = game.get_task()
        print(f'Question: {text_question}')
        user_answer = input('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
