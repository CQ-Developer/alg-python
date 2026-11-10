import pytest

from src.n3364 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_sum_subarray(solution: Solution, case: Case):
    assert solution.minimum_sum_subarray(case["nums"], case["l"], case["r"]) == case["expected"]
