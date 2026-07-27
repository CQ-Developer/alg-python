from pytest import fixture

from src.solution_n1439 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 7 == solution.kth_smallest([[1, 3, 11], [2, 4, 6]], 5)


def test_2(solution: Solution):
    assert 17 == solution.kth_smallest([[1, 3, 11], [2, 4, 6]], 9)


def test_3(solution: Solution):
    assert 9 == solution.kth_smallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7)


def test_4(solution: Solution):
    assert 12 == solution.kth_smallest([[1, 1, 10], [2, 2, 9]], 7)
