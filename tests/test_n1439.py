import pytest

from src.n1439 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_kth_smallest(solution: Solution, case: Case):
    assert solution.kth_smallest(case["mat"], case["k"]) == case["expected"]
