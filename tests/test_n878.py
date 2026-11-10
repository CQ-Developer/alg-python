import pytest

from src.n878 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_nth_magical_number(solution: Solution, case: Case):
    assert solution.nthMagicalNumber(case["n"], case["a"], case["b"]) == case["expected"]
