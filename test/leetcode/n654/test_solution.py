from src.leetcode.n654.solution import TreeNode, Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls) -> None:
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(TreeNode(6, TreeNode(3, right=TreeNode(2, right=TreeNode(1))), TreeNode(5, left=TreeNode(0))), self.solution.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5]))

    def test_2(self):
        self.assertEqual(TreeNode(3, right=TreeNode(2, right=TreeNode(1))), self.solution.construct_maximum_binary_tree([3, 2, 1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
