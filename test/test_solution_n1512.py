from pytest import fixture

from src.solution_n1512 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.num_identical_pairs([1, 2, 3, 1, 1, 3])


def test_2(solution: Solution):
    assert 6 == solution.num_identical_pairs([1, 1, 1, 1])


def test_3(solution: Solution):
    assert 0 == solution.num_identical_pairs([1, 2, 3])
