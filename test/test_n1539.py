from pytest import fixture

from src.n1539 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 9 == solution.find_kth_positive([2, 3, 4, 7, 11], 5)


def test_2(solution: Solution):
    assert 6 == solution.find_kth_positive([1, 2, 3, 4], 2)
