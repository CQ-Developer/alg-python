from pytest import fixture

from src.n1749 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 5 == solution.max_absolute_sum([1, -3, 2, 3, -4])


def test_b(solution: Solution):
    assert 8 == solution.max_absolute_sum([2, -5, 1, -4, 3, -2])
