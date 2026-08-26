from pytest import fixture

from src.n523 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert solution.check_subarray_sum([23, 2, 4, 6, 7], 6)


def test_b(solution: Solution):
    assert solution.check_subarray_sum([23, 2, 6, 4, 7], 6)


def test_c(solution: Solution):
    assert not solution.check_subarray_sum([23, 2, 6, 4, 7], 13)
