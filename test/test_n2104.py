from pytest import fixture

from src.n2104 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.sub_array_ranges([1, 2, 3])


def test_b(solution: Solution):
    assert 4 == solution.sub_array_ranges([1, 3, 3])


def test_c(solution: Solution):
    assert 59 == solution.sub_array_ranges([4, -2, -3, 4, 1])
