from pytest import fixture

from src.solution_n1930 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 3 == solution.count_palindromic_subsequence('aabca')


def test_b(solution: Solution):
    assert 0 == solution.count_palindromic_subsequence('adc')


def test_c(solution: Solution):
    assert 4 == solution.count_palindromic_subsequence('bbcbaba')
