#!/usr/bin/env python3

import prompt
from random import randrange


def game_progression():
    value_1 = randrange(0, 101)
    value_2 = randrange(1, 11)
    array = [*range(value_1, value_1 + 10 * value_2, value_2)]
    index = randrange(10)
    v = f"{' '.join(str(w) for w in array[:index])} \
.. {' '.join(str(w) for w in array[index+1:])}"
    real_answer = array[index]
    print(f'Question: {v}')
    get_answer = prompt.string('Your answer: ')
    return str(real_answer), get_answer


def main():
    pass


if __name__ == '__main__':
    main()
