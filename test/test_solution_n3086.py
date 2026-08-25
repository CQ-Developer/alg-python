import pytest

from src.solution_n3086 import Solution, SolutionA


@pytest.fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.minimum_moves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1)


def test_2(solution: Solution):
    assert 4 == solution.minimum_moves([0, 0, 0, 0], 2, 3)
