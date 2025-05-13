import unittest
from src.leetcode.n1760.solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(3, self.solution.minimumSize([9], 2))

    def test_2(self):
        self.assertEqual(2, self.solution.minimumSize([2, 4, 8, 2], 4))

    def test_3(self):
        self.assertEqual(7, self.solution.minimumSize([7, 17], 2))
