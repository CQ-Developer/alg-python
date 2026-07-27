from pytest import fixture

from src.solution_n946 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])


def test_2(solution: Solution):
    assert not solution.validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
