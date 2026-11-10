import pytest

from src.n739 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_daily_temperatures(solution: Solution, case: Case):
    assert solution.daily_temperatures(case["temperatures"]) == case["expected"]
