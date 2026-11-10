import pytest

from src.n3116 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_kth_smallest(solution: Solution, case: Case):
    assert solution.find_kth_smallest(case["coins"], case["k"]) == case["expected"]
