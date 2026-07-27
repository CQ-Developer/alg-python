from pytest import fixture

from src.solution_n53 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 6 == solution.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


def test_b(solution: Solution):
    assert 1 == solution.max_subarray([1])


def test_c(solution: Solution):
    assert 23 == solution.max_subarray([5, 4, -1, 7, 8])


def test_d(solution: Solution):
    assert -1 == solution.max_subarray([-1])
