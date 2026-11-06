from pytest import fixture

from src.n3221 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 16 == solution.max_score([1, 5, 8])


def test_b(solution: Solution):
    assert 42 == solution.max_score([4, 5, 2, 8, 9, 1, 3])
