import pytest

from src.n496 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_next_greater_element(solution: Solution, case: Case):
    assert solution.next_greater_element(case["a"], case["b"]) == case["expected"]
