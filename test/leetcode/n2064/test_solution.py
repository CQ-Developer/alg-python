import unittest
from src.leetcode.n2064.solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(3, self.solution.minimizedMaximum(6, [11, 6]))

    def test_2(self):
        self.assertEqual(5, self.solution.minimizedMaximum(7, [15, 10, 10]))

    def test_3(self):
        self.assertEqual(100000, self.solution.minimizedMaximum(1, [100000]))
