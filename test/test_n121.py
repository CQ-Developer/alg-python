from pytest import fixture

from src.n121 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.max_profit([7, 1, 5, 3, 6, 4])


def test_2(solution: Solution):
    assert 0 == solution.max_profit([7, 6, 4, 3, 1])
