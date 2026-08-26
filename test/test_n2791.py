import pytest

from src.n2791 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.count_palindrome_paths([-1, 0, 0, 1, 1, 2], "acaabc") == 8


def test_2(solution: Solution):
    assert solution.count_palindrome_paths([-1, 0, 0, 0, 0], "aaaaa") == 10
