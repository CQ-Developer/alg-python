from pytest import fixture

from src.solution_n1685 import Solution, SolutionA, SolutionB


@fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [4, 3, 5] == solution.get_sum_absolute_differences([2, 3, 5])


def test_2(solution: Solution):
    assert [24, 15, 13, 15, 21] == solution.get_sum_absolute_differences([1, 4, 6, 8, 10])
