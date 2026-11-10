import pytest

from src.n2845 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_interesting_subarrays(solution: Solution, case: Case):
    assert solution.count_interesting_subarrays(case["nums"], case["m"], case["k"]) == case["expected"]
