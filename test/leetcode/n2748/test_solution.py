from src.leetcode.n2748.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.count_beautiful_pairs([2, 5, 1, 4]))

    def test_2(self):
        self.assertEqual(2, self.solution.count_beautiful_pairs([11, 21, 12]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
