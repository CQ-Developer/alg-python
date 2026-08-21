from pytest import fixture

from src.solution_n2968 import Solution, SolutionA, SolutionB


@fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.max_frequency_score([1, 2, 6, 4], 3)


def test_2(solution: Solution):
    assert 3 == solution.max_frequency_score([1, 4, 4, 2, 4], 0)
