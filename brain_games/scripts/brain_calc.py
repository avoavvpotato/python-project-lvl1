#!/usr/bin/env python3

from brain_games.games.game_calc import game_calc
from brain_games.start import start_games

expression = 'What is the result of the expression?'


def main():
    start_games(game_calc, expression)


if __name__ == '__main__':
    main()
