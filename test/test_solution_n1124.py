from pytest import fixture

from src.solution_n1124 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution):
    assert solution.longest_WPI([9, 9, 6, 0, 6, 6, 9]) == 3


def test_b(solution):
    assert solution.longest_WPI([6, 6, 6]) == 0
