from src.leetcode.n2552.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.count_quadruplets([1, 3, 2, 4, 5]))

    def test_b(self):
        self.assertEqual(0, self.solution.count_quadruplets([1, 2, 3, 4]))
