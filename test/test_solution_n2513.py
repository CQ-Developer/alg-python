from pytest import fixture

from src.solution_n2513 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.minimizeSet(2, 7, 1, 3)


def test_2(solution: Solution):
    assert 3 == solution.minimizeSet(3, 5, 2, 1)


def test_3(solution: Solution):
    assert 15 == solution.minimizeSet(2, 4, 8, 2)
