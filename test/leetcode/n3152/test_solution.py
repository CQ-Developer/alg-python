from src.leetcode.n3152.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([False], self.solution.is_array_special([3, 4, 1, 2, 6], [[0, 4]]))

    def test_b(self):
        self.assertListEqual([False, True], self.solution.is_array_special([4, 3, 1, 6], [[0, 2], [2, 3]]))

    def test_c(self):
        self.assertListEqual([True], self.solution.is_array_special([2, 1], [[0, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
