#!/usr/bin/env python3

from brain_games.games.game_progression import game_progression
from brain_games.start import start_games

expression = 'What number is missing in the progression?'


def main():
    start_games(game_progression, expression)


if __name__ == '__main__':
    main()
