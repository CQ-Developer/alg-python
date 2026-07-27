from pytest import fixture

from src.solution_n1508 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 13 == solution.range_sum([1, 2, 3, 4], 4, 1, 5)


def test_2(solution: Solution):
    assert 6 == solution.range_sum([1, 2, 3, 4], 4, 3, 4)


def test_3(solution: Solution):
    assert 50 == solution.range_sum([1, 2, 3, 4], 4, 1, 10)
