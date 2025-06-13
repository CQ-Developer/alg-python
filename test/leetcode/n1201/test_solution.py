from src.leetcode.n1201.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.nthUglyNumber(3, 2, 3, 5))

    def test_2(self):
        self.assertEqual(6, self.solution.nthUglyNumber(4, 2, 3, 4))

    def test_3(self):
        self.assertEqual(10, self.solution.nthUglyNumber(5, 2, 11, 13))
