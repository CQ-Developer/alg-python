from pytest import fixture

from src.n3936 import Solution, SolutionA


@fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.minimum_swaps([0, 1, 0, 3, 12])


def test_2(solution: Solution):
    assert 1 == solution.minimum_swaps([0, 1, 0, 2])


def test_3(solution: Solution):
    assert 0 == solution.minimum_swaps([1, 2, 0])
