from pytest import fixture

from src.solution_n2949 import Solution, SolutionA, SolutionB, SolutionC, SolutionD


@fixture(scope="module", params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.beautiful_substrings("baeyh", 2)


def test_2(solution: Solution):
    assert 3 == solution.beautiful_substrings("abba", 1)


def test_3(solution: Solution):
    assert 0 == solution.beautiful_substrings("bcdf", 1)
