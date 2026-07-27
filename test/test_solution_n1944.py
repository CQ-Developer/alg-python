from pytest import fixture

from src.solution_n1944 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [3, 1, 2, 1, 1, 0] == solution.can_see_persons_count([10, 6, 8, 5, 11, 9])


def test_b(solution: Solution):
    assert [4, 1, 1, 1, 0] == solution.can_see_persons_count([5, 1, 2, 3, 10])
