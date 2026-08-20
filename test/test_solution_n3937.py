from pytest import fixture

from src.solution_n3937 import Solution, SolutionA, SolutionB


@fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.min_operations([1, 4, 2, 8], 3)


def test_2(solution: Solution):
    assert 1 == solution.min_operations([1, 1, 1], 3)
