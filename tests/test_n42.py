from pytest import fixture

from src.n42 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 6 == solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])


def test_b(solution: Solution):
    assert 9 == solution.trap([4, 2, 0, 3, 2, 5])
