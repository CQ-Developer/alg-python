from pytest import fixture

from src.n1010 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.num_pairs_divisible_by_60([30, 20, 150, 100, 40])


def test_2(solution: Solution):
    assert 3 == solution.num_pairs_divisible_by_60([60, 60, 60])
