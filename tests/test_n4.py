import pytest

from src.n4 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_median_sorted_arrays(solution: Solution, case: Case):
    assert solution.find_median_sorted_arrays(case["nums1"], case["nums2"]) == case["expected"]
