#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def get_sorted_digits(n):
    return sorted(str(n))


def has_same_digits(n, itertimes=6):
    digits = get_sorted_digits(n)
    for i in xrange(2, itertimes):
        if digits != get_sorted_digits(n*i):
            return False
    return True


def main():
    n = 0
    while True:
        n += 1
        if has_same_digits(n):
            print n
            break


if __name__ == '__main__':
    main()
