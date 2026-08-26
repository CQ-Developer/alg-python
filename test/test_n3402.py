from pytest import fixture

from src.n3402 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 15 == solution.minimum_operations([[3, 2], [1, 3], [3, 4], [0, 1]])


def test_b(solution: Solution):
    assert 12 == solution.minimum_operations([[3, 2, 1], [2, 1, 0], [1, 2, 3]])
