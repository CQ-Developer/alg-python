from pytest import fixture

from src.n3116 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 9 == solution.find_kth_smallest([3, 6, 9], 3)


def test_2(solution: Solution):
    assert 12 == solution.find_kth_smallest([5, 2], 7)


def test_3(solution: Solution):
    assert 35 == solution.find_kth_smallest([5], 7)
