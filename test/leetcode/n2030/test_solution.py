from src.leetcode.n2030.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual('eet', self.solution.smallest_subsequence('leet', 3, 'e', 1))

    def test_b(self):
        self.assertEqual('ecde', self.solution.smallest_subsequence('leetcode', 4, 'e', 2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
