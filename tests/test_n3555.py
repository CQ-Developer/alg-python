import pytest

from src.n3555 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_min_subarray_sort(solution: Solution, case: Case):
    assert solution.min_subarray_sort(case["nums"], case["k"]) == case["expected"]
