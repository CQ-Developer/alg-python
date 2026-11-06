from pytest import fixture

from src.n3026 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 11 == solution.maximum_subarray_sum([1, 2, 3, 4, 5, 6], 1)


def test_b(solution: Solution):
    assert 11 == solution.maximum_subarray_sum([-1, 3, 2, 4, 5], 3)


def test_c(solution: Solution):
    assert -6 == solution.maximum_subarray_sum([-1, -2, -3, -4], 2)
