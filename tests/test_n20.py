import pytest

from src.n20 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_is_valid(solution: Solution, case: Case):
    assert solution.is_valid(case["s"]) == case["expected"]
