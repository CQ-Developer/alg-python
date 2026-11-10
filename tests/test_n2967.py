import pytest

from src.n2967 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_cost(solution: Solution, case: Case):
    assert solution.minimum_cost(case["nums"]) == case["expected"]
