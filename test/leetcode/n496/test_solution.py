from src.leetcode.n496.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([-1, 3, -1], self.solution.next_greater_element([4, 1, 2], [1, 3, 4, 2]))

    def test_2(self):
        self.assertListEqual([3, -1], self.solution.next_greater_element([2, 4], [1, 2, 3, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
