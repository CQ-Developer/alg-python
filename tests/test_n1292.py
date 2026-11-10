import pytest

from src.n1292 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_side_length(solution: Solution, case: Case):
    assert solution.max_side_length(case["mat"], case["threshold"]) == case["expected"]
