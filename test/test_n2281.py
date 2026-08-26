from pytest import fixture

from src.n2281 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 44 == solution.total_strength([1, 3, 1, 2])


def test_b(solution: Solution):
    assert 213 == solution.total_strength([5, 4, 6])
