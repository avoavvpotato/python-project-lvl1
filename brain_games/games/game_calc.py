#!/usr/bin/env python3

import prompt
from random import randrange
import random
import operator


def game_calc():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    ops_array = ['*', '+', '-']
    value_1 = randrange(0, 101)
    value_2 = randrange(0, 101)
    random_num = random.choice(ops_array)
    real_answer = ops[random_num](value_1, value_2)
    print(f'Question: {value_1} {random_num} {value_2}')
    get_answer = prompt.string(f'Your answer: ')
    return str(real_answer), get_answer


def main():
    pass


if __name__ == '__main__':
    main()
