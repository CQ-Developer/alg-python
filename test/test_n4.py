from pytest import fixture

from src.n4 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.find_median_sorted_arrays([1, 3], [2])


def test_2(solution: Solution):
    assert 2.5 == solution.find_median_sorted_arrays([1, 2], [3, 4])
