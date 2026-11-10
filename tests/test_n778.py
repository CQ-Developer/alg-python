import pytest

from src.n778 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_swim_in_water(solution: Solution, case: Case):
    assert solution.swimInWater(case["grid"]) == case["expected"]
