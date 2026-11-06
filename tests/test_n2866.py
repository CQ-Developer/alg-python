from pytest import fixture

from src.n2866 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 13 == solution.maximum_sum_of_heights([5, 3, 4, 1, 1])


def test_2(solution: Solution):
    assert 22 == solution.maximum_sum_of_heights([6, 5, 3, 9, 2, 7])


def test_3(solution: Solution):
    assert 18 == solution.maximum_sum_of_heights([3, 2, 5, 5, 2, 3])
