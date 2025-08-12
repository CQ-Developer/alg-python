from src.leetcode.n3185.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.count_complete_day_pairs([12, 12, 30, 24, 24]))

    def test_2(self):
        self.assertEqual(3, self.solution.count_complete_day_pairs([72, 48, 24, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
