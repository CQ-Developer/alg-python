from src.leetcode.n1014.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(11, self.solution.max_score_sightseeing_pair([8, 1, 5, 2, 6]))

    def test_2(self):
        self.assertEqual(2, self.solution.max_score_sightseeing_pair([1, 2]))
