from unittest import TestCase, SkipTest
from src.leetcode.n222.solution import TreeNode, Solution, SolutionA, SolutionB, SolutionC, SolutionD


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        self.assertEqual(6, self.solution.count_nodes(root))

    def test_2(self):
        self.assertEqual(0, self.solution.count_nodes(None))

    def test_3(self):
        root = TreeNode(1)
        self.assertEqual(1, self.solution.count_nodes(root))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()


class TestSolutionD(TestSolution):

    def setUp(self):
        self.solution = SolutionD()
