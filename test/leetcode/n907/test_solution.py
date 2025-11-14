from src.leetcode.n907.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(17, self.solution.sum_subarray_mins([3, 1, 2, 4]))

    def test_b(self):
        self.assertEqual(444, self.solution.sum_subarray_mins([11, 81, 94, 43, 3]))

    def test_c(self):
        self.assertEqual(593, self.solution.sum_subarray_mins([71, 55, 82, 55]))

    def test_d(self):
        self.assertEqual(85, self.solution.sum_subarray_mins([85]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
