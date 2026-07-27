from pytest import fixture

from src.solution_n3381 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.max_subarray_sum([-5, 1, 2, -3, 4], 2)


def test_b(solution: Solution):
    assert -10 == solution.max_subarray_sum([-1, -2, -3, -4, -5], 4)


def test_c(solution: Solution):
    assert 3 == solution.max_subarray_sum([1, 2], 1)
