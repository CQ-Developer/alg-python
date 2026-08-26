from pytest import fixture

from src.n3555 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [2, 2, 0] == solution.min_subarray_sort([1, 3, 2, 4, 5], 3)


def test_b(solution: Solution):
    assert [4, 4] == solution.min_subarray_sort([5, 4, 3, 2, 1], 4)
