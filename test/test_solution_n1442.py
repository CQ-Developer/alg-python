from pytest import fixture

from src.solution_n1442 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.count_triplets([2, 3, 1, 6, 7])


def test_b(solution: Solution):
    assert 10 == solution.count_triplets([1, 1, 1, 1, 1])
