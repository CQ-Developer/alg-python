import pytest

from src.n3652 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_profit(solution: Solution, case: Case):
    assert solution.max_profit(case["prices"], case["strategy"], case["k"]) == case["expected"]
