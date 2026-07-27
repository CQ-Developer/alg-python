from pytest import fixture

from src.solution_n3257 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.maximum_value_sum([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]])


def test_b(solution: Solution):
    assert 15 == solution.maximum_value_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_c(solution: Solution):
    assert 3 == solution.maximum_value_sum([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
