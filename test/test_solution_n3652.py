from pytest import fixture

from src.solution_n3652 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 10 == solution.max_profit([4, 2, 8], [-1, 0, 1], 2)


def test_b(solution: Solution):
    assert 9 == solution.max_profit([5, 4, 3], [1, 1, 0], 2)
