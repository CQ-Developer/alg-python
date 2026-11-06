from pytest import fixture

from src.n2242 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 24 == solution.maximum_score([5, 2, 9, 8, 4], [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])


def test_b(solution: Solution):
    assert -1 == solution.maximum_score([9, 20, 6, 4, 11, 12], [[0, 3], [5, 3], [2, 4], [1, 3]])
