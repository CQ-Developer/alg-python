from pytest import fixture

from src.n2334 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert solution.valid_subarray_size([1, 3, 4, 3, 1], 6) in {3}


def test_b(solution: Solution):
    assert solution.valid_subarray_size([6, 5, 6, 5, 8], 7) in {1, 2, 3, 4, 5}
