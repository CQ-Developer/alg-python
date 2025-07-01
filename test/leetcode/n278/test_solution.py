from src.leetcode.n278.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest
from unittest.mock import patch, MagicMock


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    @patch('src.leetcode.n278.solution.is_bad_version')
    def test_1(self, mock_is_bad_version: MagicMock):
        mock_is_bad_version.side_effect = lambda v: v >= 4
        self.assertEqual(4, self.solution.first_bad_version(5))

    @patch('src.leetcode.n278.solution.is_bad_version')
    def test_2(self, mock_is_bad_version: MagicMock):
        mock_is_bad_version.side_effect = lambda v: v >= 1
        self.assertEqual(1, self.solution.first_bad_version(1))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
