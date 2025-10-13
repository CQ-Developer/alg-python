from src.leetcode.n2454.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([9, 6, 6, -1, -1], self.solution.second_greater_element([2, 4, 0, 9, 6]))

    def test_b(self):
        self.assertListEqual([-1, -1], self.solution.second_greater_element([3, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
