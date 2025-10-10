from src.leetcode.n1944.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([3, 1, 2, 1, 1, 0], self.solution.can_see_persons_count([10, 6, 8, 5, 11, 9]))

    def test_b(self):
        self.assertListEqual([4, 1, 1, 1, 0], self.solution.can_see_persons_count([5, 1, 2, 3, 10]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
