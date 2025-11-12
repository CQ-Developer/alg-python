from src.leetcode.n755.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls) -> None:
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([2, 2, 2, 3, 2, 2, 2], self.solution.pour_water([2, 1, 1, 2, 1, 2, 2], 4, 3))

    def test_b(self):
        self.assertListEqual([2, 3, 3, 4], self.solution.pour_water([1, 2, 3, 4], 2, 2))

    def test_c(self):
        self.assertListEqual([4, 4, 4], self.solution.pour_water([3, 1, 3], 5, 1))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
