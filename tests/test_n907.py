import pytest

from src.n907 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sum_subarray_mins(solution: Solution, case: Case):
    assert solution.sum_subarray_mins(case["arr"]) == case["expected"]
