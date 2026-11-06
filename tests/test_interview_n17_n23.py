from pytest import fixture

from src.interview_n17_n23 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [1, 0, 2] == solution.find_square([[1, 0, 1], [0, 0, 1], [0, 0, 1]])


def test_b(solution: Solution):
    assert [0, 0, 1] == solution.find_square([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
