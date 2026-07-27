from pytest import fixture

from src.solution_n85 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 6 == solution.maximal_rectangle(
        [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]
    )


def test_b(solution: Solution):
    assert 0 == solution.maximal_rectangle([['0']])


def test_c(solution: Solution):
    assert 1 == solution.maximal_rectangle([['1']])
