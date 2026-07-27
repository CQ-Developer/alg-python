from pytest import fixture

from src.solution_n402 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert '1219' == solution.remove_k_digits('1432219', 3)


def test_b(solution: Solution):
    assert '200' == solution.remove_k_digits('10200', 1)


def test_c(solution: Solution):
    assert '0' == solution.remove_k_digits('10', 2)
