from src.leetcode.n69.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.my_sqrt(4))

    def test_2(self):
        self.assertEqual(2, self.solution.my_sqrt(8))
