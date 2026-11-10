import pytest

from src.n853 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_car_fleet(solution: Solution, case: Case):
    assert solution.car_fleet(case["target"], case["position"], case["speed"]) == case["expected"]
