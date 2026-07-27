from pytest import fixture

from src.solution_n668 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.findKthNumber(3, 3, 5)


def test_2(solution: Solution):
    assert 6 == solution.findKthNumber(2, 3, 6)


def test_3(solution: Solution):
    assert 31666344 == solution.findKthNumber(9895, 28405, 100787757)


def test_4(solution: Solution):
    assert 23437314 == solution.findKthNumber(17452, 29185, 95573422)
