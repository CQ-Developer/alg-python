from pytest import fixture

from src.n3404 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.number_of_subsequences([1, 2, 3, 4, 3, 6, 1])


def test_2(solution: Solution):
    assert 3 == solution.number_of_subsequences([3, 4, 3, 4, 3, 4, 3, 4])
