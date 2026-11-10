import pytest

from src.n503 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_next_greater_elements(solution: Solution, case: Case):
    assert solution.next_greater_elements(case["nums"]) == case["expected"]
