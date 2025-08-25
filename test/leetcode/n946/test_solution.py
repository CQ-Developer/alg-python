from src.leetcode.n946.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertTrue(self.solution.validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

    def test_2(self):
        self.assertFalse(self.solution.validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
