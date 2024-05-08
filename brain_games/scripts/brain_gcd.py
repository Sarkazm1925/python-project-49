#!/usr/bin/env python3


from brain_games.games import start_game
from brain_games.games.brain_gcd import TEXT, generator


def main():
    start_game(TEXT, generator)


if __name__ == '__main__':
    main()
