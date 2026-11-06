from pytest import fixture

from src.n69 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.my_sqrt(4)


def test_2(solution: Solution):
    assert 2 == solution.my_sqrt(8)
