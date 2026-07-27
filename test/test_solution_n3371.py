from pytest import fixture

from src.solution_n3371 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 10 == solution.get_largest_outlier([2, 3, 5, 10])


def test_2(solution: Solution):
    assert 4 == solution.get_largest_outlier([-2, -1, -3, -6, 4])


def test_3(solution: Solution):
    assert 5 == solution.get_largest_outlier([1, 1, 1, 1, 1, 5, 5])
