#!/usr/bin/env python3

import prompt
from random import randrange


def game_even():
    value = randrange(0, 101)
    get_answer = prompt.string(f'Question: {value} ')
    if value % 2:
        real_answer = 'no'
    else:
        real_answer = 'yes'
    return real_answer, get_answer


def main():
    pass


if __name__ == '__main__':
    main()
