from pytest import fixture

from src.n2616 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1 == solution.minimizeMax([10, 1, 2, 7, 1, 3], 2)


def test_b(solution: Solution):
    assert 0 == solution.minimizeMax([4, 2, 1, 2], 1)


def test_c(solution: Solution):
    assert 1 == solution.minimizeMax([3, 4, 2, 3, 2, 1, 2], 3)
