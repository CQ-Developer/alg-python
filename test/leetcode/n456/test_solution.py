from src.leetcode.n456.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertFalse(self.solution.find_132_pattern([1, 2, 3, 4]))

    def test_2(self):
        self.assertTrue(self.solution.find_132_pattern([3, 1, 4, 2]))

    def test_3(self):
        self.assertTrue(self.solution.find_132_pattern([-1, 3, 2, 0]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
