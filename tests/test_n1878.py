import pytest

from src.n1878 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_get_biggest_three(solution: Solution, case: Case):
    assert solution.get_biggest_three(case["grid"]) == case["expected"]
