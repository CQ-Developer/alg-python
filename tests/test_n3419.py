import pytest

from src.n3419 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_min_max_weight(solution: Solution, case: Case):
    assert solution.minMaxWeight(case["n"], case["edges"], case["threshold"]) == case["expected"]
