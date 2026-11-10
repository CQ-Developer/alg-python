import pytest

from src.n2348 import Solution, SolutionA, SolutionB, SolutionC, SolutionD, SolutionE
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC, SolutionD, SolutionE])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_zero_filled_subarray(solution: Solution, case: Case):
    assert solution.zero_filled_subarray(case["nums"]) == case["expected"]
