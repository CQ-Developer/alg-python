import pytest

from src.n2812 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_safeness_factor(solution: Solution, case: Case):
    assert solution.maximumSafenessFactor(case["grid"]) == case["expected"]
