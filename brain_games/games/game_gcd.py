#!/usr/bin/env python3

import prompt
from random import randrange
import math


def game_gcd():
    value_1 = randrange(1, 101)
    value_2 = randrange(1, 101)
    real_answer = math.gcd(value_1, value_2)
    print(f'Question: {value_1} {value_2}')
    get_answer = prompt.string(f'Your answer: ')
    return str(real_answer), get_answer


def main():
    pass


if __name__ == '__main__':
    main()
