from pytest import fixture

from src.n1679 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.max_operations([1, 2, 3, 4], 5)


def test_2(solution: Solution):
    assert 1 == solution.max_operations([3, 1, 3, 4, 3], 6)
