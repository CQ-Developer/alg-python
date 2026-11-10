import pytest

from src.n2736 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_sum_queries(solution: Solution, case: Case):
    assert solution.maximum_sum_queries(case["nums1"], case["nums2"], case["queries"]) == case["expected"]
