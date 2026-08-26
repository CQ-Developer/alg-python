from pytest import fixture

from src.n2967 import Solution, SolutionA


@fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 6 == solution.minimum_cost([1, 2, 3, 4, 5])


def test_2(solution: Solution):
    assert 11 == solution.minimum_cost([10, 12, 13, 14, 15])


def test_3(solution: Solution):
    assert 22 == solution.minimum_cost([22, 33, 22, 33, 22])
