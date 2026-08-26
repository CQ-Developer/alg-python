from pytest import fixture

from src.n1201 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.nthUglyNumber(3, 2, 3, 5)


def test_2(solution: Solution):
    assert 6 == solution.nthUglyNumber(4, 2, 3, 4)


def test_3(solution: Solution):
    assert 10 == solution.nthUglyNumber(5, 2, 11, 13)
