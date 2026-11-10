import pytest

from src.n3756 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sum_and_multiply(solution: Solution, case: Case):
    assert solution.sum_and_multiply(case["s"], case["queries"]) == case["expected"]
