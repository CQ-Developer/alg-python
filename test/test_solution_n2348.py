from pytest import fixture

from src.solution_n2348 import Solution, SolutionA, SolutionB, SolutionC, SolutionD, SolutionE


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC, SolutionD, SolutionE])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 6 == solution.zero_filled_subarray([1, 3, 0, 0, 2, 0, 0, 4])


def test_b(solution: Solution):
    assert 9 == solution.zero_filled_subarray([0, 0, 0, 2, 0, 0])


def test_c(solution: Solution):
    assert 0 == solution.zero_filled_subarray([2, 10, 2019])
