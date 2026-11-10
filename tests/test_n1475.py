import pytest

from src.n1475 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_final_prices(solution: Solution, case: Case):
    assert solution.final_prices(case["prices"]) == case["expected"]
