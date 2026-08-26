from pytest import fixture

from src.n3427 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 11 == solution.subarray_sum([2, 3, 1])


def test_b(solution: Solution):
    assert 13 == solution.subarray_sum([3, 1, 1, 2])
