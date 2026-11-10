import pytest

from src.n1508 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_range_sum(solution: Solution, case: Case):
    assert solution.range_sum(case["nums"], case["n"], case["left"], case["right"]) == case["expected"]
