from pytest import fixture

from src.n1590 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1 == solution.min_subarray([3, 1, 4, 2], 6)


def test_b(solution: Solution):
    assert 2 == solution.min_subarray([6, 3, 5, 2], 9)


def test_c(solution: Solution):
    assert -1 == solution.min_subarray([1, 2, 3], 7)
