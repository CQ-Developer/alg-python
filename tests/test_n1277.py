from pytest import fixture

from src.n1277 import Solution, SolutionA, SolutionB, SolutionC, SolutionD


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 15 == solution.count_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])


def test_b(solution: Solution):
    assert 7 == solution.count_squares([[1, 0, 1], [1, 1, 0], [1, 1, 0]])
