from src.leetcode.n3404.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(1, self.solution.number_of_subsequences([1, 2, 3, 4, 3, 6, 1]))

    def test_2(self):
        self.assertEqual(3, self.solution.number_of_subsequences([3, 4, 3, 4, 3, 4, 3, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
