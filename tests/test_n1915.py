import pytest

from src.n1915 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.wonderful_substrings("aba") == 4


def test_2(solution: Solution):
    assert solution.wonderful_substrings("aabb") == 9


def test_3(solution: Solution):
    assert solution.wonderful_substrings("he") == 2
