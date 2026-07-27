from pytest import fixture

from src.solution_n2559 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [2, 3, 0] == solution.vowel_strings(['aba', 'bcb', 'ece', 'aa', 'e'], [[0, 2], [1, 4], [1, 1]])


def test_b(solution: Solution):
    assert [3, 2, 1] == solution.vowel_strings(['a', 'e', 'i'], [[0, 2], [0, 1], [2, 2]])
