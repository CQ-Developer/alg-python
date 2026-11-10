import pytest

from src.lcp_n12 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_min_time(solution: Solution, case: Case):
    assert solution.minTime(case["time"], case["m"]) == case["expected"]
