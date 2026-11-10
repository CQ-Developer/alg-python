import pytest

from src.n844 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_backspace_compare(solution: Solution, case: Case):
    assert solution.backspace_compare(case["s"], case["t"]) == case["expected"]
