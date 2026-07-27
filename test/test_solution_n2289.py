from pytest import fixture

from src.solution_n2289 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 3 == solution.total_steps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11])


def test_b(solution: Solution):
    assert 0 == solution.total_steps([4, 5, 7, 7, 13])
