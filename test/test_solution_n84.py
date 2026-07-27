from pytest import fixture

from src.solution_n84 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 10 == solution.largest_rectangle_area([2, 1, 5, 6, 2, 3])


def test_b(solution: Solution):
    assert 4 == solution.largest_rectangle_area([2, 4])
