from src.leetcode.n503.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([2, -1, 2], self.solution.next_greater_elements([1, 2, 1]))

    def test_2(self):
        self.assertListEqual([2, 3, 4, -1, 4], self.solution.next_greater_elements([1, 2, 3, 4, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
