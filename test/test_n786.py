from pytest import fixture

from src.n786 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [2, 5] == solution.kth_smallest_prime_fraction([1, 2, 3, 5], 3)


def test_2(solution: Solution):
    assert [1, 7] == solution.kth_smallest_prime_fraction([1, 7], 1)
