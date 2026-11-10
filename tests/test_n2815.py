import pytest

from src.n2815 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_sum(solution: Solution, case: Case):
    assert solution.max_sum(case["nums"]) == case["expected"]
