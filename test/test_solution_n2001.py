from pytest import fixture

from src.solution_n2001 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 6 == solution.interchangeable_rectangles([[4, 8], [3, 6], [10, 20], [15, 30]])


def test_2(solution: Solution):
    assert 0 == solution.interchangeable_rectangles([[4, 5], [7, 8]])
