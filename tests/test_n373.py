import pytest

from src.n373 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_k_smallest_pairs(solution: Solution, case: Case):
    assert solution.kSmallestPairs(case["nums1"], case["nums2"], case["k"]) == case["expected"]
