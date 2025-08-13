from src.leetcode.n1031.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(20, self.solution.max_sum_two_no_overlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))

    def test_2(self):
        self.assertEqual(29, self.solution.max_sum_two_no_overlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))

    def test_3(self):
        self.assertEqual(31, self.solution.max_sum_two_no_overlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
