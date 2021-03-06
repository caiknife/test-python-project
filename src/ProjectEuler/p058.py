#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Spiral primes
Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
from euler import is_prime


def sprial_numbers():
    n, step, since_last = 1, 2, 0
    while True:
        yield n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0


def main():
    level, primes = 0, 0
    for i, n in enumerate(sprial_numbers()):
        if (i - 1) % 4 == 0:
            level += 1

        if is_prime(n):
            primes += 1

        side_length = (2 * level) + 1

        ratio = float(primes) / float(i + 1)
        if 0 < ratio < 0.1:
            print side_length
            return


if __name__ == '__main__':
    main()
