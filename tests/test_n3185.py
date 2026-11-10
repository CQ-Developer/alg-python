import pytest

from src.n3185 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_complete_day_pairs(solution: Solution, case: Case):
    assert solution.count_complete_day_pairs(case["hours"]) == case["expected"]
