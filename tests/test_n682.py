import pytest

from src.n682 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_cal_points(solution: Solution, case: Case):
    assert solution.cal_points(case["operations"]) == case["expected"]
