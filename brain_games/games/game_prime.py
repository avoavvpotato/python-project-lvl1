#!/usr/bin/env python3

import prompt
from random import randrange


def is_prime(n):
  if n == 2:
    return True
  if n == 1:
    return False
  for i in range(2, n):
    if (n % i) == 0:
      return False
  return True


def game_prime():
    value_1 = randrange(1, 1000)
    if is_prime(value_1):
        real_answer = 'yes'
    else:
        real_answer = 'no'
    print(f'Question: {value_1}')
    get_answer = prompt.string(f'Your answer: ')
    return real_answer, get_answer


def main():
    pass


if __name__ == '__main__':
    main()
