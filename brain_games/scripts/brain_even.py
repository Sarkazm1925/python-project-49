#!/usr/bin/env python3


from brain_games import welcome_user, victory


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if victory():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
    exit()


if __name__ == '__main__':
    main()
