import pytest

from src.n2260 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_card_pickup(solution: Solution, case: Case):
    assert solution.minimum_card_pickup(case["cards"]) == case["expected"]
