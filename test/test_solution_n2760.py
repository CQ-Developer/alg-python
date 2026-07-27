from pytest import fixture

from src.solution_n2760 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 3 == solution.longest_alternating_subarray([3, 2, 5, 4], 5)


def test_b(solution: Solution):
    assert 1 == solution.longest_alternating_subarray([1, 2], 2)


def test_c(solution: Solution):
    assert 3 == solution.longest_alternating_subarray([2, 3, 4, 5], 4)
