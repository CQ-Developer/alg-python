import pytest

from src.n2528 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_power(solution: Solution, case: Case):
    assert solution.maxPower(case["stations"], case["r"], case["k"]) == case["expected"]
