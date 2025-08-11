from unittest import TestCase, SkipTest
from src.leetcode.n1010.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.num_pairs_divisible_by_60([30, 20, 150, 100, 40]))

    def test_2(self):
        self.assertEqual(3, self.solution.num_pairs_divisible_by_60([60, 60, 60]))
