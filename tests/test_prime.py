from unittest import TestCase

from lib.prime import postponed_sieve, prime_factors


class PrimeTest(TestCase):

    def test_prime_gen(self):
        g = postponed_sieve()
        self.assertEqual(next(g), 2)
        self.assertEqual(next(g), 3)
        self.assertEqual(next(g), 5)
        self.assertEqual(next(g), 7)
        self.assertEqual(next(g), 11)
        self.assertEqual(next(g), 13)
        self.assertEqual(next(g), 17)
        self.assertEqual(next(g), 19)
        self.assertEqual(next(g), 23)
        self.assertEqual(next(g), 29)
        self.assertEqual(next(g), 31)
        self.assertEqual(next(g), 37)
        self.assertEqual(next(g), 41)
        self.assertEqual(next(g), 43)
        self.assertEqual(next(g), 47)
        self.assertEqual(next(g), 53)
        self.assertEqual(next(g), 59)
        self.assertEqual(next(g), 61)
        self.assertEqual(next(g), 67)
        self.assertEqual(next(g), 71)

    def test_prime_factors(self):
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])
