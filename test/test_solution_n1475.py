from pytest import fixture

from src.solution_n1475 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [4, 2, 4, 2, 3] == solution.final_prices([8, 4, 6, 2, 3])


def test_2(solution: Solution):
    assert [1, 2, 3, 4, 5] == solution.final_prices([1, 2, 3, 4, 5])


def test_3(solution: Solution):
    assert [9, 0, 1, 6] == solution.final_prices([10, 1, 1, 6])
