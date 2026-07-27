from pytest import fixture

from src.solution_n755 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [2, 2, 2, 3, 2, 2, 2] == solution.pour_water([2, 1, 1, 2, 1, 2, 2], 4, 3)


def test_b(solution: Solution):
    assert [2, 3, 3, 4] == solution.pour_water([1, 2, 3, 4], 2, 2)


def test_c(solution: Solution):
    assert [4, 4, 4] == solution.pour_water([3, 1, 3], 5, 1)
