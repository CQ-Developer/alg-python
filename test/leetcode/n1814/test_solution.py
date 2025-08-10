from src.leetcode.n1814.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.count_nice_pairs([42, 11, 1, 97]))

    def test_2(self):
        self.assertEqual(4, self.solution.count_nice_pairs([13, 10, 35, 24, 76]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
