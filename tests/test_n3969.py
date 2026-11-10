import pytest

from src.n3969 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_valid_subarrays(solution: Solution, case: Case):
    assert solution.count_valid_subarrays(case["nums"], case["x"]) == case["expected"]
