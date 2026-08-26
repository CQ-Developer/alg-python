from pytest import fixture

from src.n456 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert not solution.find_132_pattern([1, 2, 3, 4])


def test_2(solution: Solution):
    assert solution.find_132_pattern([3, 1, 4, 2])


def test_3(solution: Solution):
    assert solution.find_132_pattern([-1, 3, 2, 0])
