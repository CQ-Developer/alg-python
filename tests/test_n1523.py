import pytest

from src.n1523 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_odds(solution: Solution, case: Case):
    assert solution.count_odds(case["low"], case["high"]) == case["expected"]
