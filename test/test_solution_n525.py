from pytest import fixture

from src.solution_n525 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.find_max_length([0, 1])


def test_b(solution: Solution):
    assert 2 == solution.find_max_length([0, 1, 0])


def test_c(solution: Solution):
    assert 6 == solution.find_max_length([0, 1, 1, 1, 1, 1, 0, 0, 0])
