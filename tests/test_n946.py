import pytest

from src.n946 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_validate_stack_sequences(solution: Solution, case: Case):
    assert solution.validate_stack_sequences(case["pushed"], case["popped"]) == case["expected"]
