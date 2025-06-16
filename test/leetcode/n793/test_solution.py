from src.leetcode.n793.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.preimageSizeFZF(0))

    def test_2(self):
        self.assertEqual(0, self.solution.preimageSizeFZF(5))

    def test_3(self):
        self.assertEqual(5, self.solution.preimageSizeFZF(3))
