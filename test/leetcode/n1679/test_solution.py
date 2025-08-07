from unittest import TestCase, SkipTest

from src.leetcode.n1679.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.max_operations([1, 2, 3, 4], 5))

    def test_2(self):
        self.assertEqual(1, self.solution.max_operations([3, 1, 3, 4, 3], 6))
