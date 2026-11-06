from pytest import fixture

from src.n560 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.subarray_sum([1, 1, 1], 2)


def test_b(solution: Solution):
    assert 2 == solution.subarray_sum([1, 2, 3], 3)
