from src.leetcode.n278.solution import Solution
from unittest import TestCase
from unittest.mock import patch, MagicMock


class TestSolution(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    @patch('src.leetcode.n278.solution.is_bad_version')
    def test_1(self, mock_is_bad_version: MagicMock):
        def mocked(v: int) -> bool:
            return v >= 4

        mock_is_bad_version.side_effect = mocked
        self.assertEqual(4, self.solution.first_bad_version(5))

    @patch('src.leetcode.n278.solution.is_bad_version')
    def test_2(self, mock_is_bad_version: MagicMock):
        def mocked(v: int) -> bool:
            return v >= 1

        mock_is_bad_version.side_effect = mocked
        self.assertEqual(1, self.solution.first_bad_version(1))
