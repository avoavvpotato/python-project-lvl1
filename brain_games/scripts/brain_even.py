#!/usr/bin/env python3

import prompt
from random import randrange


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


def game_even():
    value = randrange(0, 101)
    get_answer = prompt.string(f'Question: {value} ')
    if value % 2:
        real_answer = 'no'
    else:
        real_answer = 'yes'
    return real_answer, get_answer


def f():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        a, b = game_even()
        if a != b:
            print(f"'{b}' is wrong answer ;(. Correct answer was '{a}'.")
            print(f"Let's try again, {name}!")
            x = False
            break
        else:
            x = True
            print('Correct!')
    if x is True:
        print(f'Congratulations, {name}!')


def main():
    f()


if __name__ == '__main__':
    main()
