import pytest

from src.n2555 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximize_win(solution: Solution, case: Case):
    assert solution.maximize_win(case["prize_positions"], case["k"]) == case["expected"]
