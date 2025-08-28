from src.leetcode.n1019.solution import ListNode, Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([5, 5, 0], self.solution.next_larger_nodes(ListNode(2, ListNode(1, ListNode(5)))))

    def test_2(self):
        self.assertListEqual([7, 0, 5, 5, 0], self.solution.next_larger_nodes(ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
