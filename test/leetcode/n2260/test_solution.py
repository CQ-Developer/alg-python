from unittest import TestCase, SkipTest

from src.leetcode.n2260.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        print('!!!!!!!!!!!!!!!!!!!!!')

    def test_1(self):
        self.assertEqual(4, self.solution.minimum_card_pickup([3, 4, 2, 3, 4, 7]))

    def test_2(self):
        self.assertEqual(-1, self.solution.minimum_card_pickup([1, 0, 5, 3]))
