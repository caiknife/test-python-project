#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

testcase for euler.py
"""

import unittest
from ProjectEuler.euler import prime_factors, prime_generator, is_prime, make_primes, factor, \
    hexagon_number, pentagon_number, triangle_number


class TestEuler(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(20))

    def test_make_primes(self):
        primes = make_primes(100)
        for i in primes:
            self.assertTrue(is_prime(i))

    def test_prime_generator(self):
        primes = make_primes(100)
        g = prime_generator()
        i, n = 0, 0
        while True:
            n = g.next()
            if n > 100:
                break
            self.assertEqual(n, primes[i])
            i += 1

    def test_prime_factors(self):
        primes = [
            [14, [2, 7]], [15, [3, 5]],
            [644, [2, 2, 7, 23]], [645, [3, 5, 43]], [646, [2, 17, 19]]
        ]
        for p in primes:
            self.assertEqual(prime_factors(p[0]), p[1])

    def test_factor(self):
        for n in xrange(3, 100, 3):
            self.assertTrue(factor(n))

        for n in xrange(5, 100, 5):
            self.assertTrue(factor(n))

    def test_hexagon_number(self):
        for n in xrange(1, 100):
            self.assertEqual(hexagon_number(n), n * (2 * n - 1))

    def test_pentagon_number(self):
        for n in xrange(1, 100):
            self.assertEqual(pentagon_number(n), n * (3 * n - 1) / 2)

    def test_triangle_number(self):
        for n in xrange(1, 100):
            self.assertEqual(triangle_number(n), n * (n + 1) / 2)


if __name__ == '__main__':
    unittest.main()
