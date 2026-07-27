from pytest import fixture

from src.solution_n2016 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.maximum_difference([7, 1, 5, 4])


def test_2(solution: Solution):
    assert -1 == solution.maximum_difference([9, 4, 3, 2])


def test_3(solution: Solution):
    assert 9 == solution.maximum_difference([1, 5, 2, 10])
