from pytest import fixture

from src.solution_n3134 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.median_of_uniqueness_array([1, 2, 3])


def test_2(solution: Solution):
    assert 2 == solution.median_of_uniqueness_array([3, 4, 3, 4, 5])


def test_3(solution: Solution):
    assert 2 == solution.median_of_uniqueness_array([4, 3, 5, 4])
