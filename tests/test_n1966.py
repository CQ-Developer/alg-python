from pytest import fixture

from src.n1966 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1 == solution.binary_searchable_numbers([7])


def test_b(solution: Solution):
    assert 1 == solution.binary_searchable_numbers([-1, 5, 2])
