from unittest import TestCase, SkipTest

from src.leetcode.n2342.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(54, self.solution.maximum_sum([18, 43, 36, 13, 7]))

    def test_2(self):
        self.assertEqual(-1, self.solution.maximum_sum([10, 12, 19, 14]))
