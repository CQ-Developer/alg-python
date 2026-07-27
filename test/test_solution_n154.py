from pytest import fixture

from src.solution_n154 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.find_min([1, 3, 5])


def test_2(solution: Solution):
    assert 0 == solution.find_min([2, 2, 2, 0, 1])
