import pytest

from src.n321 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_number(solution: Solution, case: Case):
    assert solution.max_number(case["nums1"], case["nums2"], case["k"]) == case["expected"]
