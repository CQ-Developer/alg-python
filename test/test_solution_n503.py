from pytest import fixture

from src.solution_n503 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [2, -1, 2] == solution.next_greater_elements([1, 2, 1])


def test_2(solution: Solution):
    assert [2, 3, 4, -1, 4] == solution.next_greater_elements([1, 2, 3, 4, 3])
