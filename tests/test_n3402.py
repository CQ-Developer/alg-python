import pytest

from src.n3402 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_operations(solution: Solution, case: Case):
    assert solution.minimum_operations(case["grid"]) == case["expected"]
