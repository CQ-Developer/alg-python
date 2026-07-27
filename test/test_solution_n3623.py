from pytest import fixture

from src.solution_n3623 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.count_trapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]])


def test_2(solution: Solution):
    assert 1 == solution.count_trapezoids([[0, 0], [1, 0], [0, 1], [2, 1]])
