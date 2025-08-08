from unittest import TestCase, SkipTest

from src.leetcode.interview.n16.n24.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([[5, 6]], self.solution.pair_sums([5, 6, 5], 11))

    def test_2(self):
        self.assertListEqual([[5, 6], [5, 6]], self.solution.pair_sums([5, 6, 5, 6], 11))
