from pytest import fixture

from src.n2025 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.ways_to_partition([2, -1, 2], 3)


def test_2(solution: Solution):
    assert 2 == solution.ways_to_partition([0, 0, 0], 1)


def test_3(solution: Solution):
    assert 4 == solution.ways_to_partition([22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33)
