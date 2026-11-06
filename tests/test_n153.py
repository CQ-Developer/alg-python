from pytest import fixture

from src.n153 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.find_min([3, 4, 5, 1, 2])


def test_2(solution: Solution):
    assert 0 == solution.find_min([4, 5, 6, 7, 0, 1, 2])


def test_3(solution: Solution):
    assert 11 == solution.find_min([11, 13, 15, 17])
