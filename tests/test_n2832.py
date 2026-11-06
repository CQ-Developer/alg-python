from pytest import fixture

from src.n2832 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [1, 4, 2, 1, 5] == solution.maximum_length_of_ranges([1, 5, 4, 3, 6])


def test_b(solution: Solution):
    assert [1, 2, 3, 4, 5] == solution.maximum_length_of_ranges([1, 2, 3, 4, 5])
