from pytest import fixture

from src.n1546 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.max_non_overlapping([1, 1, 1, 1, 1], 2)


def test_b(solution: Solution):
    assert 2 == solution.max_non_overlapping([-1, 3, 5, 1, 4, 2, -9], 6)


def test_c(solution: Solution):
    assert 2 == solution.max_non_overlapping([-5, 5, -4, 5, 4], 5)
