from pytest import fixture

from src.solution_n1504 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 13 == solution.num_submat([[1, 0, 1], [1, 1, 0], [1, 1, 0]])


def test_b(solution: Solution):
    assert 24 == solution.num_submat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]])
