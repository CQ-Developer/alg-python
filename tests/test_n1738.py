import pytest

from src.n1738 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_kth_largest_value(solution: Solution, case: Case):
    assert solution.kth_largest_value(case["matrix"], case["k"]) == case["expected"]
