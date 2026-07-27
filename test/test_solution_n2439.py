from pytest import fixture

from src.solution_n2439 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.minimizeArrayValue([3, 7, 1, 6])


def test_2(solution: Solution):
    assert 10 == solution.minimizeArrayValue([10, 1])
