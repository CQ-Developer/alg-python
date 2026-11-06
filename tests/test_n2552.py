from pytest import fixture

from src.n2552 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.count_quadruplets([1, 3, 2, 4, 5])


def test_b(solution: Solution):
    assert 0 == solution.count_quadruplets([1, 2, 3, 4])
