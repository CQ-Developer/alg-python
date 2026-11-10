import pytest

from src.n3412 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_calculate_score(solution: Solution, case: Case):
    assert solution.calculate_score(case["s"]) == case["expected"]
