import pytest

from src.n1542 import Solution, SolutionA


@pytest.fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.longest_awesome("3242415") == 5


def test_2(solution: Solution):
    assert solution.longest_awesome("12345678") == 1


def test_3(solution: Solution):
    assert solution.longest_awesome("213123") == 6


def test_4(solution: Solution):
    assert solution.longest_awesome("00") == 2
