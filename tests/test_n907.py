from pytest import fixture

from src.n907 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 17 == solution.sum_subarray_mins([3, 1, 2, 4])


def test_b(solution: Solution):
    assert 444 == solution.sum_subarray_mins([11, 81, 94, 43, 3])


def test_c(solution: Solution):
    assert 593 == solution.sum_subarray_mins([71, 55, 82, 55])


def test_d(solution: Solution):
    assert 85 == solution.sum_subarray_mins([85])
