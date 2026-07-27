from pytest import fixture

from src.solution_n2909 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 9 == solution.minimum_sum([8, 6, 1, 5, 3])


def test_b(solution: Solution):
    assert 13 == solution.minimum_sum([5, 4, 8, 7, 10, 2])


def test_c(solution: Solution):
    assert -1 == solution.minimum_sum([6, 5, 4, 3, 4, 5])
