from src.leetcode.tianchi2022.ev2bru.q3.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([5, 5, 6], self.solution.arrange_bookshelf([5, 5, 6, 5], 2))

    def test_b(self):
        self.assertListEqual([5, 5, 6, 5], self.solution.arrange_bookshelf([5, 5, 6, 5], 3))

    def test_c(self):
        self.assertListEqual([3, 8, 9, 2], self.solution.arrange_bookshelf([3, 3, 9, 8, 9, 2, 8], 1))

    def test_d(self):
        self.assertListEqual([1, 2, 2, 1, 3, 3], self.solution.arrange_bookshelf([2, 1, 2, 2, 1, 3, 3, 1, 3, 3], 2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
