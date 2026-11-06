from pytest import fixture

from src.n1534 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.count_good_triplets([3, 0, 1, 1, 9, 7], 7, 2, 3)


def test_b(solution: Solution):
    assert 0 == solution.count_good_triplets([1, 1, 2, 2, 3], 0, 0, 1)
