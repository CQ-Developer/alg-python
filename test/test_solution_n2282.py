from pytest import fixture

from src.solution_n2282 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [[2, 1, 2, 1, 0]] == solution.see_people([[3, 1, 4, 2, 5]])


def test_b(solution: Solution):
    assert [[3, 1], [2, 1], [1, 0]] == solution.see_people([[5, 1], [3, 1], [4, 1]])
