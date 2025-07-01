from src.leetcode.n2476.solution import TreeNode, Solution
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        root = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(13, TreeNode(9), TreeNode(15, TreeNode(14), None)))
        self.assertListEqual([[2, 2], [4, 6], [15, -1]], self.solution.closest_nodes(root, [2, 5, 16]))

    def test_2(self):
        root = TreeNode(4, None, TreeNode(9))
        self.assertListEqual([[-1, 4]], self.solution.closest_nodes(root, [3]))
