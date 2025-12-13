from src.leetcode.n3548.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertTrue(self.solution.can_partition_grid([[1, 4], [2, 3]]))

    def test_b(self):
        self.assertTrue(self.solution.can_partition_grid([[1, 2], [3, 4]]))

    def test_c(self):
        self.assertFalse(self.solution.can_partition_grid([[1, 2, 4], [2, 3, 5]]))

    def test_d(self):
        self.assertFalse(self.solution.can_partition_grid([[4, 1, 8], [3, 2, 6]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
