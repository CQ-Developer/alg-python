import pytest

from src.n755 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_pour_water(solution: Solution, case: Case):
    assert solution.pour_water(case["heights"], case["volume"], case["k"]) == case["expected"]
