from pytest import fixture

from src.n3364 import Solution, SolutionA, SolutionB


@fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.minimum_sum_subarray([3, -2, 1, 4], 2, 3)


def test_2(solution: Solution):
    assert -1 == solution.minimum_sum_subarray([-2, 2, -3, 1], 2, 3)


def test_3(solution: Solution):
    assert 3 == solution.minimum_sum_subarray([1, 2, 3, 4], 2, 4)


def test_4(solution: Solution):
    assert 25 == solution.minimum_sum_subarray([25, -9], 1, 1)


def test_5(solution: Solution):
    assert 8 == solution.minimum_sum_subarray([-12, 8], 1, 1)
