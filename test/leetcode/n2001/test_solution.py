from unittest import TestCase, SkipTest
from src.leetcode.n2001.solution import Solution, SolutionA


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(6, self.solution.interchangeable_rectangles([[4, 8], [3, 6], [10, 20], [15, 30]]))

    def test_2(self):
        self.assertEqual(0, self.solution.interchangeable_rectangles([[4, 5], [7, 8]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
