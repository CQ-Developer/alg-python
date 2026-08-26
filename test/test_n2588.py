from pytest import fixture

from src.n2588 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.beautiful_subarrays([4, 3, 1, 2, 4])


def test_b(solution: Solution):
    assert 0 == solution.beautiful_subarrays([1, 10, 4])
