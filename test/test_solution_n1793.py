from pytest import fixture

from src.solution_n1793 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 15 == solution.maximum_score([1, 4, 3, 7, 4, 5], 3)


def test_b(solution: Solution):
    assert 20 == solution.maximum_score([5, 5, 4, 5, 4, 1, 1, 1], 0)
