from src.leetcode.n2867.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.count_paths(5, [[1, 2], [1, 3], [2, 4], [2, 5]]))

    def test_b(self):
        self.assertEqual(6, self.solution.count_paths(6, [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
