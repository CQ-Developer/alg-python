import pytest

from src.n3728 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_stable_subarrays(solution: Solution, case: Case):
    assert solution.count_stable_subarrays(case["capacity"]) == case["expected"]
