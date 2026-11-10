import pytest

from src.n454 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_four_sum_count(solution: Solution, case: Case):
    assert solution.four_sum_count(case["nums1"], case["nums2"], case["nums3"], case["nums4"]) == case["expected"]
