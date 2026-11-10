import pytest

from src.n3480 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_subarrays(solution: Solution, case: Case):
    assert solution.max_subarrays(case["n"], case["conflicting_pairs"]) == case["expected"]
