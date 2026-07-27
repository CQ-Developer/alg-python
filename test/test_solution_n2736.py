from pytest import fixture

from src.solution_n2736 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [6, 10, 7] == solution.maximum_sum_queries([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]])


def test_b(solution: Solution):
    assert [9, 9, 9] == solution.maximum_sum_queries([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]])


def test_c(solution: Solution):
    assert [-1] == solution.maximum_sum_queries([2, 1], [2, 3], [[3, 3]])
