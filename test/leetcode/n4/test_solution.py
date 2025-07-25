from unittest import TestCase, SkipTest

from src.leetcode.n4.solution import Solution, SolutionA, SolutionB


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(2, self.solution.find_median_sorted_arrays([1, 3], [2]))

    def test_2(self):
        self.assertEqual(2.5, self.solution.find_median_sorted_arrays([1, 2], [3, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
