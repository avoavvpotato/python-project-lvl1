#!/usr/bin/env python3

from brain_games.games.game_gcd import game_gcd
from brain_games.start import start_games

expression = 'Find the greatest common divisor of given numbers.'


def main():
    start_games(game_gcd, expression)


if __name__ == '__main__':
    main()
