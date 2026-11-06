from pytest import fixture

from src.n2506 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.similar_pairs(['aba', 'aabb', 'abcd', 'bac', 'aabc'])


def test_2(solution: Solution):
    assert 3 == solution.similar_pairs(['aabb', 'ab', 'ba'])


def test_3(solution: Solution):
    assert 0 == solution.similar_pairs(['nba', 'cba', 'dba'])
