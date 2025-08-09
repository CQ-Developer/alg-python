from src.leetcode.n624.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.max_distance([[1, 2, 3], [4, 5], [1, 2, 3]]))

    def test_2(self):
        self.assertEqual(0, self.solution.max_distance([[1], [1]]))
