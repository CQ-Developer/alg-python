import pytest

from src.n28 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_str_str(solution: Solution, case: Case):
    assert solution.str_str(case["haystack"], case["needle"]) == case["expected"]
