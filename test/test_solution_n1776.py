from pytest import fixture

from src.solution_n1776 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [1.0, -1.0, 3.0, -1.0] == solution.get_collision_times([[1, 2], [2, 1], [4, 3], [7, 2]])


def test_b(solution: Solution):
    assert [2.0, 1.0, 1.5, -1.0] == solution.get_collision_times([[3, 4], [5, 4], [6, 3], [9, 1]])
