from pytest import fixture

from src.solution_n2555 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 7 == solution.maximize_win([1, 1, 2, 2, 3, 3, 5], 2)


def test_2(solution: Solution):
    assert 2 == solution.maximize_win([1, 2, 3, 4], 0)
