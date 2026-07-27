from pytest import fixture

from src.solution_n2748 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.count_beautiful_pairs([2, 5, 1, 4])


def test_2(solution: Solution):
    assert 2 == solution.count_beautiful_pairs([11, 21, 12])
