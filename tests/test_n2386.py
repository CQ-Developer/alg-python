from pytest import fixture

from src.n2386 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.k_sum([2, 4, -2], 5)


def test_2(solution: Solution):
    assert 10 == solution.k_sum([1, -2, 3, 4, -10, 12], 16)
