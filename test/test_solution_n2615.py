from pytest import fixture

from src.solution_n2615 import Solution, SolutionA, SolutionB


@fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [5, 0, 3, 4, 0] == solution.distance([1, 3, 1, 1, 2])


def test_2(solution: Solution):
    assert [0, 0, 0] == solution.distance([0, 5, 3])
