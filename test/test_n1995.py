from pytest import fixture

from src.n1995 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.count_quadruplets([1, 2, 3, 6])


def test_2(solution: Solution):
    assert 0 == solution.count_quadruplets([3, 3, 6, 4, 5])


def test_3(solution: Solution):
    assert 4 == solution.count_quadruplets([1, 1, 1, 3, 5])
