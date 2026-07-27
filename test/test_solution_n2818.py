from pytest import fixture

from src.solution_n2818 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 81 == solution.maximum_score([8, 3, 9, 3, 8], 2)


def test_b(solution: Solution):
    assert 4788 == solution.maximum_score([19, 12, 14, 6, 10, 18], 3)
