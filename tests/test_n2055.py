import pytest

from src.n2055 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_plates_between_candles(solution: Solution, case: Case):
    assert solution.plates_between_candles(case["s"], case["queries"]) == case["expected"]
