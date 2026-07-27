from unittest.mock import MagicMock, patch

from pytest import fixture

from src.solution_n278 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    with patch('src.solution_n278.is_bad_version') as mock_is_bad_version:
        mock_is_bad_version.side_effect = lambda v: v >= 4
        assert 4 == solution.first_bad_version(5)


def test_2(solution: Solution):
    with patch('src.solution_n278.is_bad_version') as mock_is_bad_version:
        mock_is_bad_version.side_effect = lambda v: v >= 1
        assert 1 == solution.first_bad_version(1)
