from pytest import fixture

from src.solution_n2517 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 8 == solution.maximumTastiness([13, 5, 1, 8, 21, 2], 3)


def test_2(solution: Solution):
    assert 2 == solution.maximumTastiness([1, 3, 1], 2)


def test_3(solution: Solution):
    assert 0 == solution.maximumTastiness([7, 7, 7, 7], 2)
