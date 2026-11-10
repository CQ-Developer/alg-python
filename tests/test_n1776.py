import pytest

from src.n1776 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_get_collision_times(solution: Solution, case: Case):
    assert solution.get_collision_times(case["cars"]) == case["expected"]
