import pytest

from src.n848 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_shifting_letters(solution: Solution, case: Case):
    assert solution.shifting_letters(case["s"], case["shifts"]) == case["expected"]
