from pytest import fixture

from src.n2441 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.find_max_k([-1, 2, -3, 3])


def test_2(solution: Solution):
    assert 7 == solution.find_max_k([-1, 10, 6, 7, -7, 1])


def test_3(solution: Solution):
    assert -1 == solution.find_max_k([-10, 8, 6, 7, -2, -3])
