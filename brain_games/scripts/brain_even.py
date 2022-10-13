#!/usr/bin/env python3

from brain_games.games.game_even import game_even
from brain_games.start import start_games

expression = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    start_games(game_even, expression)


if __name__ == '__main__':
    main()
