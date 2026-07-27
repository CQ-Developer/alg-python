from pytest import fixture

from src.solution_n3584 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 81 == solution.maximum_product([-1, -9, 2, 3, -2, -3, 1], 1)


def test_2(solution: Solution):
    assert 20 == solution.maximum_product([1, 3, -5, 5, 6, -4], 3)


def test_3(solution: Solution):
    assert 35 == solution.maximum_product([2, -1, 2, -6, 5, 2, -5, 7], 2)
