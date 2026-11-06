from pytest import fixture

from src.n3267 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.count_pair([1023, 2310, 2130, 213])


def test_2(solution: Solution):
    assert 3 == solution.count_pair([1, 10, 100])
