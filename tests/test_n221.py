from pytest import fixture

from src.n221 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.maximal_square(
        [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]
    )


def test_b(solution: Solution):
    assert 1 == solution.maximal_square([['0', '1'], ['1', '0']])


def test_c(solution: Solution):
    assert 0 == solution.maximal_square([['0']])
