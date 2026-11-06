from pytest import fixture

from src.n3430 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 20 == solution.min_max_subarray_sum([1, 2, 3], 2)


def test_b(solution: Solution):
    assert -6 == solution.min_max_subarray_sum([1, -3, 1], 2)
