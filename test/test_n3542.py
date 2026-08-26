from pytest import fixture

from src.n3542 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1 == solution.min_operations([0, 2])


def test_b(solution: Solution):
    assert 3 == solution.min_operations([3, 1, 2, 1])


def test_c(solution: Solution):
    assert 4 == solution.min_operations([1, 2, 1, 2, 1, 2])
