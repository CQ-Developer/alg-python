from pytest import fixture

from src.solution_n2602 import Solution, SolutionA


@fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [14, 10] == solution.min_operations([3, 1, 6, 8], [1, 5])


def test_2(solution: Solution):
    assert [20] == solution.min_operations([2, 9, 6, 3], [10])
