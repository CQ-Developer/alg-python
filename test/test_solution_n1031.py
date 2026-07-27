from pytest import fixture

from src.solution_n1031 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 20 == solution.max_sum_two_no_overlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)


def test_2(solution: Solution):
    assert 29 == solution.max_sum_two_no_overlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2)


def test_3(solution: Solution):
    assert 31 == solution.max_sum_two_no_overlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3)
