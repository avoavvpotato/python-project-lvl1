#!/usr/bin/env python3

import prompt


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def start_games(game, expresson):
    name = hello()
    print(expresson)
    for _ in range(3):
        a, b = game()
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
    pass


if __name__ == '__main__':
    main()
