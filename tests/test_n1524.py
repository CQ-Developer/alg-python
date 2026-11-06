from pytest import fixture

from src.n1524 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.num_of_subarrays([1, 3, 5])


def test_b(solution: Solution):
    assert 0 == solution.num_of_subarrays([2, 4, 6])


def test_c(solution: Solution):
    assert 16 == solution.num_of_subarrays([1, 2, 3, 4, 5, 6, 7])


def test_d(solution: Solution):
    assert 4 == solution.num_of_subarrays([100, 100, 99, 99])


def test_e(solution: Solution):
    assert 1 == solution.num_of_subarrays([7])
