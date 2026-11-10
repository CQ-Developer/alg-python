import pytest

from src.n974 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_subarrays_div_by_k(solution: Solution, case: Case):
    assert solution.subarrays_div_by_k(case["nums"], case["k"]) == case["expected"]
