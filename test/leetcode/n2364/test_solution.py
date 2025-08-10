from src.leetcode.n2364.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test1(self):
        self.assertEqual(5, self.solution.count_bad_pairs([4, 1, 3, 3]))

    def test2(self):
        self.assertEqual(0, self.solution.count_bad_pairs([1, 2, 3, 4, 5]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
