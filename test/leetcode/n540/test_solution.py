from src.leetcode.n540.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(2, self.solution.single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))

    def test_2(self):
        self.assertEqual(10, self.solution.single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
