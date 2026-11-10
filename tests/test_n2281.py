import pytest

from src.n2281 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_total_strength(solution: Solution, case: Case):
    assert solution.total_strength(case["strength"]) == case["expected"]
