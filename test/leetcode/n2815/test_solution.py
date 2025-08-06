from src.leetcode.n2815.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(-1, self.solution.max_sum([112, 131, 411]))

    def test_2(self):
        self.assertEqual(5902, self.solution.max_sum([2536, 1613, 3366, 162]))

    def test_3(self):
        self.assertEqual(88, self.solution.max_sum([51, 71, 17, 24, 42]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
