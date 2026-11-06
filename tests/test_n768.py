from pytest import fixture

from src.n768 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.max_chunks_to_sorted([5, 4, 3, 2, 1])


def test_2(solution: Solution):
    assert 4 == solution.max_chunks_to_sorted([2, 1, 3, 4, 4])
