from src.leetcode.n33.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(4, self.solution.search([4, 5, 6, 7, 0, 1, 2], 0))

    def test_2(self):
        self.assertEqual(-1, self.solution.search([4, 5, 6, 7, 0, 1, 2], 3))

    def test_3(self):
        self.assertEqual(-1, self.solution.search([1], 0))
