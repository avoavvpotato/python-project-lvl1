#!/usr/bin/env python3

from brain_games.games.game_prime import game_prime
from brain_games.start import start_games

expression = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    start_games(game_prime, expression)


if __name__ == '__main__':
    main()
