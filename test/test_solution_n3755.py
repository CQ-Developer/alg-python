from pytest import fixture

from src.solution_n3755 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.max_balanced_subarray([3, 1, 3, 2, 0])


def test_b(solution: Solution):
    assert 8 == solution.max_balanced_subarray([3, 2, 8, 5, 4, 14, 9, 15])


def test_c(solution: Solution):
    assert 0 == solution.max_balanced_subarray([4, 1, 2, 3, 2, 2, 0, 4, 2, 3, 4])
