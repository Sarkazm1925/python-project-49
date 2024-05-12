import prompt


GAME_LIMIT = 3
TEXT_DEFEAT = "is wrong answer ;(. Correct answer was"


def start_game(link):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(link.TEXT)
    count = 0
    while count < GAME_LIMIT:
        current_answer, text_question = link.get_task()
        print(f'Question: {text_question}')
        answer = input("Your answer: ")
        if current_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' {TEXT_DEFEAT} '{current_answer}'")
            print(f"Let's try again, {name}!")
            exit()
    print(f"Congratulations, {name}!")
