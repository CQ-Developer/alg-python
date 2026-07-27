from pytest import fixture

from src.solution_n1014 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 11 == solution.max_score_sightseeing_pair([8, 1, 5, 2, 6])


def test_2(solution: Solution):
    assert 2 == solution.max_score_sightseeing_pair([1, 2])
