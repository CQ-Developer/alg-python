from unittest.mock import MagicMock, patch

from pytest import fixture

from src.solution_n374 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    with patch('src.solution_n374.guess') as mock:
        pick = 6
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        assert 6 == solution.guess_number(10)


def test_2(solution: Solution):
    with patch('src.solution_n374.guess') as mock:
        pick = 1
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        assert 1 == solution.guess_number(1)


def test_3(solution: Solution):
    with patch('src.solution_n374.guess') as mock:
        pick = 1
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        assert 1 == solution.guess_number(2)
