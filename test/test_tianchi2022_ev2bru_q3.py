from pytest import fixture

from src.tianchi2022_ev2bru_q3 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [5, 5, 6] == solution.arrange_bookshelf([5, 5, 6, 5], 2)


def test_b(solution: Solution):
    assert [5, 5, 6, 5] == solution.arrange_bookshelf([5, 5, 6, 5], 3)


def test_c(solution: Solution):
    assert [3, 8, 9, 2] == solution.arrange_bookshelf([3, 3, 9, 8, 9, 2, 8], 1)


def test_d(solution: Solution):
    assert [1, 2, 2, 1, 3, 3] == solution.arrange_bookshelf([2, 1, 2, 2, 1, 3, 3, 1, 3, 3], 2)
