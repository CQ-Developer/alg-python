from pytest import fixture

from src.n162 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.find_peak_element([1, 2, 3, 1])


def test_2(solution: Solution):
    assert solution.find_peak_element([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
