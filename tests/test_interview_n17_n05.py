import pytest

from src.interview_n17_n05 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_longest_subarray(solution: Solution, case: Case):
    assert solution.find_longest_subarray(case["array"]) == case["expected"]
