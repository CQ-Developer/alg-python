from src.leetcode.n1512.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(4, self.solution.num_identical_pairs([1, 2, 3, 1, 1, 3]))

    def test_2(self):
        self.assertEqual(6, self.solution.num_identical_pairs([1, 1, 1, 1]))

    def test_3(self):
        self.assertEqual(0, self.solution.num_identical_pairs([1, 2, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
