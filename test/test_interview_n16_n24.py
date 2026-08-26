from pytest import fixture

from src.interview_n16_n24 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [[5, 6]] == solution.pair_sums([5, 6, 5], 11)


def test_2(solution: Solution):
    assert [[5, 6], [5, 6]] == solution.pair_sums([5, 6, 5, 6], 11)
