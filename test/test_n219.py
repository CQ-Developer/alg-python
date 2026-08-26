from pytest import fixture

from src.n219 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.contains_nearby_duplicate([1, 2, 3, 1], 3)


def test_2(solution: Solution):
    assert solution.contains_nearby_duplicate([1, 0, 1, 1], 1)


def test_3(solution: Solution):
    assert not solution.contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)


def test_4(solution: Solution):
    assert not solution.contains_nearby_duplicate([1], 1)


def test_5(solution: Solution):
    assert not solution.contains_nearby_duplicate([1, 2, 1], 0)


def test_6(solution: Solution):
    assert solution.contains_nearby_duplicate([0, 1, 2, 3, 2, 5], 3)
