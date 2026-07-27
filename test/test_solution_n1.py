from pytest import fixture

from src.solution_n1 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [0, 1] == solution.two_sum([2, 7, 11, 15], 9)


def test_2(solution: Solution):
    assert [1, 2] == solution.two_sum([3, 2, 4], 6)


def test_3(solution: Solution):
    assert [0, 1] == solution.two_sum([3, 3], 6)
