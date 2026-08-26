import pytest

from src.solution_n1371 import Solution, SolutionA


@pytest.fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.find_the_longest_substring("eleetminicoworoep") == 13


def test_2(solution: Solution):
    assert solution.find_the_longest_substring("leetcodeisgreat") == 5


def test_3(solution: Solution):
    assert solution.find_the_longest_substring("bcbcbc") == 6
