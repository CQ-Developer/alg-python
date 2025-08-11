from unittest import TestCase, SkipTest
from src.leetcode.n3584.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(81, self.solution.maximum_product([-1, -9, 2, 3, -2, -3, 1], 1))

    def test_2(self):
        self.assertEqual(20, self.solution.maximum_product([1, 3, -5, 5, 6, -4], 3))

    def test_3(self):
        self.assertEqual(35, self.solution.maximum_product([2, -1, 2, -6, 5, 2, -5, 7], 2))
