from unittest import TestCase
from problems_01_10 import euler_01, euler_02, euler_03


class Euler01To10Tests(TestCase):

    def test_euler_1(self):
        self.assertEqual(euler_01.run(1000), 233168)

    def test_euler_2(self):
        self.assertEqual(euler_02.run(), 4613732)

    def test_euler_3(self):
        self.assertEqual(euler_03.run(), 6857)
